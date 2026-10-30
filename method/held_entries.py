# The held pass's entries (Stage 4A; the brief studies/class-model/briefs/H-held.md): every entry of the platforms'
# self-descriptions that the class's model has not read, listed from the evidence repositories' structures, so that
# each is placed on the model by reading it, never found by search (the founder, 30 October).
#
# A structure is chosen in studies/class-model/held/selection.tsv (platform, structure, read, rule, reason). Its
# entries are the items of its items.jsonl files in every label (a store, a language), or its JSON files where it
# holds one file per item, each rendered from the fields the platform states (the capture's own keys for position,
# provenance and code are left out). Items that render the same are one entry, with every label it appears under.
# An item a citation of the concern map or of a landed subject already names (its file and line) is read already,
# and isn't listed. A rule narrows a structure: `new-vs:<structure>` keeps the items whose id the named structure
# lacks (a later version of a read one); `prefix:<text>` keeps the items whose rendering starts with it;
# `where:<key>=<value>` keeps the items whose field has that value.
#
# Usage:
#   python3 -I method/held_entries.py registers --platform P      every registered structure, held, cited and items
#   python3 -I method/held_entries.py build [--platform P]         writes studies/class-model/held/<platform>/entries.tsv
#   python3 -I method/held_entries.py show --platform P [--structure S] [--from N] [--to M] [--width W]
#   python3 -I method/held_entries.py batches [--size N]              cuts the entries into batches: held/batches.tsv
#   python3 -I method/held_entries.py check --platform P --batch B   checks held/<platform>/placements-<B>.tsv
import argparse, collections, csv, glob, json, os, re, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from class_slice import MODEL, PLATFORMS, PREFIX, rows
from held_vs_read import REPOS, read_sources

csv.field_size_limit(10**9)
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HELD = os.path.join(MODEL, "held")
SEL_HEAD = ["platform", "structure", "read", "rule", "reason"]
E_HEAD = ["entry_id", "structure", "labels", "source", "locator", "text"]
P_HEAD = ["entry_id", "placement", "cap_id", "supports", "reading"]
PLACEMENTS = ("capability", "new", "out")
SUPPORTS = ("core", "own-service", "extension-point", "outside", "shows")
# the capture's own keys: position, provenance, layout and code, never the platform's statement
SKIP = {"position", "array_offset", "line", "n", "record_id", "sha256", "bytes", "run_id", "index", "bounds", "clickable",
        "checked", "step", "class", "imports", "module", "hasAction", "hasLoader", "hasClientAction", "hasClientLoader",
        "hasClientMiddleware", "hasDefaultExport", "hasErrorBoundary", "component", "loader", "file", "version", "keys",
        "path_source", "sliceId", "html", "__typename", "location_status", "location_record_id", "resolved_from",
        "pointer", "depth", "indent", "headings", "item", "source", "icon", "logo", "thumbnail", "image", "color", "focused",
        "selected", "scrollable", "enabled_ui", "package", "resource-id", "content-desc", "bounds_px", "parent", "within",
        "container", "app", "condition"}
LONG = 220
# an identifier that says nothing: a uuid, a global or base64 id, a hash, an Android resource id
OPAQUE = re.compile(r"^([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}|gid://.*|[A-Za-z0-9+/=_-]{24,}|[0-9a-f]{8,}|\d+|.*:id/.*|android:.*)$")
WORDS = ("text", "title", "name", "label", "desc", "description", "section", "group", "key", "handle", "path", "slug",
         "pageKey", "value", "option", "page", "href", "url", "link", "category", "type", "event", "summary",
         "heading", "title_en", "title_ar", "address", "store_country", "bundles", "feature", "features", "plan", "parentId")


def git(root, *a):
    p = subprocess.run(["git", "-C", root, *a], capture_output=True, text=True)
    return p.stdout.strip() if p.returncode == 0 else ""


def clip(s, n=LONG):
    s = " ".join(str(s).split())
    return s if len(s) <= n else s[: n - 1] + "…"


def render(o, depth=0):
    """An item as the platform states it: its fields, in the source's order, without the capture's own keys."""
    if not isinstance(o, dict):
        return clip(json.dumps(o, ensure_ascii=False))
    parts = []
    for k, v in o.items():
        if k in SKIP:
            continue
        if isinstance(v, str):
            v = v.strip()
            if v and not (k in ("id", "gid", "uuid", "resource_id") and OPAQUE.search(v)):
                parts.append(f"{k}: {clip(v, 160)}")
        elif isinstance(v, bool):
            parts.append(f"{k}: {'true' if v else 'false'}")
        elif isinstance(v, (int, float)) and k not in ("id", "order", "sort", "priority"):
            parts.append(f"{k}: {v}")
        elif isinstance(v, dict) and depth < 2:
            inner = render(v, depth + 1)
            if inner:
                parts.append(f"{k}: {{{inner}}}")
        elif isinstance(v, list) and v:
            if all(isinstance(x, str) for x in v):
                parts.append(f"{k}: [{clip(', '.join(v), 160)}]")
            elif all(isinstance(x, dict) for x in v) and depth < 1:
                inner = " | ".join(render(x, depth + 1) for x in v[:12])
                parts.append(f"{k}: [{clip(inner, 300)}{' …' if len(v) > 12 else ''}]")
            else:
                parts.append(f"{k}: {len(v)} items")
    return clip("; ".join(parts), 600)


def selection():
    path = os.path.join(HELD, "selection.tsv")
    return rows(path) if os.path.exists(path) else []


def folder(platform, structure):
    repo, root, sub = REPOS[platform]
    return os.path.join(root, sub, "structures", structure) if sub else os.path.join(root, "structures", platform, structure)


def cited_lines(platform):
    """(file path relative to its repository, line) pairs what the model reads cites."""
    repo, root, sub = REPOS[platform]
    out = set()
    for s, loc in read_sources()[platform]:
        m = re.match(rf"^{repo}@[0-9a-f]+:(.+)$", s)
        if not m:
            continue
        f = re.sub(r"[#:]L?\d+(-L?\d+)?$", "", m.group(1))
        ln = re.search(r"\bline (\d+)", loc or "") or re.search(r"[#:]L(\d+)", m.group(1))
        out.add((f, int(ln.group(1)) if ln else 0))
    return out


def item_id(o):
    for k in ("id", "key", "slug", "handle", "pageKey", "name", "path", "url"):
        if isinstance(o, dict) and o.get(k) not in (None, ""):
            return f"{k}={o[k]}"
    return None


def items_of(platform, structure, rule=""):
    """Every item of a structure: (label, file relative to the repository, line or 0, item). A structure held as a
    table in a run (rule `rows:<path from the repository>:<pattern on the first column>`) gives one item per row."""
    repo, root, sub = REPOS[platform]
    base = folder(platform, structure)
    out = []
    m = re.match(r"^rows:([^:]+):(.+)$", rule or "")
    if m:
        f = os.path.join(root, m.group(1))
        for i, r in enumerate(csv.reader(open(f, encoding="utf-8", errors="replace"), delimiter="\t", quoting=csv.QUOTE_NONE), 1):
            if i == 1 or not r or not re.match(m.group(2), r[0]):
                continue
            out.append((".", m.group(1), i, {"option": r[0], "value": clip(r[-1], 160)}))
        return out
    files = sorted(glob.glob(os.path.join(base, "**", "items.jsonl"), recursive=True))
    if files:
        for f in files:
            label = os.path.relpath(os.path.dirname(f), base)
            for i, l in enumerate(open(f, encoding="utf-8", errors="replace"), 1):
                try:
                    out.append((label, os.path.relpath(f, root), i, json.loads(l)))
                except Exception:
                    continue
        return out
    for f in sorted(glob.glob(os.path.join(base, "**", "*.json"), recursive=True)):
        if os.path.basename(f) in ("meta.json",):
            continue
        try:
            o = json.load(open(f, encoding="utf-8"))
        except Exception:
            continue
        label = os.path.relpath(os.path.dirname(f), base)
        name = os.path.splitext(os.path.basename(f))[0].replace("~", " > ")
        head = {"file": name}
        if isinstance(o, dict):
            for k in ("title", "name", "label", "description", "type"):
                if isinstance(o.get(k), (str, dict)):
                    head[k] = o[k]
            d = o.get("data") if isinstance(o.get("data"), dict) else None
            if d:
                for k in ("title", "name", "label", "description"):
                    if isinstance(d.get(k), (str, dict)) and k not in head:
                        head[k] = d[k]
        out.append((label, os.path.relpath(f, root), 0, {"page": name, **{k: v for k, v in head.items() if k != "file"}}))
    return out


def cmd_registers(a):
    from held_vs_read import structures
    for s in structures(a.platform, read_sources()[a.platform]):
        print(f"{s['structure']}\theld {int(s['held'])}\tread {int(s['read'])}\titems {s['items']}\tcited {s['items_read']}\t{s['date_seen']}\t{s['what'][:120]}")


def cmd_build(a):
    sel = [r for r in selection() if r["read"] == "yes" and (not a.platform or r["platform"] == a.platform)]
    by_p = collections.defaultdict(list)
    for r in sel:
        by_p[r["platform"]].append(r)
    for p, rs in by_p.items():
        repo, root, sub = REPOS[p]
        commit = git(root, "rev-parse", "--short=9", "HEAD")
        cited = cited_lines(p)
        out, n = [], 0
        for r in rs:
            its = items_of(p, r["structure"], r.get("rule", ""))
            if not its:
                print(f"{p} {r['structure']}: no items found under {folder(p, r['structure'])}")
            rule = r.get("rule", "").strip()
            if rule.startswith("new-vs:"):
                old = {item_id(o) for _, _, _, o in items_of(p, rule[7:])}
                its = [x for x in its if item_id(x[3]) not in old]
            m = re.match(r"^where:([^=]+)=(.+)$", rule)
            if m:
                its = [x for x in its if isinstance(x[3], dict) and str(x[3].get(m.group(1), "")) == m.group(2)]
            groups = collections.OrderedDict()
            for label, f, ln, o in its:
                t = render(o)
                if rule.startswith("prefix:") and not t.startswith(rule[7:]):
                    continue
                g = groups.setdefault(t.casefold(), {"text": t, "labels": [], "at": None, "read": False})
                if label not in g["labels"]:
                    g["labels"].append(label)
                if (f, ln) in cited:
                    g["read"] = True
                if g["at"] is None:
                    g["at"] = (f, ln)
            for g in groups.values():
                # an item that renders to no word of the platform's (layout nodes, bare ids) says nothing to place
                if g["read"] or not g["text"] or not any(g["text"].startswith(w + ":") or f"; {w}:" in g["text"] for w in WORDS):
                    continue
                n += 1
                f, ln = g["at"]
                out.append([f"{PREFIX[p]}-E-{n:05d}", r["structure"], ",".join(g["labels"]), f"{repo}@{commit}:{f}",
                            f"line {ln}" if ln else "", g["text"]])
        os.makedirs(os.path.join(HELD, p), exist_ok=True)
        with open(os.path.join(HELD, p, "entries.tsv"), "w", encoding="utf-8") as fh:
            fh.write("\t".join(E_HEAD) + "\n")
            for l in out:
                fh.write("\t".join(x.replace("\t", " ").replace("\n", " ") for x in l) + "\n")
        c = collections.Counter(l[1] for l in out)
        print(f"{p}: {len(out)} entries from {len(rs)} structures at {repo}@{commit}: " + ", ".join(f"{k} {v}" for k, v in c.items()))


def entries(p):
    path = os.path.join(HELD, p, "entries.tsv")
    return rows(path) if os.path.exists(path) else []


def cmd_show(a):
    es = entries(a.platform)
    if a.structure:
        es = [e for e in es if e["structure"] == a.structure]
    lo = a.__dict__.get("from") or 1
    for e in es:
        n = int(e["entry_id"].rsplit("-", 1)[1])
        if n < lo or (a.to and n > a.to):
            continue
        print(f"{e['entry_id']} [{e['structure']}{' @' + e['labels'] if e['labels'] and e['labels'] != '.' else ''}] {clip(e['text'], a.width)}")


def batch_range(platform, batch):
    for r in rows(os.path.join(HELD, "batches.tsv")):
        if r["batch"] == batch and r["platform"] == platform:
            return int(r["from"]), int(r["to"])
    sys.exit(f"no batch {batch} for {platform} in held/batches.tsv")


def cmd_batches(a):
    """Cuts each platform's entries into batches of at most --size, at a structure's end where one falls near."""
    out = []
    for p in PLATFORMS:
        es = entries(p)
        if not es:
            continue
        n, start, k = 0, None, 0
        for i, e in enumerate(es):
            num = int(e["entry_id"].rsplit("-", 1)[1])
            if start is None:
                start, n = num, 0
            n += 1
            last = i == len(es) - 1
            boundary = last or es[i + 1]["structure"] != e["structure"]
            if last or n >= a.size or (boundary and n >= a.size * 0.6):
                k += 1
                structs = list(dict.fromkeys(x["structure"] for x in es if start <= int(x["entry_id"].rsplit("-", 1)[1]) <= num))
                out.append([f"{PREFIX[p]}-{k}", p, str(start), str(num), str(n), ",".join(structs)])
                start = None
    with open(os.path.join(HELD, "batches.tsv"), "w", encoding="utf-8") as fh:
        fh.write("batch\tplatform\tfrom\tto\tentries\tstructures\n")
        for l in out:
            fh.write("\t".join(l) + "\n")
            print("\t".join(l)[:200])


def cmd_check(a):
    problems = []
    lo, hi = batch_range(a.platform, a.batch)
    es = {e["entry_id"]: e for e in entries(a.platform) if lo <= int(e["entry_id"].rsplit("-", 1)[1]) <= hi}
    caps = {r["cap_id"] for r in rows(os.path.join(MODEL, "merged", "capabilities.tsv"))}
    path = os.path.join(HELD, a.platform, f"placements-{a.batch}.tsv")
    if not os.path.exists(path):
        sys.exit(f"no {os.path.relpath(path, ROOT)}")
    raw = open(path, encoding="utf-8").read().split("\n")
    if raw[0].split("\t") != P_HEAD:
        problems.append(f"placements-{a.batch}.tsv: header must be: {' '.join(P_HEAD)}")
    seen = set()
    for i, l in enumerate(raw[1:], 2):
        if not l.strip():
            continue
        f = l.split("\t")
        w = f"placements-{a.batch}.tsv line {i}"
        if len(f) != len(P_HEAD):
            problems.append(f"{w}: {len(P_HEAD)} tab-separated fields (it has {len(f)})"); continue
        r = dict(zip(P_HEAD, f))
        ids = [x.strip() for x in r["entry_id"].split(";") if x.strip()]
        for x in ids:
            if x not in es:
                problems.append(f"{w}: {x} is not an entry of batch {a.batch} (held/batches.tsv)")
            if x in seen:
                problems.append(f"{w}: {x} placed again")
            seen.add(x)
        if r["placement"] not in PLACEMENTS:
            problems.append(f"{w}: placement is one of {', '.join(PLACEMENTS)}")
        if r["placement"] == "capability":
            cs = [c.strip() for c in r["cap_id"].split(";") if c.strip()]
            if not cs or any(c not in caps for c in cs):
                problems.append(f"{w}: capability names cap_ids of the merged model, `;`-separated")
            ss = [s.strip() for s in r["supports"].split(";") if s.strip()]
            if not ss or any(s not in SUPPORTS for s in ss):
                problems.append(f"{w}: supports is one or more of {', '.join(SUPPORTS)}, `;`-separated")
        if r["placement"] == "new":
            if not re.match(r"^new:\S", r["cap_id"]):
                problems.append(f"{w}: a new capability is named in cap_id as new:<its name, in the platform's words>")
            if r["supports"] and any(s.strip() not in SUPPORTS for s in r["supports"].split(";")):
                problems.append(f"{w}: supports is one or more of {', '.join(SUPPORTS)}")
        if r["placement"] == "out" and (r["cap_id"] or r["supports"]):
            problems.append(f"{w}: out of scope names no capability and supports nothing")
        if not r["reading"].strip():
            problems.append(f"{w}: reading says why, as a reading")
    for x in sorted(set(es) - seen):
        problems.append(f"{x} has no placement")
    for p in problems[:200]:
        print("PROBLEM", p)
    if len(problems) > 200:
        print(f"... and {len(problems) - 200} more")
    print(f"{len(seen & set(es))} of {len(es)} entries placed; {len(problems)} problems")
    sys.exit(1 if problems else 0)


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("registers"); s.add_argument("--platform", choices=PLATFORMS, required=True); s.set_defaults(f=cmd_registers)
    s = sub.add_parser("build"); s.add_argument("--platform", choices=PLATFORMS); s.set_defaults(f=cmd_build)
    s = sub.add_parser("show"); s.add_argument("--platform", choices=PLATFORMS, required=True)
    s.add_argument("--structure"); s.add_argument("--from", type=int); s.add_argument("--to", type=int)
    s.add_argument("--width", type=int, default=400); s.set_defaults(f=cmd_show)
    s = sub.add_parser("check"); s.add_argument("--platform", choices=PLATFORMS, required=True)
    s.add_argument("--batch", required=True); s.set_defaults(f=cmd_check)
    s = sub.add_parser("batches"); s.add_argument("--size", type=int, default=900); s.set_defaults(f=cmd_batches)
    a = ap.parse_args()
    a.f(a)


if __name__ == "__main__":
    main()
