#!/usr/bin/env python3
"""Local estimated-credit ledger. Records observations; never stops agents."""
import argparse
from contextlib import contextmanager
from datetime import datetime, timezone
import json
import math
import os
from pathlib import Path
import tempfile


def number(value):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError("Expected a finite nonnegative number")
    if not math.isfinite(value) or value < 0:
        raise ValueError("Expected a finite nonnegative number")
    return value


def new_ledger(scope, limit, rates):
    if not scope or not rates.get("source") or not rates.get("date"):
        raise ValueError("Scope, rate source and date are required")
    if not rates.get("models"):
        raise ValueError("At least one model rate is required")
    for rate in rates["models"].values():
        for key in ("input", "cached_input", "output"):
            number(rate[key])
    return {"version": 1, "rates": rates, "scopes": {
        scope: {"parent": None, "limit": number(limit), "decision": "initial grant"}
    }, "sessions": {}}


def children(data, scope):
    return [key for key, value in data["scopes"].items()
            if value["parent"] == scope]


def spent(data, scope):
    direct = sum(s["credits"] for s in data["sessions"].values()
                 if s["scope"] == scope)
    return direct + sum(spent(data, child) for child in children(data, scope))


def committed(data, scope):
    direct = sum(s["credits"] for s in data["sessions"].values()
                 if s["scope"] == scope)
    return direct + sum(max(data["scopes"][c]["limit"], committed(data, c))
                        for c in children(data, scope))


def allocate(data, parent, scope, limit, decision):
    number(limit)
    if parent not in data["scopes"] or scope in data["scopes"] or not scope:
        raise ValueError("Unknown parent or duplicate/empty scope")
    if not decision:
        raise ValueError("An authorization reference is required")
    if committed(data, parent) + limit > data["scopes"][parent]["limit"] + 1e-9:
        raise ValueError("Allocation exceeds parent's unreserved allowance")
    data["scopes"][scope] = {"parent": parent, "limit": limit, "decision": decision}


def set_limit(data, scope, limit, decision):
    number(limit)
    if not decision:
        raise ValueError("An authorization reference is required")
    entry = data["scopes"][scope]
    if limit + 1e-9 < committed(data, scope):
        raise ValueError("Cannot reduce below observed spending or reservations")
    parent = entry["parent"]
    if parent is not None:
        old_commitment = max(entry["limit"], committed(data, scope))
        if committed(data, parent) - old_commitment + limit > data["scopes"][parent]["limit"] + 1e-9:
            raise ValueError("Increase exceeds parent's unreserved allowance")
    entry.update(limit=limit, decision=decision)


def register(data, scope, session, model, speed=1):
    number(speed)
    if speed == 0 or scope not in data["scopes"] or not session:
        raise ValueError("Positive speed multiplier, known scope and session required")
    if model not in data["rates"]["models"]:
        raise ValueError("No supplied rate for model")
    existing = data["sessions"].get(session)
    identity = {"scope": scope, "model": model, "speed": speed}
    if existing:
        if any(existing[k] != v for k, v in identity.items()):
            raise ValueError("Session scope/model/speed cannot change")
        return existing
    entry = dict(identity, counters=None, credits=0, observed_at=None)
    data["sessions"][session] = entry
    return entry


def observe(data, scope, session, model, counters, speed=1):
    for key in ("input", "cached_input", "output", "reasoning_output"):
        value = counters[key]
        number(value)
        if not isinstance(value, int):
            raise ValueError("Token counters must be integers")
    if counters["cached_input"] > counters["input"] or counters["reasoning_output"] > counters["output"]:
        raise ValueError("Cached/reasoning tokens are subsets, not extra tokens")
    existing = data["sessions"].get(session)
    if existing and existing["counters"]:
        if any(counters[k] < existing["counters"][k] for k in counters):
            raise ValueError("Cumulative counters decreased; investigate before importing")
        old = existing["counters"]
        if counters["input"]-old["input"] < counters["cached_input"]-old["cached_input"]:
            raise ValueError("Cumulative uncached input decreased")
        if counters["output"]-old["output"] < counters["reasoning_output"]-old["reasoning_output"]:
            raise ValueError("Cumulative non-reasoning output decreased")
    entry = register(data, scope, session, model, speed)
    rate = data["rates"]["models"][model]
    credits = ((counters["input"] - counters["cached_input"]) * rate["input"]
               + counters["cached_input"] * rate["cached_input"]
               + counters["output"] * rate["output"]) * speed / 1_000_000
    entry.update(counters=dict(counters), credits=credits,
                 observed_at=datetime.now(timezone.utc).isoformat())


def report(data):
    result = {}
    for scope, entry in data["scopes"].items():
        total, reserved, limit = spent(data, scope), committed(data, scope), entry["limit"]
        result[scope] = dict(entry, observed_spend=total, committed=reserved,
                            unallocated=limit-reserved, remaining=limit-total,
                            status="exhausted" if total >= limit else
                            "reassess" if total >= .8 * limit else "within")
    return {"scopes": result, "sessions": data["sessions"],
            "unknown_sessions": [k for k, v in data["sessions"].items() if v["counters"] is None],
            "notice": "Observed cumulative totals only. Register every session; refresh before decisions. "
                      "Unregistered sessions cannot be detected. Rates do not measure actual quota."}


@contextmanager
def lock(path):
    # Local macOS/Linux host only; not a distributed or network filesystem lock.
    import fcntl
    path.parent.mkdir(parents=True, exist_ok=True)
    with Path(str(path) + ".lock").open("a") as handle:
        fcntl.flock(handle, fcntl.LOCK_EX)
        yield


def save(path, data):
    fd, name = tempfile.mkstemp(prefix=".allowance-", dir=str(path.parent))
    try:
        with os.fdopen(fd, "w") as handle:
            json.dump(data, handle, indent=2, allow_nan=False)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(name, path)
    finally:
        if os.path.exists(name):
            os.unlink(name)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    for name in ("init", "allocate", "set-limit", "register", "observe", "report"):
        p = commands.add_parser(name)
        p.add_argument("--ledger", type=Path, required=True)
        if name != "report":
            p.add_argument("--scope", required=True)
        if name in ("init", "allocate", "set-limit"):
            p.add_argument("--limit", type=float, required=True)
        if name == "init":
            p.add_argument("--rates", type=Path, required=True)
        if name == "allocate":
            p.add_argument("--parent", required=True)
        if name in ("allocate", "set-limit"):
            p.add_argument("--decision", required=True)
        if name in ("register", "observe"):
            p.add_argument("--session", required=True)
            p.add_argument("--model", required=True)
            p.add_argument("--speed", type=float, default=1)
        if name == "observe":
            for key in ("input", "cached-input", "output", "reasoning-output"):
                p.add_argument("--" + key, type=int, required=True)
    args = parser.parse_args()
    try:
        with lock(args.ledger):
            if args.command == "init":
                if args.ledger.exists():
                    raise ValueError("Ledger exists; refusing to reset accounting")
                data = new_ledger(args.scope, args.limit, json.loads(args.rates.read_text()))
            else:
                data = json.loads(args.ledger.read_text())
                if data.get("version") != 1:
                    raise ValueError("Unsupported ledger version")
                if args.command == "allocate":
                    allocate(data, args.parent, args.scope, args.limit, args.decision)
                elif args.command == "set-limit":
                    set_limit(data, args.scope, args.limit, args.decision)
                elif args.command in ("register", "observe"):
                    values = (data, args.scope, args.session, args.model)
                    if args.command == "register":
                        register(*values, speed=args.speed)
                    else:
                        observe(*values, counters={k: getattr(args, k) for k in
                                ("input", "cached_input", "output", "reasoning_output")}, speed=args.speed)
            if args.command != "report":
                save(args.ledger, data)
            print(json.dumps(report(data), indent=2, allow_nan=False))
    except (OSError, ValueError, KeyError, ImportError) as exc:
        parser.exit(1, "allowance: " + str(exc) + "\n")


if __name__ == "__main__":
    main()
