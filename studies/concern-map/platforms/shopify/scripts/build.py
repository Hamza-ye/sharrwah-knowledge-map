# Build the deliverable TSVs from the work files.
#   work/inventory_raw.tsv      (build_inventory.py)
#   scripts/concerns_def.py     (concern catalogue)
#   scripts/mapping_def.py      (inventory -> concerns)
#   work/cites.tsv              (registered citations, verified by cite.py)
#   work/placements/*.txt       (placement blocks)
# Writes inventory.tsv, concerns.tsv, placements.tsv, citations.tsv in the output directory.
# Run: python3 -I build.py
import csv, glob, os, re, sys, collections

D = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.dirname(D)
ns = {}; exec(open(os.path.join(D, "concerns_def.py")).read(), ns)
ms = {}; exec(open(os.path.join(D, "mapping_def.py")).read(), ms)
CONCERNS = ns["C"]
PLACEMENTS = ["software", "decides", "legal", "boundary", "reason"]

def clean(v):
    return str(v).replace("\t", " ").replace("\r", " ").replace("\n", " ").strip()

def read_tsv(p):
    return list(csv.DictReader(open(p, encoding="utf-8"), delimiter="\t", quoting=csv.QUOTE_NONE))

# ---------------- citations: registered first, inventory after
cites = read_tsv(os.path.join(OUT, "work", "cites.tsv"))
cite_id = {}
cit_rows = []
n = 0
for r in cites:
    n += 1
    cid = f"SH-S-{n:04d}"
    cite_id[r["key"]] = cid
    cit_rows.append(dict(cite_id=cid, source=r["source"], locator=r["locator"], quote=r["quote"],
                         source_date=r["source_date"], date_basis=r["date_basis"], accessed=r["accessed"],
                         access_path=r["access_path"], _file=r["file"]))

inv = read_tsv(os.path.join(OUT, "work", "inventory_raw.tsv"))
key_to_cid = {c["key"]: f"SH-C-{i:03d}" for i, c in enumerate(CONCERNS, 1)}
inv_rows = []
inv_by_concern = collections.defaultdict(list)
inv_ref = collections.defaultdict(list)  # (list, entry) -> [(group, cite_id, inv_id)]
for i, r in enumerate(inv, 1):
    n += 1
    cid = f"SH-S-{n:04d}"
    iid = f"SH-I-{i:04d}"
    cit_rows.append(dict(cite_id=cid, source=r["source"], locator=r["locator"], quote=r["quote"],
                         source_date=r["source_date"], date_basis=r["date_basis"],
                         accessed="2026-10-10", access_path=r["access_path"], _file=r["file"]))
    ks, reason = ms["map_row"](r["list"], r["entry"], r["group"], r["extra"])
    ids = sorted(key_to_cid[k] for k in ks)
    for k in ks:
        inv_by_concern[k].append(iid)
    if not ids and not reason:
        sys.exit(f"unmapped inventory row: {r['list']} | {r['entry']}")
    inv_rows.append(dict(inv_id=iid, list=r["list"], entry=r["entry"], cite_id=cid,
                         concern_ids=";".join(ids), out_of_scope_reason="" if ids else reason, _group=r["group"]))
    inv_ref[(r["list"], r["entry"])].append((r["group"], cid, iid))

def resolve_cite(ref, where):
    ref = ref.strip().replace("%2C", ",")  # a comma inside an inventory entry is written %2C
    if ref.startswith("inv:"):
        parts = ref[4:].split("|")
        lst, entry = parts[0], parts[1]
        grp = parts[2] if len(parts) > 2 else None
        cands = inv_ref.get((lst, entry), [])
        if grp:
            cands = [c for c in cands if grp in c[0]]
        if not cands:
            sys.exit(f"{where}: inventory reference not found: {ref}")
        return cands[0][1]
    if ref not in cite_id:
        sys.exit(f"{where}: citation key not registered: {ref}")
    return cite_id[ref]

# ---------------- placements
pl_rows = []
seen = collections.defaultdict(set)
for path in sorted(glob.glob(os.path.join(OUT, "work", "placements", "*.txt"))):
    cur = None
    for ln, line in enumerate(open(path, encoding="utf-8"), 1):
        line = line.rstrip("\n")
        if not line.strip() or line.startswith("#"):
            continue
        where = f"{os.path.basename(path)}:{ln}"
        m = re.match(r"^concern: (\S+)$", line)
        if m:
            cur = m.group(1)
            if cur not in key_to_cid:
                sys.exit(f"{where}: unknown concern {cur}")
            continue
        m = re.match(r"^(software|decides|legal|boundary|reason): (.*)$", line)
        if not m:
            sys.exit(f"{where}: cannot parse: {line[:80]}")
        pl, rest = m.group(1), m.group(2)
        parts = [p.strip() for p in rest.split(" || ")]
        value = parts[0]
        cites_ = []; note = ""
        for p in parts[1:]:
            if p.startswith("cites: "):
                cites_ = [resolve_cite(x, where) for x in p[7:].split(",") if x.strip()]
            elif p.startswith("note: "):
                note = p[6:]
            else:
                sys.exit(f"{where}: unknown part: {p[:60]}")
        # citation keys mentioned inside parentheses in a note are written as their SH-S ids
        note = re.sub(r"\(([a-z0-9_]+(?:, [a-z0-9_]+)*)\)",
                      lambda m: "(" + ", ".join(cite_id.get(k, k) for k in m.group(1).split(", ")) + ")", note)
        status = "not shown" if value == "not shown" else "shown"
        if status == "shown" and not cites_:
            sys.exit(f"{where}: shown placement without citation")
        if status == "not shown" and cites_:
            sys.exit(f"{where}: 'not shown' placement carries citations; put sources that do not settle it in the note only")
        if note and re.search(r"\binfer", note, re.I) and not note.startswith("Inference:") and "Inference:" not in note:
            sys.exit(f"{where}: inference must be labelled 'Inference:'")
        seen[cur].add(pl)
        pl_rows.append(dict(concern_id=key_to_cid[cur], placement=pl, value=value, status=status,
                            cite_ids=";".join(dict.fromkeys(cites_)), note=note, _key=cur))

# every concern gets every placement; missing ones are written as not shown
missing = 0
for c in CONCERNS:
    for pl in PLACEMENTS:
        if pl not in seen[c["key"]]:
            missing += 1
            pl_rows.append(dict(concern_id=key_to_cid[c["key"]], placement=pl, value="not shown", status="not shown",
                                cite_ids="", note="", _key=c["key"]))
order = {c["key"]: i for i, c in enumerate(CONCERNS)}
pl_rows.sort(key=lambda r: (order[r["_key"]], PLACEMENTS.index(r["placement"])))

# ---------------- write
def write(name, cols, rows):
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as fh:
        fh.write("\t".join(cols) + "\n")
        for r in rows:
            fh.write("\t".join(clean(r.get(c, "")) for c in cols) + "\n")

write("inventory.tsv", ["inv_id", "list", "entry", "cite_id", "concern_ids", "out_of_scope_reason"], inv_rows)
crow = []
for c in CONCERNS:
    crow.append(dict(concern_id=key_to_cid[c["key"]], concern=c["name"], platform_terms=c["terms"],
                     inv_ids=";".join(inv_by_concern[c["key"]]), split_note=c["split"]))
write("concerns.tsv", ["concern_id", "concern", "platform_terms", "inv_ids", "split_note"], crow)
write("placements.tsv", ["concern_id", "placement", "value", "status", "cite_ids", "note"], pl_rows)
write("citations.tsv", ["cite_id", "source", "locator", "quote", "source_date", "date_basis", "accessed", "access_path"], cit_rows)

# ---------------- checks
bad = 0
cache = {}
for r in cit_rows:
    f = r["_file"] if os.path.isabs(r["_file"]) else os.path.join(OUT, r["_file"])
    if f not in cache:
        cache[f] = open(f, encoding="utf-8", errors="replace").read()
    if r["quote"] not in cache[f]:
        bad += 1; print("QUOTE MISSING", r["cite_id"], r["quote"][:60])
st = collections.Counter(r["status"] for r in pl_rows)
print(f"inventory {len(inv_rows)} (out of scope {sum(1 for r in inv_rows if not r['concern_ids'])}); concerns {len(crow)}; "
      f"placements {len(pl_rows)} {dict(st)} (defaulted not shown: {missing}); citations {len(cit_rows)}; quotes missing {bad}")
