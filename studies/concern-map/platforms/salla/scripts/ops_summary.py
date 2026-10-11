# Summarize docs-operations items: position, method, path, summary, tags, scope lines.
# Usage: python3 -I ops_summary.py ITEMS_JSONL
import json, sys, re

for line in open(sys.argv[1], encoding="utf-8"):
    it = json.loads(line)
    doc = it["document"]
    for p, ops in doc.get("paths", {}).items():
        for m, op in ops.items():
            if not isinstance(op, dict):
                continue
            desc = op.get("description", "") or ""
            scopes = re.findall(r"`([a-z_\.]+)`\s*-\s*([^\n<]+)", desc)
            tags = op.get("tags", [])
            servers = [s.get("url") for s in doc.get("servers", [])]
            print("\t".join([str(it["position"]), m.upper(), p, op.get("summary", ""),
                             " | ".join(tags), "; ".join(f"{a}={b.strip()}" for a, b in scopes),
                             " ".join(servers or [])]))
