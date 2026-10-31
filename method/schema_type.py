"""Print GraphQL types in full from a schema an observed repository holds, with the citation a quote from them takes.

Usage: python3 -I method/schema_type.py STRUCTURE_DIR TYPE [TYPE ...]
       python3 -I method/schema_type.py STRUCTURE_DIR --search WORD [WORD ...]
  e.g. python3 -I method/schema_type.py /home/user/observed-sh/structures/shopify/admin-graphql-schema/2026-10 Market

A schema structure's items.jsonl keeps each description only up to its first line break, so a longer description
is cut short there. The full text is in the introspection answer its meta.json names, a record of a fetch archive
held in git. This prints each type from that record: its description, then each field, input field or enum value
with its type and description. --search lists the types whose name or description holds any WORD.

A quote from it is cited with the source and locator printed at the top, which method/quote_check.py reads. A
field's or value's name is printed with its description below it, as the schema holds them one after the other, so
"<name> <description>" can be quoted. Lines in square brackets are this tool's own, never the schema's words.
"""
import json, os, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from warc_text import read_record


def type_name(t):
    if not t:
        return ""
    if t.get("kind") == "NON_NULL":
        return type_name(t.get("ofType")) + "!"
    if t.get("kind") == "LIST":
        return "[" + type_name(t.get("ofType")) + "]"
    return t.get("name") or ""


def load(structure):
    meta = json.load(open(os.path.join(structure, "meta.json"), encoding="utf-8"))["source"]
    root = subprocess.run(["git", "-C", structure, "rev-parse", "--show-toplevel"], capture_output=True, text=True,
                          check=True).stdout.strip()
    commit = subprocess.run(["git", "-C", root, "rev-parse", "HEAD"], capture_output=True, text=True,
                            check=True).stdout.strip()
    cdx = os.path.join(root, os.path.dirname(meta["warc"]), "fetch.cdx")
    offset = None
    for line in open(cdx, encoding="utf-8"):      # CDX a b a m s k r M V g u: V, the ninth, is the offset
        f = line.split()
        if len(f) == 11 and f[10] == meta["record_id"]:
            offset = int(f[8])
    if offset is None:
        sys.exit(f"no record {meta['record_id']} in {cdx}")
    warc, status, headers, body = read_record(os.path.join(root, meta["warc"]), offset)
    data = json.loads(body.decode("utf-8"))
    types = (data.get("data") or data)["__schema"]["types"]
    return f"{os.path.basename(root)}@{commit}:{meta['warc']}", offset, {t["name"]: t for t in types}


def show(t):
    print(f"## {t['name']} [{t['kind']}]")
    print(t.get("description") or "[no description]")
    for key in ("fields", "inputFields", "enumValues"):
        for f in t.get(key) or []:
            print(f["name"])                            # the name, then its description, as the schema holds them
            if f.get("description"):
                print("    " + f["description"].replace("\n", "\n    "))
            ty = type_name(f.get("type"))
            if ty or f.get("isDeprecated"):
                print("    [" + "; ".join(x for x in (f"type {ty}" if ty else "",
                                                     f"deprecated: {f.get('deprecationReason')}" if f.get("isDeprecated") else "") if x) + "]")
    print()


def main(argv):
    if len(argv) < 2:
        sys.exit(__doc__)
    source, offset, types = load(argv[0])
    print(f"source: {source}\nlocator: {offset} (type <name>)\n")
    if argv[1] == "--search":
        words = [w.lower() for w in argv[2:]]
        for name, t in sorted(types.items()):
            text = (name + " " + (t.get("description") or "")).lower()
            if any(w in text for w in words):
                print(f"{name} ({t['kind']}): {(t.get('description') or '').splitlines()[0][:160] if t.get('description') else ''}")
        return
    for name in argv[1:]:
        if name not in types:
            print(f"## {name}: not a type of this schema\n")
            continue
        show(types[name])


if __name__ == "__main__":
    main(sys.argv[1:])
