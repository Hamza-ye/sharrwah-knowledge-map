# The held pass's entries (Stage 4A; the brief studies/class-model/briefs/H-held.md): every entry of the platforms'
# self-descriptions that the class's model has not read, listed from the evidence repositories, so that each is placed
# on the model by reading it, never found by search (the founder, 30 October). Rebuilt after its inspection
# (studies/class-model/inspection-H.md).
#
# A structure is chosen in studies/class-model/held/selection.tsv: platform, structure, read (yes, or no with its
# reason), rule, placement, note, reason. Its items are the lines of its items.jsonl files in every label (a store, a
# language), or what its rule reads instead. Each item is rendered from the fields the platform states: the capture's
# own keys (position, provenance, layout, code) are left out, and nothing is clipped. Items that render the same are
# one entry, with every label it appears under. An item that a citation of what the model reads names (its file and
# line, holding the same text at the head as at the cited commit) is read already, and isn't listed.
#
# An entry's id is stable: <PREFIX>-E-<8 hex>, from its structure and its rendering, so a rebuild keeps every id
# whose text is unchanged. `build` refuses to drop an id that a placements file names.
#
# Rules, `;`-separated, applied in this order (studies/class-model/briefs/H-held.md names them):
#   rows:<path from the repository's root>:<pattern>   a table's rows (tab-separated, with a header), the first column
#                                                      matching the pattern
#   text:                     one item per non-empty line of each text.txt of the structure
#   json:<glob>               the JSON files the glob names (from the repository's root), each one item; json1: the
#                             last of them only
#   changes:<path>            a route manifest's changes, before and after, from the repository's derived file
#   dict:<key>                one item per key of the dict at <key>, with its value
#   nested:<k1>,<k2>          one item per element of each list so named, at any depth, carrying its ancestors' names
#   new-vs:<structure>        the items whose name the named structure lacks
#   where:<key>=<v1>|<v2>     the items whose field has one of the values; where:<key>!= keeps those where it is set
#   labels:<pattern>          the items of the labels that match
#   drop:<k1>,<k2>            leaves those fields out of the rendering
#   drop-match:<pattern>      drops the items whose rendering matches
#   translate:<en>,<ar>       resolves values that are keys of those translation files (paths from the structures folder)
#
# Usage:
#   python3 -I method/held_entries.py registers --platform P       every registered structure: held, cited, items
#   python3 -I method/held_entries.py build [--platform P]          writes held/<platform>/entries.tsv, reports per structure
#   python3 -I method/held_entries.py batches [--size N]            cuts the entries no batch holds into batches
#   python3 -I method/held_entries.py show --platform P (--batch B | --structure S) [--from I] [--to J] [--width W] [--meta]
#                                                [--candidates]   each entry's leads, by identifier or by term: leads only
#   python3 -I method/held_entries.py check --platform P --batch B  checks held/<platform>/placements-<B>.tsv
import argparse, collections, csv, glob, hashlib, json, os, re, subprocess, sys, unicodedata
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from class_slice import MODEL, PLATFORMS, PREFIX, rows
from held_vs_read import REPOS, read_sources

csv.field_size_limit(10**9)
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HELD = os.path.join(MODEL, "held")
SEL_HEAD = ["platform", "structure", "read", "rule", "placement", "note", "reason"]
E_HEAD = ["entry_id", "structure", "labels", "source", "locator", "section", "text"]
P_HEAD = ["entry_id", "placement", "cap_id", "supports", "scope", "terms", "filler", "quality", "reading"]
PLACEMENTS = ("capability", "new", "out")
SUPPORTS = ("core", "own-service", "extension-point", "outside", "shows")
MAX_TEXT = 3000          # an entry longer than this holds a list of things: its structure needs a nested: rule
# the capture's own keys (position, provenance, layout, code), never a statement of the platform's
SKIP = {"position", "array_offset", "line", "n", "record_id", "sha256", "bytes", "run_id", "bounds", "clickable",
        "checked", "step", "imports", "module", "hasAction", "hasLoader", "hasClientAction", "hasClientLoader",
        "hasClientMiddleware", "hasDefaultExport", "hasErrorBoundary", "component", "loader", "file", "version", "keys",
        "path_source", "sliceId", "html", "__typename", "location_status", "location_record_id", "resolved_from",
        "pointer", "depth", "indent", "icon", "iconUrl", "logo", "thumbnail", "image", "color", "focused", "selected",
        "scrollable", "package", "resource-id", "bounds_px", "condition", "css", "titleLoader", "array", "expr"}
LAYOUT = {"role", "kind", "tag", "type", "class", "id", "parent", "label_key", "set"}   # a rendering of these alone says nothing
# an identifier that says nothing: a UUID, a global id, a hex hash, a base64 string, an Android resource id
OPAQUE = re.compile(r"^([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}|gid://\S+|[0-9a-f]{8,}|"
                    r"(?=[A-Za-z0-9+/]*\d)(?=[A-Za-z0-9+/]*[A-Z])[A-Za-z0-9+/]{24,}={0,2}|\S*:id/\S*|android:\S+)$")
SECTION_KEYS = ("section", "group", "page", "category", "app", "segment", "within", "list", "pageKey", "parentId")


def git(root, *a):
    p = subprocess.run(["git", "-C", root, *a], capture_output=True, text=True)
    return p.stdout if p.returncode == 0 else ""


def clip(s, n):
    s = " ".join(str(s).split())
    return s if len(s) <= n else s[: n - 1] + "…"


def fold(s):
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[\s_-]+", " ", s.casefold()).strip()


def render(o, drop=(), tr=None, depth=0):
    """An item as the platform states it: its fields, in the source's order, without the capture's own keys."""
    if not isinstance(o, dict):
        return " ".join(str(o).split())
    parts = []
    for k, v in o.items():
        if k in SKIP or k in drop:
            continue
        if isinstance(v, str):
            v = " ".join(v.split())
            if not v or (k in ("id", "gid", "uuid", "resource_id", "objectID") and OPAQUE.search(v)):
                continue
            if tr and v in tr:
                v = f"{tr[v][0]}" + (f" ({tr[v][1]})" if tr[v][1] else "") + f" [{v}]"
            parts.append(f"{k}: {v}")
        elif isinstance(v, bool):
            parts.append(f"{k}: {'true' if v else 'false'}")
        elif isinstance(v, (int, float)):
            if k in ("id", "order", "sort", "priority", "index", "source") and depth == 0:
                continue
            parts.append(f"{k}: {v}")
        elif isinstance(v, dict) and v:
            inner = render(v, drop, tr, depth + 1)
            if inner:
                parts.append(f"{k}: {{{inner}}}")
        elif isinstance(v, list) and v:
            if all(isinstance(x, (str, int, float)) for x in v):
                parts.append(f"{k}: [{', '.join(str(x) for x in v)}]")
            else:
                inner = " | ".join(x for x in (render(x, drop, tr, depth + 1) for x in v) if x)
                if inner:
                    parts.append(f"{k}: [{inner}]")
    return "; ".join(parts)


def says_something(o):
    return isinstance(o, dict) and any(k not in SKIP and k not in LAYOUT and v not in (None, "", [], {}) for k, v in o.items())


def name_of(o):
    if isinstance(o, dict):
        for k in ("name", "title", "label", "key", "slug", "handle", "id", "path", "url"):
            v = o.get(k)
            if isinstance(v, dict):
                v = v.get("en") or next(iter(v.values()), "")
            if isinstance(v, str) and v.strip():
                return v.strip()
    return ""


def flatten(o, keys, trail=()):
    """One item per element of each list named in keys, at any depth, carrying its ancestors' names."""
    out = []
    if isinstance(o, dict):
        here = trail + ((name_of(o),) if name_of(o) else ())
        for k, v in o.items():
            if k in keys and isinstance(v, list):
                for i, x in enumerate(v):
                    if isinstance(x, dict):
                        out.append(({"within": " > ".join(here), "list": k, **{kk: vv for kk, vv in x.items() if kk not in keys}}, f"/{k}/{i}"))
                        out += [(it, f"/{k}/{i}{p}") for it, p in flatten(x, keys, here + ((name_of(x),) if name_of(x) else ()))]
                    else:
                        out.append(({"within": " > ".join(here), "list": k, "value": x}, f"/{k}/{i}"))
            elif isinstance(v, (dict, list)):
                out += [(it, f"/{k}{p}") for it, p in flatten(v, keys, here)]
    elif isinstance(o, list):
        for i, x in enumerate(o):
            out += [(it, f"/{i}{p}") for it, p in flatten(x, keys, trail)]
    return out


def selection():
    path = os.path.join(HELD, "selection.tsv")
    return rows(path) if os.path.exists(path) else []


RULE = re.compile(r";(?=\s*(?:rows|text|json1?|changes|dict|nested|new-vs|where|labels|drop|drop-match|translate|release):)")


def rules(r):
    """A selection row's rules, `;`-separated: a `;` inside a rule's pattern stays in it."""
    out = []
    for x in RULE.split(r.get("rule") or ""):
        x = x.strip()
        if x:
            k, _, v = x.partition(":")
            out.append((k, v))
    return out


def folder(platform, structure):
    repo, root, sub = REPOS[platform]
    return os.path.join(root, sub, "structures", structure) if sub else os.path.join(root, "structures", platform, structure)


def items_of(platform, structure, rs):
    """Every item of a structure, after its reading rules: (label, file from the repository's root, line or 0,
    a JSON pointer or "", the item)."""
    repo, root, sub = REPOS[platform]
    base = folder(platform, structure)
    rd = dict(rs)
    out = []
    if "release" in rd:
        return release_items(rd["release"])
    if "rows" in rd:
        path, pat = rd["rows"].split(":", 1)
        f = os.path.join(root, path)
        rdr = csv.reader(open(f, encoding="utf-8", errors="replace"), delimiter="\t", quoting=csv.QUOTE_NONE)
        head = None
        for i, r in enumerate(rdr, 1):
            if head is None:
                head = r
                continue
            if r and re.match(pat, r[0]):
                out.append((".", path, i, "", dict(zip(head, (clip(x, 400) for x in r)))))
        return out
    if "text" in rd:
        for f in sorted(glob.glob(os.path.join(base, "**", "text.txt"), recursive=True)):
            label = os.path.relpath(os.path.dirname(f), base)
            for i, l in enumerate(open(f, encoding="utf-8", errors="replace"), 1):
                if l.strip():
                    out.append((label, os.path.relpath(f, root), i, "", {"text": l.strip()}))
        return out
    if "json" in rd or "json1" in rd:
        fs = sorted(glob.glob(os.path.join(root, rd.get("json") or rd.get("json1")), recursive=True))
        if "json1" in rd:
            fs = fs[-1:]
        for f in fs:
            try:
                o = json.load(open(f, encoding="utf-8"))
            except Exception:
                continue
            out.append((os.path.basename(os.path.dirname(f)), os.path.relpath(f, root), 0, "", o))
    elif "changes" in rd:
        f = os.path.join(root, rd["changes"])
        for i, l in enumerate(open(f, encoding="utf-8", errors="replace"), 1):
            try:
                o = json.loads(l)
            except Exception:
                continue
            def elig(x):
                return [e.get("eligibility") for e in ((x or {}).get("eligibilityMatch") or []) if isinstance(e, dict)] if isinstance(x, dict) else []
            out.append((".", os.path.relpath(f, root), i, "", {"id": o.get("id"), "change": o.get("change"), "keys": o.get("keys"),
                        "eligibility before": json.dumps(elig(o.get("before")), ensure_ascii=False),
                        "eligibility after": json.dumps(elig(o.get("after")), ensure_ascii=False)}))
    else:
        files = sorted(glob.glob(os.path.join(base, "**", "items.jsonl"), recursive=True))
        for f in files:
            label = os.path.relpath(os.path.dirname(f), base)
            for i, l in enumerate(open(f, encoding="utf-8", errors="replace"), 1):
                try:
                    out.append((label, os.path.relpath(f, root), i, "", json.loads(l)))
                except Exception:
                    continue
        if not files:
            for f in sorted(glob.glob(os.path.join(base, "**", "*.json"), recursive=True)):
                if os.path.basename(f) == "meta.json":
                    continue
                try:
                    o = json.load(open(f, encoding="utf-8"))
                except Exception:
                    continue
                d = o.get("data") if isinstance(o, dict) and isinstance(o.get("data"), dict) else o
                out.append((os.path.relpath(os.path.dirname(f), base), os.path.relpath(f, root), 0, "",
                            {"page": os.path.splitext(os.path.basename(f))[0].replace("~", " > "), **(d if isinstance(d, dict) else {"value": d})}))
    if "dict" in rd:
        nxt = []
        for label, f, ln, ptr, o in out:
            d = o
            for k in rd["dict"].split("."):
                d = d.get(k, {}) if isinstance(d, dict) else {}
            for k, v in (d.items() if isinstance(d, dict) else []):
                nxt.append((label, f, ln, f"{ptr}/{rd['dict'].replace('.', '/')}/{k}", {"key": k, "value": v}))
        out = nxt
    if "nested" in rd:
        keys = set(rd["nested"].split(","))
        nxt = []
        for label, f, ln, ptr, o in out:
            fl = flatten(o, keys)
            nxt += [(label, f, ln, ptr + p, it) for it, p in fl] if fl else [(label, f, ln, ptr, o)]
        out = nxt
    if "new-vs" in rd:
        old = {name_of(o) for _, _, _, _, o in items_of(platform, rd["new-vs"], [])}
        out = [x for x in out if name_of(x[4]) not in old]
    if "where" in rd:
        k, op, vals = re.match(r"^([^=!]+)(!?=)(.*)$", rd["where"]).groups()
        if op == "!=":
            out = [x for x in out if isinstance(x[4], dict) and x[4].get(k) not in (None, "")]
        else:
            vs = set(vals.split("|"))
            out = [x for x in out if isinstance(x[4], dict) and str(x[4].get(k, "")) in vs]
    if "labels" in rd:
        out = [x for x in out if re.search(rd["labels"], x[0])]
    return out


RELEASE = "/home/user/woocommerce-release/11.2.1/woocommerce"   # evidence/product-class/woocommerce-11.2.1/ fixes it


def release_items(kind):
    """WooCommerce's own lists in its release, read from the PHP that declares them, each item at its file and line
    (cited as woocommerce-11.2.1:<path>, as the concern map cites the release)."""
    out = []
    def lines(rel):
        return open(os.path.join(RELEASE, rel), encoding="utf-8", errors="replace").read().split("\n")
    def tr(x):
        m = re.search(r"__\(\s*'((?:[^'\\]|\\.)*)'", x)
        return m.group(1).replace("\\'", "'") if m else ""
    if kind == "settings":
        for f in sorted(glob.glob(os.path.join(RELEASE, "includes/admin/settings/class-wc-settings-*.php"))):
            rel = os.path.relpath(f, RELEASE)
            L = lines(rel)
            tab = re.sub(r"^class-wc-settings-|\.php$", "", os.path.basename(f))
            for i, l in enumerate(L):
                m = re.search(r"'id'\s*=>\s*'([^']+)'", l)
                if not m:
                    continue
                near = L[max(0, i - 8): i + 10]
                o = {"tab": tab, "id": m.group(1)}
                for k in ("title", "desc", "desc_tip"):
                    for x in near:
                        if re.search(rf"'{k}'\s*=>", x) and tr(x):
                            o[k] = tr(x)
                            break
                for x in near:
                    t = re.search(r"'type'\s*=>\s*'([^']+)'", x)
                    if t:
                        o["type"] = t.group(1)
                        break
                out.append((".", f"woocommerce-11.2.1:{rel}", i + 1, "", o))
    elif kind == "admin-menus":
        rel = "includes/admin/class-wc-admin-menus.php"
        L = lines(rel)
        for i, l in enumerate(L):
            if re.search(r"add_(sub)?menu_page\(", l):
                blob = " ".join(L[i: i + 8])
                ts = re.findall(r"__\(\s*'([^']+)'", blob)
                parent = re.search(r"add_submenu_page\(\s*'([^']+)'", blob)
                out.append((".", f"woocommerce-11.2.1:{rel}", i + 1, "", {"menu": ts[1] if len(ts) > 1 else (ts[0] if ts else ""), "page title": ts[0] if ts else "",
                            "under": parent.group(1) if parent else "top level"}))
    elif kind == "capabilities":
        rel = "includes/class-wc-install.php"
        L = lines(rel)
        start = next(i for i, l in enumerate(L) if "function get_core_capabilities" in l)
        for i in range(start, start + 60):
            for c in re.findall(r"['\"]([a-z_{}$]+)['\"]", L[i]):
                if c not in ("core",) and ("_" in c or c in ("product",)):
                    out.append((".", f"woocommerce-11.2.1:{rel}", i + 1, "", {"capability": c}))
            if i > start and re.match(r"^\t}", L[i]):
                break
    elif kind == "webhook-topics":
        rel = "includes/class-wc-webhook.php"
        L = lines(rel)
        for i, l in enumerate(L):
            m = re.match(r"^\s*'([a-z_]+\.[a-z_]+)'\s*=>\s*array\(", l)
            if m:
                hooks = []
                for x in L[i + 1: i + 8]:
                    if ")" in x and "(" not in x:
                        break
                    hooks += re.findall(r"'([a-z_]+)'", x)
                out.append((".", f"woocommerce-11.2.1:{rel}", i + 1, "", {"topic": m.group(1), "fired by": hooks}))
    elif kind == "rest-controllers":
        rel = "includes/rest-api/Server.php"
        L = lines(rel)
        group = ""
        for i, l in enumerate(L):
            g = re.search(r"function get_(v\d|wc_admin|[a-z_]+)_controllers", l)
            if g:
                group = g.group(1)
            m = re.match(r"^\s*'([a-z0-9/_-]+)'\s*=>\s*'([A-Za-z0-9_\\\\]+)'", l)
            if m:
                out.append((".", f"woocommerce-11.2.1:{rel}", i + 1, "", {"api": group, "endpoint": m.group(1), "controller": m.group(2)}))
    elif kind == "features":
        rel = "src/Internal/Features/FeaturesController.php"
        L = lines(rel)
        for i, l in enumerate(L):
            m = re.match(r"^\s*('?[A-Za-z0-9_:-]+'?)\s*=>\s*array\(\s*$", l)
            if not m:
                continue
            near = L[i + 1: i + 12]
            o = {"feature": m.group(1).strip("'")}
            for k in ("name", "description"):
                for x in near:
                    if re.search(rf"'{k}'\s*=>", x) and tr(x):
                        o[k] = tr(x)
                        break
            for k in ("is_experimental", "enabled_by_default"):
                for x in near:
                    t = re.search(rf"'{k}'\s*=>\s*(true|false)", x)
                    if t:
                        o[k] = t.group(1)
                        break
            if "name" in o:
                out.append((".", f"woocommerce-11.2.1:{rel}", i + 1, "", o))
    return out


def translations(platform, spec):
    repo, root, sub = REPOS[platform]
    base = os.path.join(root, sub, "structures", platform) if not sub else os.path.join(root, sub, "structures")
    en, ar = (os.path.join(base, p) for p in spec.split(","))
    def load(p):
        try:
            d = json.load(open(p, encoding="utf-8"))
            return d if isinstance(d, dict) else {}
        except Exception:
            return {}
    e, a = load(en), load(ar)
    return {k: (v, a.get(k, "")) for k, v in e.items() if isinstance(v, str)}


def cited_lines(platform):
    """(file from the repository's root, line) pairs that what the model reads cites, where the line holds the same
    text at the head as at the cited commit."""
    repo, root, sub = REPOS[platform]
    by = collections.defaultdict(set)
    for s, loc in read_sources()[platform]:
        m = re.match(rf"^{repo}@([0-9a-f]+):(.+)$", s)
        if not m:
            continue
        f = re.sub(r"[#:]L?\d+(-L?\d+)?$", "", m.group(2))
        ln = re.search(r"\bline (\d+)", loc or "") or re.search(r"[#:]L(\d+)", m.group(2))
        by[(f, m.group(1))].add(int(ln.group(1)) if ln else 0)
    if platform == "woocommerce":
        for s, loc in read_sources()[platform]:
            m = re.match(r"^woocommerce-11\.2\.1:(.+)$", s)
            ln = re.search(r"\bline (\d+)", loc or "")
            if m:
                by[(f"woocommerce-11.2.1:{re.sub(r'[#:]L?[0-9]+(-L?[0-9]+)?$', '', m.group(1))}", "release")].add(int(ln.group(1)) if ln else 0)
    out = set()
    head_cache = {}
    for (f, c), lns in by.items():
        if c == "release":
            out |= {(f, l) for l in lns}
            continue
        if 0 in lns:
            out.add((f, 0))
        lns = {l for l in lns if l}
        if not lns:
            continue
        if f not in head_cache:
            p = os.path.join(root, f)
            head_cache[f] = open(p, encoding="utf-8", errors="replace").read().split("\n") if os.path.isfile(p) else []
        then = git(root, "show", f"{c}:{f}").split("\n")
        for l in lns:
            if l <= len(then) and l <= len(head_cache[f]) and then[l - 1] == head_cache[f][l - 1]:
                out.add((f, l))
    return out


def stable_id(p, structure, text, taken):
    h = hashlib.sha1(f"{structure}\x00{fold(text)}".encode()).hexdigest()
    for n in (8, 10, 12, 40):
        i = f"{PREFIX[p]}-E-{h[:n]}"
        if taken.get(i) in (None, (structure, fold(text))):
            taken[i] = (structure, fold(text))
            return i
    sys.exit("an id collision no length resolves")


def placed_ids(p):
    out = set()
    for path in glob.glob(os.path.join(HELD, p, "placements-*.tsv")):
        for r in rows(path):
            out |= {x.strip() for x in r["entry_id"].split(";") if x.strip()}
    return out


def cmd_registers(a):
    from held_vs_read import structures
    for s in structures(a.platform, read_sources()[a.platform]):
        print(f"{s['structure']}\theld {int(s['held'])}\tread {int(s['read'])}\titems {s['items']}\tcited {s['items_read']}\t{s['date_seen']}\t{s['what'][:120]}")


def strings_of(o, out, drop=()):
    if isinstance(o, dict):
        for k, v in o.items():
            if k not in SKIP and k not in drop:
                strings_of(v, out, drop)
    elif isinstance(o, list):
        for x in o:
            strings_of(x, out, drop)
    elif isinstance(o, str) and len(o.strip()) >= 3 and not OPAQUE.search(o.strip()):
        out.add(" ".join(o.split()))


def cmd_build(a):
    sel = [r for r in selection() if r["read"] == "yes" and (not a.platform or r["platform"] == a.platform)]
    by_p = collections.defaultdict(list)
    for r in sel:
        by_p[r["platform"]].append(r)
    failed = False
    for p, rs in by_p.items():
        repo, root, sub = REPOS[p]
        commit = git(root, "rev-parse", "--short=9", "HEAD").strip()
        cited = cited_lines(p)
        out, taken, report = [], {}, []
        for r in rs:
            rl = rules(r)
            rd = dict(rl)
            drop = set(rd.get("drop", "").split(",")) - {""}
            tr = translations(p, rd["translate"]) if "translate" in rd else None
            its = items_of(p, r["structure"], rl)
            groups = collections.OrderedDict()
            n_empty = n_match = n_read = 0
            unread_strings = set()
            for label, f, ln, ptr, o in its:
                if not says_something(o):
                    n_empty += 1
                    continue
                t = render(o, drop, tr)
                if "drop-match" in rd and re.search(rd["drop-match"], t):
                    n_match += 1
                    continue
                g = groups.setdefault(fold(t), {"text": t, "labels": [], "at": None, "read": False, "items": [], "section": ""})
                if label not in g["labels"]:
                    g["labels"].append(label)
                if (f, ln) in cited and not ptr:
                    g["read"] = True
                if g["at"] is None:
                    g["at"] = (f, ln, ptr)
                    g["section"] = next((clip(o.get(k), 80) for k in SECTION_KEYS if isinstance(o, dict) and isinstance(o.get(k), (str, int)) and o.get(k) not in ("",)), "")
                g["items"].append(o)
            n_entries = 0
            text_all = []
            for g in groups.values():
                if g["read"]:
                    n_read += 1
                    continue
                for o in g["items"]:
                    strings_of(o, unread_strings, drop)
                f, ln, ptr = g["at"]
                n_entries += 1
                if len(g["text"]) > MAX_TEXT:
                    report.append(f"PROBLEM {p} {r['structure']}: an entry of {len(g['text'])} characters holds a list: give the structure a nested: rule ({clip(g['text'], 120)})")
                    failed = True
                text_all.append(fold(g["text"]))
                loc = f"line {ln}" if ln else ""
                if ptr:
                    loc = (loc + " " if loc else "") + f"pointer {ptr}"
                out.append([stable_id(p, r["structure"], g["text"], taken), r["structure"], ",".join(g["labels"]),
                            f if f.startswith("woocommerce-11.2.1:") else f"{repo}@{commit}:{f}", loc, g["section"], g["text"]])
            hay = " ".join(text_all)
            reached = sum(1 for s in unread_strings if fold(s) in hay)
            share = reached / len(unread_strings) if unread_strings else 1.0
            report.append(f"{p} {r['structure']}: {len(its)} items after its rule, {n_empty} say nothing, {n_match} dropped by drop-match, "
                          f"{len(groups)} renderings, {n_read} read already, {n_entries} entries; {share:.0%} of the unread items' strings reach an entry")
            if not its:
                report.append(f"PROBLEM {p} {r['structure']}: no item: check its rule ({r.get('rule')})")
                failed = True
            elif n_entries == 0 and len(groups) > n_read:
                report.append(f"PROBLEM {p} {r['structure']}: no entry, though some renderings are unread")
                failed = True
            if share < 0.9:
                report.append(f"PROBLEM {p} {r['structure']}: only {share:.0%} of the unread items' strings reach an entry: its rendering loses words")
                failed = True
        lost = placed_ids(p) - {l[0] for l in out}
        if lost:
            sys.exit(f"{p}: the rebuild would drop {len(lost)} entries that placements name, such as {sorted(lost)[:3]}: refused")
        os.makedirs(os.path.join(HELD, p), exist_ok=True)
        with open(os.path.join(HELD, p, "entries.tsv"), "w", encoding="utf-8") as fh:
            fh.write("\t".join(E_HEAD) + "\n")
            for l in out:
                fh.write("\t".join(x.replace("\t", " ").replace("\n", " ") for x in l) + "\n")
        for l in report:
            print(l)
        print(f"{p}: {len(out)} entries from {len(rs)} structures at {repo}@{commit}")
    sys.exit(1 if failed else 0)


def entries(p):
    path = os.path.join(HELD, p, "entries.tsv")
    return rows(path) if os.path.exists(path) else []


def batch_ids(batch):
    path = os.path.join(HELD, "batches", f"{batch}.txt")
    if not os.path.exists(path):
        sys.exit(f"no batch {batch}: held/batches/{batch}.txt")
    return [l.strip() for l in open(path, encoding="utf-8") if l.strip()]


def cmd_batches(a):
    """Cuts the entries no batch holds yet into batches of about --size, where a structure or a section ends."""
    os.makedirs(os.path.join(HELD, "batches"), exist_ok=True)
    taken = set()
    for path in glob.glob(os.path.join(HELD, "batches", "*.txt")):
        taken |= set(batch_ids(os.path.basename(path)[:-4]))
    lines = []
    for p in PLATFORMS:
        es = [e for e in entries(p) if e["entry_id"] not in taken]
        k = len(glob.glob(os.path.join(HELD, "batches", f"{PREFIX[p]}-*.txt")))
        cur = []
        for i, e in enumerate(es):
            cur.append(e)
            last = i == len(es) - 1
            nxt = es[i + 1] if not last else None
            boundary = last or nxt["structure"] != e["structure"] or nxt["section"] != e["section"]
            if last or (boundary and len(cur) >= a.size * 0.5) or len(cur) >= a.size * 1.3:
                k += 1
                b = f"{PREFIX[p]}-{k}"
                with open(os.path.join(HELD, "batches", f"{b}.txt"), "w", encoding="utf-8") as fh:
                    fh.write("\n".join(x["entry_id"] for x in cur) + "\n")
                lines.append([b, p, str(len(cur)), ",".join(dict.fromkeys(x["structure"] for x in cur))])
                cur = []
    path = os.path.join(HELD, "batches.tsv")
    new = not os.path.exists(path) or not taken
    with open(path, "w" if new else "a", encoding="utf-8") as fh:
        if new:
            fh.write("batch\tplatform\tentries\tstructures\n")
        for l in lines:
            fh.write("\t".join(l) + "\n")
            print("\t".join(l)[:180])


# an identifier, whole: a word is never matched from its middle (BigCommerce is one token, never "igCommerce")
TOKEN = re.compile(r"(?<![A-Za-z0-9])(?:[A-Za-z][A-Za-z0-9]*(?:[_:./-][A-Za-z0-9]+)+|[a-z]+[A-Z][A-Za-z0-9]+|[A-Z]{2,}_[A-Z_]+)(?![A-Za-z0-9])")


def candidate_index(platform):
    """For leads only: the identifiers in the statements each capability's cells cite on this platform, and every
    platform's terms for each capability."""
    from class_slice import citable, key
    st = {key(x): x for x in citable(platform)}
    by_tok = collections.defaultdict(set)
    for r in rows(os.path.join(MODEL, "merged", "evidence.tsv")):
        if r["platform"] != platform:
            continue
        x = st.get(r["key"])
        if not x:
            continue
        for t in TOKEN.findall((x.get("identifier") or "") + " " + (x.get("statement") or "")):
            if len(t) >= 5:
                by_tok[t.casefold()].add(r["cap_id"])
    terms = collections.defaultdict(set)
    names = {}
    for r in rows(os.path.join(MODEL, "merged", "cells.tsv")):
        for t in (r.get("terms") or "").split(";"):
            t = fold(t)
            if len(t) >= 4:
                terms[t].add(r["cap_id"])
    for r in rows(os.path.join(MODEL, "merged", "capabilities.tsv")):
        names[r["cap_id"]] = r["capability"]
    return by_tok, terms, names


def candidates(e, idx):
    by_tok, terms, names = idx
    score = collections.Counter()
    why = collections.defaultdict(set)
    for t in set(TOKEN.findall(e["text"])):
        for c in by_tok.get(t.casefold(), ()):
            score[c] += 2
            why[c].add(t)
    ft = " " + fold(e["text"]) + " "
    for t, cs in terms.items():
        if f" {t} " in ft or (len(t) > 8 and t in ft):
            for c in cs:
                score[c] += 1
                why[c].add(t)
    return [(c, sorted(why[c])[:3]) for c, _ in score.most_common(3)]


def cmd_show(a):
    es = entries(a.platform)
    if a.batch:
        by = {e["entry_id"]: e for e in es}
        es = [by[i] for i in batch_ids(a.batch) if i in by]
    if a.structure:
        es = [e for e in es if e["structure"] == a.structure]
    if a.meta:
        seen = set()
        for e in es:
            if e["structure"] in seen:
                continue
            seen.add(e["structure"])
            for m in sorted(glob.glob(os.path.join(folder(a.platform, e["structure"]), "**", "meta.json"), recursive=True))[:1]:
                try:
                    d = json.load(open(m, encoding="utf-8"))
                except Exception:
                    continue
                keep = {k: d[k] for k in ("structure", "surface", "shape", "shape_observed", "counts", "items", "of") if k in d}
                print(f"[{e['structure']}] {clip(json.dumps(keep, ensure_ascii=False), 1500)}")
        return
    lo, hi = (a.__dict__.get("from") or 1), (a.to or len(es))
    idx = candidate_index(a.platform) if a.candidates else None
    for i, e in enumerate(es, 1):
        if lo <= i <= hi:
            lab = e["labels"] if e["labels"] not in ("", ".") else ""
            print(f"{i:>4} {e['entry_id']} [{e['structure']}{' @' + clip(lab, 80) if lab else ''}] {clip(e['text'], a.width)}")
            if idx:
                cs = candidates(e, idx)
                if cs:
                    print("       leads: " + "; ".join(f"{c} {clip(idx[2].get(c, ''), 50)} (by {', '.join(w)})" for c, w in cs))


PARTNER = re.compile(r"collaborator|partner-api|app-install|stores-access-requests|portal-app-scopes", re.I)


def cmd_check(a):
    problems, notes = [], []
    ids = batch_ids(a.batch)
    es = {e["entry_id"]: e for e in entries(a.platform)}
    order = {i: n for n, i in enumerate(ids)}
    caps = {r["cap_id"]: r for r in rows(os.path.join(MODEL, "merged", "capabilities.tsv"))}
    cap_names = {fold(r["capability"].split(":")[0].split("(")[0]) for r in caps.values()} | {fold(c) for c in caps}
    path = os.path.join(HELD, a.platform, f"placements-{a.batch}.tsv")
    if not os.path.exists(path):
        sys.exit(f"no {os.path.relpath(path, ROOT)}")
    raw = open(path, encoding="utf-8-sig").read().replace("\r\n", "\n").split("\n")
    if raw[0].split("\t") != P_HEAD:
        problems.append(f"placements-{a.batch}.tsv: header must be: {' '.join(P_HEAD)}")
    seen = collections.defaultdict(list)
    new_names = collections.defaultdict(list)
    for i, l in enumerate(raw[1:], 2):
        if not l.strip():
            continue
        f = l.split("\t")
        w = f"placements-{a.batch}.tsv line {i}"
        if len(f) != len(P_HEAD) or '"' in l:
            problems.append(f"{w}: {len(P_HEAD)} tab-separated fields, no quoting (it has {len(f)})"); continue
        r = dict(zip(P_HEAD, f))
        pieces = [x.strip() for x in r["entry_id"].split(";")]
        if not r["entry_id"].strip() or any(not x for x in pieces):
            problems.append(f"{w}: entry_id names one entry, or several `;`-separated, with no empty piece"); continue
        for x in pieces:
            if x not in order:
                problems.append(f"{w}: {x} is not an entry of batch {a.batch}")
        ok = [x for x in pieces if x in order]
        if len(ok) > 1:
            ns = sorted(order[x] for x in ok)
            if ns != list(range(ns[0], ns[0] + len(ns))) or len({es[x]["structure"] for x in ok if x in es}) > 1:
                problems.append(f"{w}: a group's entries are consecutive in the batch, and of one structure")
        for fld in ("supports", "scope", "terms", "filler", "quality"):
            if r[fld] and any(not x.strip() for x in r[fld].split(";")):
                problems.append(f"{w}: {fld} has an empty piece")
        ss = [x.strip() for x in r["supports"].split(";") if x.strip()]
        if r["placement"] not in PLACEMENTS:
            problems.append(f"{w}: placement is one of {', '.join(PLACEMENTS)}")
        if r["placement"] == "capability":
            if r["cap_id"] not in caps:
                problems.append(f"{w}: capability names one cap_id of the merged model (an entry two capabilities' takes two lines)")
            if not ss or any(x not in SUPPORTS for x in ss) or len(ss) > 2 or len(set(ss)) != len(ss):
                problems.append(f"{w}: supports is one value of {', '.join(SUPPORTS)}, or two different ones, `;`-separated")
            for x in ok:
                if x in seen and any(c == r["cap_id"] or pl != "capability" for c, pl in seen[x]):
                    problems.append(f"{w}: {x} placed again on the same capability, or placed otherwise too")
        elif r["placement"] == "new":
            m = re.match(r"^new:(\S.*\S|\S)$", r["cap_id"])
            if not m:
                problems.append(f"{w}: a new capability is named in cap_id as new:<its name, in the platform's words>")
            else:
                nm = m.group(1)
                if fold(nm) in cap_names or re.match(r"^CM-[A-Z]{3}-\d{3}$", nm):
                    problems.append(f"{w}: new:{nm} is an existing capability's name or id: place it there")
                new_names[fold(nm)].append(nm)
            if not ss or any(x not in SUPPORTS for x in ss):
                problems.append(f"{w}: a new thing says what the entry supports")
            for x in ok:
                if x in seen:
                    problems.append(f"{w}: {x} placed again")
        elif r["placement"] == "out":
            if any(r[k].strip() for k in ("cap_id", "supports", "scope", "terms", "filler", "quality")):
                problems.append(f"{w}: out names no capability, supports nothing, and has no scope, terms, filler or quality")
            for x in ok:
                if x in seen:
                    problems.append(f"{w}: {x} placed again")
        for t in [x.strip() for x in r["terms"].split(";") if x.strip()]:
            if not all(fold(t) in fold(es[x]["text"]) for x in ok if x in es):
                problems.append(f"{w}: term {t!r} is not in the text of each of its entries")
        if not r["reading"].strip():
            problems.append(f"{w}: reading says why, as a reading")
        for x in ok:
            seen[x].append((r["cap_id"], r["placement"]))
        if "own-service" in ss and ok:
            notes.append(f"own-service on {r['cap_id']}: {clip(es.get(ok[0], {}).get('text', ''), 160)}")
        if "core" in ss and ok and PARTNER.search(es.get(ok[0], {}).get("structure", "")):
            notes.append(f"core on a partner's or an app's permission ({es[ok[0]]['structure']}): the dry run's S7 makes it shows")
    for k, names in new_names.items():
        if len(set(names)) > 1:
            problems.append(f"one new thing named several ways: {sorted(set(names))}: name it one way")
    for x in ids:
        if x not in seen:
            problems.append(f"{x} has no placement")
    notes_path = os.path.join(HELD, a.platform, f"notes-{a.batch}.md")
    if not os.path.exists(notes_path):
        problems.append(f"no notes-{a.batch}.md")
    else:
        nt = fold(open(notes_path, encoding="utf-8").read())
        for k, names in new_names.items():
            if fold(names[0]) not in nt:
                problems.append(f"notes-{a.batch}.md doesn't name the new thing {names[0]!r}")
    for n in notes[:60]:
        print("NOTE", n)
    for k, names in sorted(new_names.items()):
        print(f"NEW {names[0]}: {len(names)} lines")
    for p in problems[:200]:
        print("PROBLEM", p)
    if len(problems) > 200:
        print(f"... and {len(problems) - 200} more")
    print(f"{len(set(seen) & set(ids))} of {len(ids)} entries placed; {len(problems)} problems")
    sys.exit(1 if problems else 0)


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("registers"); s.add_argument("--platform", choices=PLATFORMS, required=True); s.set_defaults(f=cmd_registers)
    s = sub.add_parser("build"); s.add_argument("--platform", choices=PLATFORMS); s.set_defaults(f=cmd_build)
    s = sub.add_parser("batches"); s.add_argument("--size", type=int, default=300); s.set_defaults(f=cmd_batches)
    s = sub.add_parser("show"); s.add_argument("--platform", choices=PLATFORMS, required=True)
    s.add_argument("--batch"); s.add_argument("--structure"); s.add_argument("--from", type=int); s.add_argument("--to", type=int)
    s.add_argument("--width", type=int, default=600); s.add_argument("--meta", action="store_true")
    s.add_argument("--candidates", action="store_true", help="each entry's leads: capabilities whose cited statements share its identifiers, or whose terms it holds")
    s.set_defaults(f=cmd_show)
    s = sub.add_parser("check"); s.add_argument("--platform", choices=PLATFORMS, required=True)
    s.add_argument("--batch", required=True); s.set_defaults(f=cmd_check)
    a = ap.parse_args()
    a.f(a)


if __name__ == "__main__":
    main()
