#!/usr/bin/env python3
"""Small native Codex adapters; no session launch or daemon management."""
import argparse
import json
from pathlib import Path
import queue
import subprocess
import threading
import time


def usage(path):
    latest = None
    thread_id = None
    with Path(path).open() as handle:
        for line in handle:
            try:
                item = json.loads(line)
            except json.JSONDecodeError:
                if not line.endswith("\n"):
                    continue  # Writer may still be appending its last record.
                raise ValueError("Malformed complete JSONL record")
            payload = item.get("payload") or {}
            candidate = payload.get("thread_id") if item.get("type") == "token_usage_record" else None
            if item.get("type") == "session_meta":
                candidate = payload.get("id")
            if candidate:
                if thread_id and thread_id != candidate:
                    raise ValueError("Mixed thread identities; select one session log")
                thread_id = candidate
            counters = None
            if item.get("type") == "token_usage_record":
                counters = payload.get("thread_token_usage")
            elif item.get("type") == "event_msg" and payload.get("type") == "token_count":
                counters = (payload.get("info") or {}).get("total_token_usage")
            if counters is not None:
                keys = ("input_tokens", "cached_input_tokens", "output_tokens", "reasoning_output_tokens")
                if any(not isinstance(counters.get(k), int) or isinstance(counters.get(k), bool)
                       or counters[k] < 0 for k in keys):
                    raise ValueError("Incomplete/invalid cumulative token categories")
                if counters["cached_input_tokens"] > counters["input_tokens"] or counters["reasoning_output_tokens"] > counters["output_tokens"]:
                    raise ValueError("Invalid subset counters")
                if counters.get("cache_write_input_tokens", 0):
                    raise ValueError("Cache-write accounting is unsupported; do not silently misprice it")
                latest = {"thread_id": thread_id, "observed_at": item.get("timestamp"),
                          "counters": {k: counters[k] for k in keys}}
    if latest is None:
        raise ValueError("No recognized cumulative token record found")
    return latest


class Client:
    def __init__(self, binary, timeout=20):
        self.proc = subprocess.Popen([binary, "app-server", "--listen", "stdio://"],
                                     stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                     stderr=subprocess.DEVNULL, text=True)
        self.messages = queue.Queue()
        self.sequence, self.timeout = 0, timeout
        threading.Thread(target=self._read, daemon=True).start()

    def _read(self):
        try:
            for line in self.proc.stdout:
                self.messages.put(json.loads(line))
        except (ValueError, OSError) as exc:
            self.messages.put(exc)
        finally:
            self.messages.put(None)

    def write(self, value):
        self.proc.stdin.write(json.dumps(value) + "\n")
        self.proc.stdin.flush()

    def rpc(self, method, params):
        self.sequence += 1
        self.write({"id": self.sequence, "method": method, "params": params})
        deadline = time.monotonic() + self.timeout
        while True:
            try:
                value = self.messages.get(timeout=max(0, deadline-time.monotonic()))
            except queue.Empty:
                raise TimeoutError("App-server request timed out: " + method)
            if value is None or isinstance(value, Exception):
                raise RuntimeError("App-server closed or returned invalid JSON")
            if value.get("id") == self.sequence:
                if "error" in value:
                    raise RuntimeError(str(value["error"]))
                return value["result"]

    def close(self):
        self.proc.terminate()
        try:
            self.proc.wait(timeout=3)
        except subprocess.TimeoutExpired:
            self.proc.kill()
            self.proc.wait()
        self.proc.stdin.close()
        self.proc.stdout.close()


def rename(client, thread, project, name):
    if not name.strip():
        raise ValueError("Empty session name")
    client.rpc("initialize", {"clientInfo": {"name": "agent_workflow", "version": "0.1.0"}})
    client.write({"method": "initialized", "params": {}})
    params = {"threadId": thread, "includeTurns": False}
    before = client.rpc("thread/read", params)["thread"]
    root, cwd = Path(project).resolve(), Path(before["cwd"]).resolve()
    if not root.is_dir() or (cwd != root and root not in cwd.parents):
        raise ValueError("Session is outside the explicitly selected project/worktree root")
    client.rpc("thread/name/set", {"threadId": thread, "name": name})
    after = client.rpc("thread/read", params)["thread"]
    if after.get("name") != name:
        raise RuntimeError("Session name readback did not match")
    return {"thread_id": thread, "before": before.get("name"), "name": name, "cwd": str(cwd)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    p = commands.add_parser("usage")
    p.add_argument("--file", type=Path, required=True)
    p = commands.add_parser("rename")
    p.add_argument("--thread", required=True)
    p.add_argument("--project", type=Path, required=True)
    p.add_argument("--name", required=True)
    p.add_argument("--codex", default="codex")
    p = commands.add_parser("send")
    p.add_argument("--thread", required=True)
    p.add_argument("--message-file", type=Path, required=True)
    p.add_argument("--remote")
    p.add_argument("--codex", default="codex")
    args = parser.parse_args()
    try:
        if args.command == "usage":
            result = usage(args.file)
        elif args.command == "rename":
            client = Client(args.codex)
            try:
                result = rename(client, args.thread, args.project, args.name)
            finally:
                client.close()
        else:
            message = args.message_file.read_text()
            if not message.strip():
                raise ValueError("Empty message")
            cmd = [args.codex, "queue", "--thread", args.thread, "--message", message]
            if args.remote:
                cmd += ["--remote", args.remote]
            subprocess.run(cmd, check=True, timeout=30)
            result = {"queued": True, "acknowledged": False}
        print(json.dumps(result, ensure_ascii=False))
    except (OSError, ValueError, RuntimeError, TimeoutError, subprocess.SubprocessError) as exc:
        parser.exit(1, "session: " + str(exc) + "\n")


if __name__ == "__main__":
    main()
