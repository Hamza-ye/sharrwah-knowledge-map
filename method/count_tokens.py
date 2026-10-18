"""Count the tokens an agent run processed, from its transcript.

Usage: python3 -I method/count_tokens.py [--since ISO] [--until ISO] TRANSCRIPT.jsonl ...

For each transcript, prints the tokens processed: input, output, cache reads and cache writes,
summed over its API requests, each request counted once.

A transcript writes one request over several lines, one per block of the reply (thinking, text,
each tool call), and each line repeats the request's whole usage. Counting every line counts a
request once per block. The method report's first count did that, and so roughly doubled the
pilot's figures (`studies/subjects/S-01/method-report.md`, section 12). This script counts each
request once, by its message id.

A transcript also records each request's output at its start, so output is undercounted. Output
is a small part of what a run processes, which is mostly its context read again on each turn.

--since and --until keep only requests whose timestamp falls between them, as ISO times in UTC
(such as 2026-10-17T05:00). Prints one line per transcript and, for several, the total.
"""
import json, sys

FIELDS = ("input_tokens", "output_tokens", "cache_read_input_tokens", "cache_creation_input_tokens")


def count(path, since="", until="9999"):
    """{message id: tokens} for one transcript's requests between since and until."""
    seen = {}
    with open(path, encoding="utf-8") as f:
        for line in f:
            try:
                d = json.loads(line)
            except ValueError:
                continue
            if d.get("type") != "assistant":
                continue
            ts = d.get("timestamp") or ""
            if not (since <= ts < until):
                continue
            m = d.get("message") or {}
            u = m.get("usage")
            if not u:
                continue
            seen[m.get("id") or d.get("uuid")] = sum((u.get(k) or 0) for k in FIELDS)
    return seen


def main(argv):
    since, until, paths = "", "9999", []
    it = iter(argv)
    for a in it:
        if a == "--since":
            since = next(it)
        elif a == "--until":
            until = next(it)
        else:
            paths.append(a)
    total = 0
    for p in paths:
        seen = count(p, since, until)
        n = sum(seen.values())
        total += n
        print(f"{n / 1e6:.1f}M\t{len(seen)} requests\t{p}")
    if len(paths) > 1:
        print(f"{total / 1e6:.1f}M\ttotal")


if __name__ == "__main__":
    main(sys.argv[1:])
