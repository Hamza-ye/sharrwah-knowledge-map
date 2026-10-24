# Citation registry with verbatim checks.
# Each citation is keyed by a readable KEY; build.py later assigns SH-S ids.
#
# Usage:
#   python3 -I cite.py add KEY SOURCE LOCATOR QUOTE SOURCE_DATE DATE_BASIS [ACCESS_PATH]
#     SOURCE is a URL (looked up in fetched/log.tsv, last 2xx fetch wins) or a local
#     source written as observed-sh@b46731d0:<path> or sharrwah-knowledge-map:<path>.
#     For a URL, an optional '#rendered' or '#md' suffix on SOURCE is not used; instead,
#     the file is the most recent logged copy whose name matches the access path:
#     ACCESS_PATH 'rendered' picks the .rendered.txt copy, 'md' the .md copy, 'raw' the
#     curl copy. Default: md if the URL ends with .md, else rendered.
#   python3 -I cite.py check            re-verify every citation in work/cites.tsv
#   python3 -I cite.py find SOURCE TEXT [ACCESS_PATH]   print lines that contain TEXT
#
# The quote must occur verbatim in the file (exact substring). Tabs and newlines are
# not allowed in quotes. Quotes longer than 320 characters are refused.
import csv, os, sys, json

OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORK = os.path.join(OUT, "work")
FETCHED = os.path.join(OUT, "fetched")
CITES = os.path.join(WORK, "cites.tsv")
COLS = ["key", "source", "file", "locator", "quote", "source_date", "date_basis", "accessed", "access_path"]
OBS = "/home/user/observed-sh/"
SKM = "/home/user/sharrwah-knowledge-map/"
os.makedirs(WORK, exist_ok=True)

def read_log():
    rows = []
    with open(os.path.join(FETCHED, "log.tsv"), encoding="utf-8") as fh:
        next(fh)
        for line in fh:
            p = line.rstrip("\n").split("\t")
            if len(p) >= 5:
                rows.append(dict(url=p[0], file=p[1], status=p[2], fetched_at=p[3], sha=p[4]))
    return rows

def resolve(source, access_path=None):
    """Return (file_path, accessed, access_path)."""
    if source.startswith("observed-sh@b46731d0:"):
        return OBS + source.split(":", 1)[1], "2026-10-10", access_path or "local"
    if source.startswith("sharrwah-knowledge-map:"):
        return SKM + source.split(":", 1)[1], "2026-10-10", access_path or "local"
    if access_path is None:
        access_path = "md" if source.endswith(".md") else "rendered"
    cands = []
    for r in read_log():
        if r["url"] != source or not r["file"]:
            continue
        if not r["status"].startswith("2"):
            continue
        f = r["file"]
        if access_path == "rendered" and not f.endswith(".rendered.txt"):
            continue
        if access_path in ("md",) and not f.endswith(".md"):
            continue
        if access_path == "raw" and f.endswith(".rendered.txt"):
            continue
        cands.append(r)
    if not cands:
        raise SystemExit(f"no logged {access_path} copy for {source}")
    r = cands[-1]
    return os.path.join(FETCHED, r["file"]), r["fetched_at"][:10], access_path

def load():
    if not os.path.exists(CITES):
        return []
    with open(CITES, encoding="utf-8") as fh:
        rd = csv.DictReader(fh, delimiter="\t", quoting=csv.QUOTE_NONE)
        return list(rd)

def save_row(row):
    new = not os.path.exists(CITES)
    with open(CITES, "a", encoding="utf-8") as fh:
        if new:
            fh.write("\t".join(COLS) + "\n")
        fh.write("\t".join(row[c] for c in COLS) + "\n")

def text_of(path):
    return open(path, encoding="utf-8", errors="replace").read()

def cmd_add(args):
    key, source, locator, quote, sdate, dbasis = args[:6]
    ap = args[6] if len(args) > 6 else None
    for bad in ("\t", "\n"):
        if bad in quote or bad in locator:
            raise SystemExit("tab/newline in quote or locator")
    if len(quote) > 320:
        raise SystemExit(f"quote too long ({len(quote)})")
    existing = {r["key"]: r for r in load()}
    if key in existing:
        raise SystemExit(f"key exists: {key}")
    path, accessed, ap = resolve(source, ap)
    t = text_of(path)
    if quote not in t:
        raise SystemExit(f"QUOTE NOT FOUND in {path}: {quote[:120]}")
    row = dict(key=key, source=source, file=os.path.relpath(path, OUT) if path.startswith(OUT) else path,
               locator=locator, quote=quote, source_date=sdate, date_basis=dbasis,
               accessed=accessed, access_path=ap)
    save_row(row)
    print("ok", key)

def cmd_check(args):
    bad = 0
    rows = load()
    for r in rows:
        path = r["file"] if os.path.isabs(r["file"]) else os.path.join(OUT, r["file"])
        if r["quote"] not in text_of(path):
            bad += 1
            print("MISSING", r["key"], r["quote"][:80])
    print(f"{len(rows)} citations, {bad} missing")

def cmd_find(args):
    source, text = args[0], args[1]
    ap = args[2] if len(args) > 2 else None
    path, _, _ = resolve(source, ap)
    for i, line in enumerate(text_of(path).split("\n"), 1):
        if text in line:
            print(f"{i}: {line[:600]}")

def parse_blocks(path):
    blocks, cur = [], {}
    for line in open(path, encoding="utf-8"):
        line = line.rstrip("\n")
        if not line.strip():
            if cur:
                blocks.append(cur); cur = {}
            continue
        if line.startswith("#"):
            continue
        k, _, v = line.partition(": ")
        cur[k.strip()] = v
    if cur:
        blocks.append(cur)
    return blocks

def cmd_addfile(args):
    """Blocks of 'key/source/locator/quote/date/basis/access' lines, blank-line separated."""
    existing = {r["key"]: r for r in load()}
    added = skipped = errors = 0
    for b in parse_blocks(args[0]):
        try:
            key = b["key"]; source = b["source"]; locator = b["locator"]; quote = b["quote"]
            sdate = b["date"]; dbasis = b["basis"]; ap = b.get("access") or None
        except KeyError as e:
            print("BLOCK MISSING FIELD", e, b); errors += 1; continue
        if key in existing:
            if existing[key]["quote"] == quote and existing[key]["locator"] == locator:
                skipped += 1; continue
            print("KEY CONFLICT", key); errors += 1; continue
        if len(quote) > 320:
            print("TOO LONG", key, len(quote)); errors += 1; continue
        if "\t" in quote or "\t" in locator:
            print("TAB IN FIELD", key); errors += 1; continue
        try:
            path, accessed, ap2 = resolve(source, ap)
        except SystemExit as e:
            print("RESOLVE", key, e); errors += 1; continue
        if quote not in text_of(path):
            print("QUOTE NOT FOUND", key, "|", quote[:100]); errors += 1; continue
        row = dict(key=key, source=source, file=os.path.relpath(path, OUT) if path.startswith(OUT) else path,
                   locator=locator, quote=quote, source_date=sdate, date_basis=dbasis,
                   accessed=accessed, access_path=ap2)
        save_row(row); existing[key] = row; added += 1
    print(f"added {added}, already present {skipped}, errors {errors}")

if __name__ == "__main__":
    c, rest = sys.argv[1], sys.argv[2:]
    {"add": cmd_add, "check": cmd_check, "find": cmd_find, "addfile": cmd_addfile}[c](rest)
