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
#   files:<n1>,<n2>           the structure's JSONL files so named are its items, not items.jsonl alone (a CLI's
#                             topics.jsonl beside its commands)
#   json:<glob>               the JSON files the glob names (from the repository's root), each one item; json1: the
#                             last of them only
#   changes:<path>            a route manifest's changes, before and after, from the repository's derived file
#   label:<key>=<pattern>     an item's label is what the pattern's first group matches in its field (a page's country
#                             site, from its uri), so the entries it renders carry every site that states them
#   prune:<k1>,<k2>           leaves out what sits under those keys, at any depth, before the rules below read it (a
#                             page's own copies of its words: its translations, the site's header and footer)
#   wrap:<k1>,<k2>            the dicts at those keys, at any depth, are lists of one, so nested: can name them (a
#                             card that stands alone: a plan card, a table's column headers)
#   pick:<p1>,<p2>            adds, before each item, one item of only the fields at those paths (`/`-separated):
#                             what a page states beside its lists (its prices and terms, the variant it was served)
#   dict:<key>                one item per key of the dict at <key>, with its value
#   name:<k1>,<k2>            the fields that name an item for nested:, ahead of the usual name, title, label and the
#                             like (a page's uri, a section's heading), so the elements under it carry them
#   nested:<k1>,<k2>          one item per element of each list so named, at any depth, carrying its ancestors' names
#   new-vs:<structure>        the items whose name the named structure lacks
#   merge:<key>               the items of one source line (a page) that state the same value of the key are one item:
#                             the first's fields, then each field it lacks from the others; a field they state
#                             differently keeps each distinct value, ` | `-separated (a feature listed in two sections),
#                             a value that only begins another giving way to it
#   where:<key>=<v1>|<v2>     the items whose field has one of the values; where:<key>!= keeps those where it is set
#   labels:<pattern>          the items of the labels that match
#   latest:<k1>,<k2>          of the items that state the same value of the first of those keys they have, only those
#                             in the words of the latest version (the label, after any `@`) are kept: a target or a
#                             command once, as its newest version states it, under each version that states it so
#   group:<key>=<v1>|<v2>[/<h1>|<h2>]   a rendered page's items in order: each one whose field has one of the values
#                             begins an item that holds those after it (`then`), up to the next; one with an h value
#                             stays alone and names the groups after it (a feature's heading, its paragraph and links,
#                             under its section's heading)
#   meta:<k1>,<k2>            adds one item per value of those keys of the structure's meta.json, where the extractor
#                             kept what the platform states beside its items
#   drop:<k1>,<k2>            leaves those fields out of the rendering
#   nodes:<field>             each item joined to its node in the answer beside items.jsonl that its field names
#                             (`<value, '/' as '~'>.json`), the s: nodes in document order: what the item leaves out
#                             (a sub-page's href and features, a plan gate's plans, a field's controls and options, the
#                             words it shows), and a parent with no name of its own named by its kind under its nearest
#                             named ancestor, so the same item in each store's answer is one entry (Salla's settings)
#   long:<n>                  the structure's entries are prose, each one statement the platform publishes whole (a
#                             changelog post, a feature's dialog): an entry up to n characters is not taken for a list
#   drop-match:<pattern>      drops the items whose rendering matches
#   translate:<en>,<ar>       resolves values that are keys of those translation files (paths from the structures folder)
#
# Usage:
#   python3 -I method/held_entries.py registers --platform P       every registered structure: held, cited, items
#   python3 -I method/held_entries.py build [--platform P]          writes held/<platform>/entries.tsv, reports per structure
#   python3 -I method/held_entries.py batches [--size N]            cuts the entries no batch holds into batches
#   python3 -I method/held_entries.py show --platform P (--batch B | --structure S) [--from I] [--to J] [--width W] [--meta]
#                                                [--candidates]   each entry's leads, by identifier or by term: leads only
#   python3 -I method/held_entries.py makers --platform P NAME ...   the held entries naming NAME with a maker's cue
#   python3 -I method/held_entries.py check --platform P --batch B  checks held/<platform>/placements-<B>.tsv
import argparse, math, collections, csv, glob, hashlib, json, os, re, subprocess, sys, unicodedata
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


def name_of(o, names=()):
    # a country, a package or a variant names a list's element too, so a nested entry carries it (inspection-H2, MF-5)
    if isinstance(o, dict):
        for k in (*names, "name", "title", "label", "key", "slug", "handle", "id", "path", "url", "display_name", "location",
                  "store_country", "duration_code"):
            v = o.get(k)
            if isinstance(v, dict):
                v = v.get("en") or next(iter(v.values()), "")
            if isinstance(v, str) and v.strip():
                return v.strip()
    return ""


def flatten(o, keys, trail=(), names=()):
    """One item per element of each list named in keys, at any depth, carrying its ancestors' names."""
    out = []
    if isinstance(o, dict):
        here = trail + ((name_of(o, names),) if name_of(o, names) else ())
        for k, v in o.items():
            if k in keys and isinstance(v, list):
                for i, x in enumerate(v):
                    if isinstance(x, dict):
                        out.append(({"within": " > ".join(here), "list": k, **{kk: vv for kk, vv in x.items() if kk not in keys}}, f"/{k}/{i}"))
                        out += [(it, f"/{k}/{i}{p}") for it, p in flatten(x, keys, here + ((name_of(x, names),) if name_of(x, names) else ()), names)]
                    else:
                        out.append(({"within": " > ".join(here), "list": k, "value": x}, f"/{k}/{i}"))
            elif isinstance(v, (dict, list)):
                out += [(it, f"/{k}{p}") for it, p in flatten(v, keys, here, names)]
    elif isinstance(o, list):
        for i, x in enumerate(o):
            out += [(it, f"/{i}{p}") for it, p in flatten(x, keys, trail, names)]
    return out


SETTINGS_CONTROLS = {"s-toggle", "s-select", "s-input", "s-radio", "s-checkbox", "s-calendar", "s-lingual-field",
                     "s-uploader", "s-tags", "s-tel-input"}
SETTINGS_SKIP = {"_", "$", "class", "className", "slot", "loading", "overlayAlignment", "wide", "portal", "placeholder",
                 "created_at", "updated_at", "initialValues", "invalidateQueries", "start", "label", "description", "id",
                 "action", "method", "path", "permissions", "flag", "title"}


def store_cond(c):
    """A settings `if`'s condition as a gate on the store, in the answer's identifiers (a feature, the store's plan), or
    None where it isn't one (a form's value, a query's state)."""
    if not isinstance(c, dict):
        return None
    k, v = c.get("_"), c.get("$")
    if k == "useFeature" and isinstance(v, list) and v and all(isinstance(x, str) for x in v):
        return " and ".join(v)
    if k == "not":
        inner = store_cond(v)
        return f"not {inner}" if inner else None
    if (k in ("eq", "neq") and isinstance(v, list) and len(v) == 2 and isinstance(v[0], dict)
            and v[0].get("_") == "getStorePlan" and isinstance(v[1], str)):
        return f"plan {'' if k == 'eq' else 'not '}{v[1]}"
    if k in ("and", "or") and isinstance(v, list):
        parts = [store_cond(x) for x in v if x is not None]
        if k == "or":
            return " or ".join(parts) if parts and all(parts) else None
        parts = [x for x in parts if x]
        return " and ".join(parts) if parts else None
    return None


def settings_nodes(path, cache={}):
    """A settings section's answer: its s: nodes in document order, the order the structure's items list them in,
    each with the store gates of the `if`s it sits under (an `else` under the condition's negation, SA-50's T2)."""
    if path not in cache:
        seq = []
        def walk(o, conds=()):
            if isinstance(o, dict):
                if isinstance(o.get("_"), str) and o["_"].startswith("s:"):
                    seq.append((o, conds))
                c = store_cond(o.get("condition")) if o.get("_") == "if" else None
                for kk, v in o.items():
                    if c and kk == "else":
                        walk(v, conds + (f"not ({c})" if " " in c else f"not {c}",))
                    elif c and kk != "condition":
                        walk(v, conds + (c,))
                    else:
                        walk(v, conds)
            elif isinstance(o, list):
                for v in o:
                    walk(v, conds)
        try:
            walk(json.load(open(path, encoding="utf-8")))
        except Exception:
            pass
        cache[path] = seq
    return cache[path]


def settings_extra(node, own=()):
    """What a settings node states that its item leaves out: its scalar fields (a sub-page's href, its features, a plan
    gate's plans), the controls under it with their options, and the other words it shows (tooltips, badges, alerts),
    as translation keys, each once; nothing under another s: node."""
    out = {k: v for k, v in node.items() if k not in SETTINGS_SKIP and (isinstance(v, (str, int, float, bool))
           or (isinstance(v, list) and v and all(isinstance(x, (str, int, float)) for x in v)))}
    controls, words, taken = [], [], set(own)
    def key(v):
        return v.get("$") if isinstance(v, dict) and v.get("_") == "t" and isinstance(v.get("$"), str) else None
    def walk(o, top):
        if isinstance(o, dict):
            k = o.get("_")
            if not top and isinstance(k, str) and k.startswith("s:"):
                return
            if key(o):
                if key(o) not in taken:
                    taken.add(key(o)); words.append({"text": key(o)})
                return
            if k in SETTINGS_CONTROLS:
                c = {"control": k, **{kk: o[kk] for kk in ("type", "name", "min", "max", "step", "multiselect")
                                      if isinstance(o.get(kk), (str, int, float, bool))}}
                opts = [it for it in o.get("items") if isinstance(it, dict)] if isinstance(o.get("items"), list) else []
                if opts:
                    c["options"] = [{"option": key(it.get("label")) or it.get("label") or it.get("value")} for it in opts]
                    taken.update(key(it.get("label")) for it in opts if key(it.get("label")))
                controls.append(c)
            for kk, v in o.items():
                if kk != "_":
                    walk(v, False)
        elif isinstance(o, list):
            for v in o:
                walk(v, False)
    walk(node, True)
    if controls:
        out["controls"] = controls
    if words:
        out["shows"] = words
    return out


def selection():
    path = os.path.join(HELD, "selection.tsv")
    return rows(path) if os.path.exists(path) else []


RULE = re.compile(r";(?=\s*(?:rows|text|files|json1?|changes|label|prune|wrap|pick|dict|name|nested|new-vs|merge|where|labels|latest|group|drop|drop-match|translate|release|meta|long|nodes):)")


def pruned(o, keys, wrap=()):
    if isinstance(o, dict):
        return {k: ([pruned(v, keys, wrap)] if k in wrap and isinstance(v, dict) else pruned(v, keys, wrap)) for k, v in o.items() if k not in keys}
    if isinstance(o, list):
        return [pruned(x, keys, wrap) for x in o]
    return o


def merged(a, b):
    """b's statements added to a's: the fields a lacks, and each value a states otherwise."""
    for k, v in b.items():
        if k not in a or a[k] in (None, "", [], {}):
            a[k] = v
        elif a[k] != v and v not in (None, "", [], {}):
            if isinstance(a[k], list) and isinstance(v, list):
                a[k] = a[k] + [x for x in v if x not in a[k]]
            elif isinstance(a[k], dict) and isinstance(v, dict):
                a[k] = merged(dict(a[k]), v)
            elif isinstance(a[k], (str, int, float)) and isinstance(v, (str, int, float)):
                had = str(a[k]).split(" | ")
                if any(h.startswith(str(v)) for h in had):        # said already, or the start of what was said
                    continue
                kept = [h for h in had if not str(v).startswith(h)]  # a value v continues (an ancestor's name) gives way
                a[k] = " | ".join(kept + [str(v)])
    return a


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
        files = sorted(f for n in rd.get("files", "items.jsonl").split(",") for f in glob.glob(os.path.join(base, "**", n), recursive=True))
        for f in files:
            label = os.path.relpath(os.path.dirname(f), base)
            here = []
            for i, l in enumerate(open(f, encoding="utf-8", errors="replace"), 1):
                try:
                    here.append((label, os.path.relpath(f, root), i, "", json.loads(l)))
                except Exception:
                    continue
            # a group given only as the position of the item it sits under is that item's name (inspection-H2, SF-8)
            at = {x[4].get("position"): x[4] for x in here if isinstance(x[4], dict) and isinstance(x[4].get("position"), int)}
            def called(p):
                props = p.get("props") if isinstance(p.get("props"), dict) else {}
                return next((str(v).strip() for v in (name_of(p), p.get("text"), p.get("aria_label"), props.get("title"))
                             if isinstance(v, str) and v.strip()), "")
            for x in here:
                o = x[4]
                for k in ("parent", "within"):
                    if isinstance(o, dict) and isinstance(o.get(k), int) and not isinstance(o.get(k), bool) and o[k] in at and called(at[o[k]]):
                        o[k] = called(at[o[k]])
            if "nodes" in rd:
                k_of, off = collections.Counter(), collections.Counter()
                for x in here:
                    o = x[4]
                    sec = o.get(rd["nodes"] or "section") if isinstance(o, dict) else None
                    if not isinstance(sec, str):
                        continue
                    seq = settings_nodes(os.path.join(os.path.dirname(f), sec.replace("/", "~") + ".json"))
                    i = k_of[sec]; k_of[sec] += 1
                    node, conds = seq[i] if i < len(seq) else (None, ())
                    if node is None or node.get("_") != o.get("kind"):
                        off[sec] += 1
                        continue
                    if conds and not o.get("if"):
                        o["if"] = " and ".join(dict.fromkeys(conds))
                    own = {v.get("$") for v in (node.get("label"), node.get("description")) if isinstance(v, dict) and v.get("_") == "t"}
                    for kk, vv in settings_extra(node, own).items():
                        if o.get(kk) in (None, "", [], {}):
                            o[kk] = vv
                if off:
                    print(f"NOTE {structure} {label}: {sum(off.values())} items not joined to their answers' nodes ({', '.join(sorted(off)[:5])})")
                def lineage(p, seen=()):
                    q = at.get(p)
                    if not isinstance(q, dict) or p in seen:
                        return ""
                    if called(q):
                        return called(q)
                    up = q.get("parent")
                    up = lineage(up, seen + (p,)) if isinstance(up, int) and not isinstance(up, bool) else (up if isinstance(up, str) else "")
                    return str(q.get("kind") or "item") + (f" under {up}" if up else "")
                for x in here:
                    o = x[4]
                    if isinstance(o, dict) and isinstance(o.get("parent"), int) and not isinstance(o.get("parent"), bool):
                        o["parent"] = lineage(o["parent"]) or o["parent"]
            out += here
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
    if "label" in rd:
        k, pat = rd["label"].split("=", 1)
        def site(label, o):
            m = re.search(pat, str(o.get(k, ""))) if isinstance(o, dict) else None
            return (next((g for g in m.groups() if g), m.group(0)) if m.groups() else m.group(0)) if m else label
        out = [(site(label, o), f, ln, ptr, o) for label, f, ln, ptr, o in out]
    if "prune" in rd or "wrap" in rd:
        keys, wrap = set(rd.get("prune", "").split(",")) - {""}, set(rd.get("wrap", "").split(",")) - {""}
        out = [(label, f, ln, ptr, pruned(o, keys, wrap)) for label, f, ln, ptr, o in out]
    if "pick" in rd:
        nxt = []
        for label, f, ln, ptr, o in out:
            got, at = {}, []
            for p in rd["pick"].split(","):
                v = o
                for step in p.split("/"):
                    v = v.get(step) if isinstance(v, dict) else None
                if v not in (None, "", [], {}):
                    got[p.split("/")[-1]] = v
                    at.append(f"{ptr}/{p}")
            if says_something(got):
                nxt.append((label, f, ln, " + ".join(at), got))
            nxt.append((label, f, ln, ptr, o))
        out = nxt
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
            fl = flatten(o, keys, (), tuple(rd.get("name", "").split(",")) if rd.get("name") else ())
            # an item the platform names (its name, title or label) is an entry of its own, without its lists, before
            # its elements: Salla's navigation sections, with their permissions, had none (SA-20's check)
            if fl and isinstance(o, dict) and any(o.get(k) and isinstance(o.get(k), (str, dict)) for k in ("name", "title", "label")):
                nxt.append((label, f, ln, ptr, {k: v for k, v in o.items() if k not in keys}))
            nxt += [(label, f, ln, ptr + p, it) for it, p in fl] if fl else [(label, f, ln, ptr, o)]
        out = nxt
    if "new-vs" in rd:
        old = {name_of(o) for _, _, _, _, o in items_of(platform, rd["new-vs"], [])}
        out = [x for x in out if name_of(x[4]) not in old]
    if "merge" in rd:
        k, nxt, at = rd["merge"], [], {}
        for label, f, ln, ptr, o in out:
            v = o.get(k) if isinstance(o, dict) else None
            if not isinstance(v, (str, int)) or isinstance(v, bool) or str(v).strip() == "":
                nxt.append((label, f, ln, ptr, o))
            elif (label, f, ln, v) in at:
                merged(at[(label, f, ln, v)], o)
            else:
                at[(label, f, ln, v)] = dict(o)
                nxt.append((label, f, ln, ptr, at[(label, f, ln, v)]))
        out = nxt
    if "where" in rd:
        k, op, vals = re.match(r"^([^=!]+)(!?=)(.*)$", rd["where"]).groups()
        if op == "!=":
            out = [x for x in out if isinstance(x[4], dict) and x[4].get(k) not in (None, "")]
        else:
            vs = set(vals.split("|"))
            out = [x for x in out if isinstance(x[4], dict) and str(x[4].get(k, "")) in vs]
    if "labels" in rd:
        out = [x for x in out if re.search(rd["labels"], x[0])]
    if "latest" in rd:
        def version(label):
            v = label.rsplit("@", 1)[-1]
            main, _, pre = v.partition("-")
            nums = lambda s: tuple(int(x) if x.isdigit() else -1 for x in re.split(r"[.]", s) if x)
            return (nums(main), 0 if pre else 1, nums(pre))
        ks = rd["latest"].split(",")
        def what(o):
            return next(((k, str(o[k])) for k in ks if isinstance(o, dict) and str(o.get(k) or "").strip()), None)
        drop = set(rd.get("drop", "").split(",")) - {""}
        best = {}
        for x in out:
            w = what(x[4])
            if w and (w not in best or version(x[0]) > version(best[w][0])):
                best[w] = (x[0], fold(render(x[4], drop)))
        # an earlier version that states it in the same words stays, so its label and a citation of it still count
        out = [x for x in out if not what(x[4]) or fold(render(x[4], drop)) == best[what(x[4])][1]]
    if "group" in rd:
        k, vals = rd["group"].split("=", 1)
        starts, _, heads = vals.partition("/")
        starts, heads = set(starts.split("|")), set(heads.split("|")) - {""}
        nxt, cur, head = [], None, {}
        for label, f, ln, ptr, o in out:
            v = str(o.get(k, "")) if isinstance(o, dict) else ""
            if v in heads:
                head[(label, f)] = str(o.get("text") or name_of(o)).strip()
                nxt.append((label, f, ln, ptr, o))
                cur = None
            elif v in starts or cur is None or cur[0] != (label, f):
                cur = ((label, f), {**({"within": head[(label, f)]} if head.get((label, f)) else {}), **o})
                nxt.append((label, f, ln, ptr, cur[1]))
            else:
                cur[1].setdefault("then", []).append(o)
        out = nxt
    if "meta" in rd:
        # What the platform states beside its items, which the extractor kept in meta.json (BigCommerce's plan prices
        # above its plan table): one entry per value of each named key, at its JSON pointer.
        for m in sorted(glob.glob(os.path.join(base, "**", "meta.json"), recursive=True)):
            try:
                d = json.load(open(m, encoding="utf-8"))
            except Exception:
                continue
            for k in rd["meta"].split(","):
                if k not in d:
                    continue
                vs = d[k] if isinstance(d[k], list) else [d[k]]
                for i, v in enumerate(vs):
                    ptr = f"/{k}/{i}" if isinstance(d[k], list) else f"/{k}"
                    out.append((os.path.relpath(os.path.dirname(m), base), os.path.relpath(m, root), 0, ptr,
                                {"key": k, **v} if isinstance(v, dict) else {"key": k, "value": v}))
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
                # the setting's own array( ... ): its fields sit at the id's depth, between the array( that opens it and the
                # ) that closes it, so a neighbour's title or type is never read as its own (WC-7's agent found 51 so)
                depth = len(l) - len(l.lstrip("\t "))
                start = i
                while start > 0 and not (re.search(r"array\(\s*$", L[start - 1]) and len(L[start - 1]) - len(L[start - 1].lstrip("\t ")) < depth):
                    start -= 1
                    if i - start > 40:
                        break
                end = i
                while end + 1 < len(L) and end - i < 40:
                    x = L[end + 1]
                    if x.strip().startswith(")") and len(x) - len(x.lstrip("\t ")) < depth:
                        break
                    end += 1
                own = [x for x in L[start: end + 1] if len(x) - len(x.lstrip("\t ")) == depth]
                o = {"tab": tab, "id": m.group(1)}
                for k in ("title", "desc", "desc_tip"):
                    for x in own:
                        if re.search(rf"^\s*'{k}'\s*=>", x) and tr(x):
                            o[k] = tr(x)
                            break
                for x in own:
                    t = re.search(r"^\s*'type'\s*=>\s*'([^']+)'", x)
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
                if len(g["text"]) > int(rd.get("long") or MAX_TEXT):
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
        n_of = collections.Counter(e["structure"] for e in es)
        cut, cur = [], []
        for i, e in enumerate(es):
            cur.append(e)
            last = i == len(es) - 1
            nxt = es[i + 1] if not last else None
            boundary = last or nxt["structure"] != e["structure"] or nxt["section"] != e["section"]
            # a structure of --alone entries or more starts and ends its own batches, so its batches don't wait on
            # another structure's, nor another's on its
            alone = a.alone and not last and nxt["structure"] != e["structure"] and max(n_of[e["structure"]], n_of[nxt["structure"]]) >= a.alone
            if last or alone or (boundary and len(cur) >= a.size * a.min) or len(cur) >= a.size * 1.3:
                cut.append(cur)
                cur = []
        # a short batch (a structure's tail, or a small structure between two of --alone entries) would pay a batch's
        # whole start for a few entries: it joins the batch before it, the two split evenly where together they would
        # pass the largest batch
        joined = []
        for c in cut:
            if joined and len(c) < a.size * a.min / 2:
                both = joined.pop() + c
                joined += [both[:len(both) // 2], both[len(both) // 2:]] if len(both) > a.size * 1.3 else [both]
            else:
                joined.append(c)
        cut = joined
        for cur in cut:
            k += 1
            b = f"{PREFIX[p]}-{k}"
            with open(os.path.join(HELD, "batches", f"{b}.txt"), "w", encoding="utf-8") as fh:
                fh.write("\n".join(x["entry_id"] for x in cur) + "\n")
            lines.append([b, p, str(len(cur)), ",".join(dict.fromkeys(x["structure"] for x in cur))])
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
    # An identifier that many of the platform's entries share (Zid's routes all hold "$storeId") leads nowhere.
    df = collections.Counter()
    es = entries(platform)
    for e in es:
        df.update({t.casefold() for t in TOKEN.findall(e["text"])})
    common = {t for t, n in df.items() if n > max(25, len(es) // 50)}
    # Each lead's cell on this platform: what it holds now, so an agent sees where a placement would change a cell.
    state = {}
    for r in rows(os.path.join(MODEL, "merged", "cells.tsv")):
        if r["platform"] == platform:
            state[r["cap_id"]] = (r.get("placed_as") or "shows") if r["held"] == "statements" else "holds nothing"
    # A term many of the platform's entries hold in their values leads nowhere either ("merchant", "available in").
    vals = [" " + fold(values_of(e["text"])) + " " for e in es]
    for t in list(terms):
        if sum(1 for v in vals if f" {t} " in v) > max(25, len(es) // 50):
            del terms[t]
    # Leads by a capability's own name: the words it shares with the entry's values, each weighted by how few names hold it.
    bag = {c: set(name_words(n)) for c, n in names.items()}
    df_w = collections.Counter(w for b in bag.values() for w in b)
    return by_tok, terms, names, common, state, (bag, df_w)


STOP_WORDS = set("the a an of and or to in on for its it is by with as from at be are this that these their your you our "
                 "store stores setting settings page pages list manage management admin dashboard option options general "
                 "new view edit create".split()) | {"و", "في", "من", "على", "الى", "إلى", "عن", "مع", "اعدادات", "إعدادات",
                                                    "صفحة", "إدارة", "ادارة", "قائمة", "عرض", "تعديل", "انشاء", "إنشاء"}


def name_words(s):
    """A name's or a value's words, folded: an English word without its plural; an Arabic one without its article, the
    conjunction or preposition joined to it, and a feminine plural (والتقييمات and التقييم are one word)."""
    out = []
    for w in re.findall(r"[a-z]+|[\u0600-\u06ff]+", fold(s)):
        if w in STOP_WORDS:
            continue
        if w[0].isascii():
            if len(w) < 3:
                continue
            w = re.sub(r"ies$", "y", w)
            w = re.sub(r"(?<!s)s$", "", w)
        else:
            w = re.sub(r"^(?:وال|بال|فال|كال|لل|ال)", "", w)
            if len(w) > 4:
                w = re.sub(r"ات$", "", w)
            if len(w) < 3 or w in STOP_WORDS:
                continue
        out.append(w)
    return out


ID_FIELDS = {"path", "pagekey", "id", "parentid", "key", "route", "url", "href", "module", "slug", "gid", "handle"}
PATH_FIELDS = {"path", "route", "key"}


def values_of(text):
    """An entry's values, without its field names, identifier fields or identifiers: what its own words say. The plans an
    entry is offered on (Zid's `available_in`, `package_restrictions`) are its scope, not its thing, and are left out."""
    keep = []
    text = re.sub(r"(?:^|; )(?:available_in|package_restrictions): (?:\{[^}]*\}|\[[^\]]*\])", "", text)
    for part in text.split(";"):
        k, sep, v = part.partition(":")
        if sep and re.fullmatch(r"\s*[\w .-]{1,40}", k):
            if k.strip().casefold() in PATH_FIELDS:
                # a route's path is the platform's own words for its place: its segments, without parameters (:id, $storeId)
                keep.append(re.sub(r"[/._-]+", " ", re.sub(r"[:$][\w-]+", " ", v)))
                continue
            if k.strip().casefold() in ID_FIELDS:
                continue
            part = v
        keep.append(TOKEN.sub(" ", part))
    return " ".join(keep)


def candidates(e, idx):
    by_tok, terms, names, common, state, (bag, df_w) = idx
    score = collections.Counter()
    why = collections.defaultdict(set)
    for t in set(TOKEN.findall(e["text"])):
        cs = by_tok.get(t.casefold(), ())
        if t.casefold() in common or len(cs) > 3:
            continue
        for c in cs:
            score[c] += 2
            why[c].add(t)
    ft = " " + fold(values_of(e["text"])) + " "
    for t, cs in terms.items():
        if len(cs) > 2:          # a term several capabilities share ("products", "settings") leads nowhere
            continue
        if f" {t} " in ft or (len(t) > 8 and t in ft):
            for c in cs:
                score[c] += 1
                why[c].add(t)
    # ties break by the capability's id, so the leads print in the same order on every run (a set's order varies)
    out = [(c, sorted(why[c])[:3]) for c in sorted(score, key=lambda c: (-score[c], c))[:3]]
    # by a capability's own name, up to two more, the first whose cell holds nothing among them where one scores near the top
    ws = set(name_words(values_of(e["text"])))
    n = len(bag)
    by_name = {c: sum(math.log(n / df_w[w]) for w in ws & b) for c, b in bag.items() if ws & b}
    ranked = [c for c in sorted(by_name, key=lambda c: (-by_name[c], c)) if by_name[c] >= 6 and c not in score]
    pick = ranked[:1]
    nothing = [c for c in ranked[1:10] if state.get(c) == "holds nothing" and by_name[c] >= 0.5 * by_name[ranked[0]]]
    pick += nothing[:1] or ranked[1:2]
    out += [(c, ["name: " + ", ".join(sorted(ws & bag[c])[:3])]) for c in pick]
    return out


def cmd_cells(a):
    """Each named capability's cell on the platform, compact: its name, parent and note, what its cell holds and places,
    its terms and reading, and its evidence rows' reasons. What a placement needs to see of a lead, in one call."""
    caps = {r["cap_id"]: r for r in rows(os.path.join(MODEL, "merged", "capabilities.tsv"))}
    cells = {r["cap_id"]: r for r in rows(os.path.join(MODEL, "merged", "cells.tsv")) if r["platform"] == a.platform}
    ev = collections.defaultdict(list)
    for r in rows(os.path.join(MODEL, "merged", "evidence.tsv")):
        if r["platform"] == a.platform:
            ev[r["cap_id"]].append(r)
    for c in a.cap_ids:
        r = caps.get(c)
        if not r:
            print(f"{c}: no capability of the model")
            continue
        print(f"{c} [{r['domain']}] {clip(r['capability'], 200)} | parent {r.get('parent') or '-'}")
        print(f"   note: {clip(r.get('note', ''), a.width)}")
        cell = cells.get(c)
        if not cell:
            print(f"   {a.platform}: no cell")
            continue
        held = "held" if cell["held"] == "statements" else "holds nothing"
        print(f"   {a.platform}: {held}; placed {cell.get('placed_as') or '-'}; terms: {clip(cell.get('terms', ''), 300)}")
        print(f"   reading: {clip(cell.get('reading', ''), a.width)}")
        es = ev.get(c, [])
        if es:
            n = collections.Counter(e["supports"] for e in es)
            print(f"   evidence, {len(es)} rows ({', '.join(f'{k} {v}' for k, v in sorted(n.items()))}): "
                  + "; ".join(clip(e["why"], 90) for e in es[: a.rows]) + ("; …" if len(es) > a.rows else ""))


# Bundle route structures: an entry stands for every item with its app and path (the brief's known case), so `show`
# prints them, with the archive record of the bundle each one is in, and an agent needs no search to find either.
ROUTE_ITEMS = {("salla", "dashboard-app-routes"), ("salla", "portal-app-routes")}


def route_items(platform, structure, cache={}):
    """{(app, path, parent): [(line, keys, has condition, record, path source)]} for a bundle route structure's items, each with the
    record `raw/runs/<run>/fetch.warc.gz@<offset>` of the bundle file it was read from, by the structure's runs' fetch.cdx."""
    if (platform, structure) in cache:
        return cache[(platform, structure)]
    repo, root, sub = REPOS[platform]
    base = folder(platform, structure)
    out = collections.defaultdict(list)
    for f in sorted(glob.glob(os.path.join(base, "*", "items.jsonl"))):
        meta = json.load(open(os.path.join(os.path.dirname(f), "meta.json"), encoding="utf-8"))
        uris = {}
        for run in meta.get("runs") or []:
            cdx = os.path.join(root, "raw", "runs", run, "fetch.cdx")
            if not os.path.exists(cdx):
                continue
            for l in open(cdx, encoding="utf-8", errors="replace"):
                g = l.split()
                if len(g) > 8 and g[8].isdigit():
                    uris.setdefault(g[0], f"raw/runs/{run}/fetch.warc.gz@{g[8]}")
        its = [json.loads(l) for l in open(f, encoding="utf-8")]
        at = {d.get("position"): d for d in its}
        for i, d in enumerate(its, 1):
            app, ver, fn = d.get("app") or "", d.get("version") or "", d.get("file") or ""
            rec = next((r for u, r in uris.items() if u.endswith("/" + fn) and f"/{app}/{ver}/" in u), "") or \
                next((r for u, r in uris.items() if u.endswith("/" + fn)), "")
            # an item under a parent renders as `parent: <the parent's path>`, or its position where it has none
            par = d.get("parent")
            if par is not None:
                par = (at.get(par) or {}).get("path") or str(par)
            out[(app, d.get("path"), par)].append((i, ",".join(d.get("keys") or []) or "none", "condition" in d, rec,
                                                   d.get("path_source") or ""))
    cache[(platform, structure)] = out
    return out


def bundle_code(platform, rec, path_source, keys, chars, cache={}):
    """The bundle's code at the places an object literal gives `path` the item's own expression and, near it, the
    item's own other keys (its `element`, `children`, `redirect`): up to two, a quarter of `chars` before and the rest
    after, so the route's element, guard or redirect shows beside its path. Where no place holds its keys, the first."""
    repo, root, sub = REPOS[platform]
    if rec not in cache:
        warc, off = rec.rsplit("@", 1)
        import warc_text
        body = warc_text.read_record(os.path.join(root, warc), int(off))[-1]
        cache[rec] = body.decode("utf-8", "replace") if isinstance(body, bytes) else str(body)
    text = cache[rec]
    near = re.compile(r"(?<![\w$])(?:" + "|".join(re.escape(k) for k in keys) + r")\s*:") if keys else None
    hits = [m.start() for m in re.finditer(r"path\s*:\s*" + re.escape(path_source), text)]
    good = [h for h in hits if near and near.search(text[max(0, h - 200): h + 300])]
    return [text[max(0, h - chars // 4): h + chars].replace("\n", " ") for h in (good or hits[:1])[:2]]


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
            # the meta of a label the entries are read under, where the structure has several (the changelog's @posts,
            # not its @feed: SH-34 to SH-38)
            labs = {l.strip() for x in es if x["structure"] == e["structure"] for l in x["labels"].split(",") if l.strip()}
            ms = sorted(glob.glob(os.path.join(folder(a.platform, e["structure"]), "**", "meta.json"), recursive=True))
            ms = [m for m in ms if os.path.basename(os.path.dirname(m)) in labs] or ms
            for m in ms[:1]:
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
            if (a.platform, e["structure"]) in ROUTE_ITEMS:
                m = re.match(r"app: ([^;]+); path: (.*?)(?:; parent: (.*))?$", e["text"])
                its = route_items(a.platform, e["structure"]).get((m.group(1).strip(), m.group(2).strip(),
                                                                    m.group(3).strip() if m.group(3) else None)) if m else None
                if its:
                    recs = sorted({r for _, _, _, r, _ in its if r})
                    print("       items: " + ", ".join(f"line {n} (keys {k}{'; condition' if c else ''})" for n, k, c, _, _ in its)
                          + ("; bundle " + ", ".join(recs) if recs else ""))
                    if a.code:
                        shown = set()
                        for n, k, c, r, src in its:
                            if k != "none" and r and src:
                                for snip in bundle_code(a.platform, r, src, k.split(","), a.code):
                                    if snip not in shown:
                                        shown.add(snip)
                                        print(f"       code, line {n}: {snip}")
            if idx:
                cs = candidates(e, idx)
                if cs:
                    print("       leads: " + "; ".join(f"{c} {clip(idx[2].get(c, ''), 50)} [cell: {idx[4].get(c, 'none')}] (by {', '.join(w)})" for c, w in cs))


# earlier: an entry's own keys, looked up in the platform's other batches' readings and terms
EARLIER_PATH = re.compile(r"(?:href|path|url|link|route_path|to): (/[^\s;,\]}]*)")
# a key is a whole value: an ARIA name's first word ('Add' of 'Add your first product') is no key (SH-1)
EARLIER_NAME = re.compile(r"(?:^|; |\{)(?:route|name|key|id|app|slug): ([\w@./,:-]{3,})(?=\s*(?:[;}\]|]|$))|(?:^|; |\{)(?:title|label): ([a-z][\w-]*(?:[._][\w-]+)+)(?=[;}]|$)")
EARLIER_KEY = re.compile(r"\[([\w-]+(?:[/#.][\w.-]+)+)\]")
EARLIER_LABEL = re.compile(r"(?:^|; |\{)(?:section|label|title|heading|text|name|aria_label|en|ar): ([^;\[\]{}()]{3,80}?)\s*(?=[;(\[{}]|$)")


EARLIER_GENERIC = {"value", "values", "type", "enabled", "status", "true", "false", "default", "data", "items", "item",
                   "name", "label", "title", "text", "list", "form", "field", "option", "options", "query", "action",
                   "market", "markets", "limit", "limits", "scopes", "statuses", "updates", "community", "partners",
                   "actions", "settings", "notifications", "general", "checkout", "orders", "products", "customers",
                   "method", "description", "hours", "window", "days", "duration", "types", "content_title", "sales"}


def earlier_keys(text):
    keys = []
    for m in EARLIER_PATH.finditer(text):
        v = m.group(1).split("?")[0]
        if len(v) > 1:
            keys.append(("path", v.rstrip("/") or "/"))
        # a store's admin link (/store/<handle>/orders) is the router's route 'at orders' (SH-2)
        a = re.match(r"/store/[^/]+/(.+)$", v)
        if a and a.group(1).strip("/"):
            keys.append(("admin", a.group(1).strip("/")))
    # a control's own field name (value, type, enabled) names nothing of the entry's (SA-49)
    # and an ARIA name that is one capitalized word (Search, Recommended) is a label, which says too little (SH-2)
    keys += [("name", m.group(1) or m.group(2)) for m in EARLIER_NAME.finditer(text)
             if not (m.group(1) or m.group(2)).isdigit() and (m.group(1) or m.group(2)).lower() not in EARLIER_GENERIC
             and not (m.group(1) and re.fullmatch(r"[A-Z][a-z]+", m.group(1)) and "name:" in m.group(0))]
    keys += [("key", m.group(1)) for m in EARLIER_KEY.finditer(text)]
    # a one-word label (Orders, الطلبات) is cited for too many things to say anything; its address does
    keys += [("label", m.group(1).strip()) for m in EARLIER_LABEL.finditer(text) if len(m.group(1).split()) >= 2]
    seen, out = set(), []
    for k in keys:
        if k[1] not in seen and len(k[1]) >= 3:
            seen.add(k[1]); out.append(k)
    return out[:6]


def earlier_pattern(kind, v):
    if kind == "path":
        # the address alone, or with a host before it; never as the start of a longer address
        return re.compile(re.escape(v) + r"(?![\w/-])")
    if kind == "label":
        return re.compile(r"['‘“]" + re.escape(v) + r"(?:['’”]| \(| /)|;" + re.escape(v) + ";")
    if kind == "admin":
        return re.compile(r"(?<![\w-])at " + re.escape(v) + r"(?![\w/:*-])")
    # a route's id whole: balance:root is never matched inside balance:root:statements (SH-8)
    return re.compile(r"(?<![\w.:-])" + re.escape(v) + r"(?![\w:-])")


def cmd_earlier(a):
    """For each entry of a batch: the lines of the platform's other batches whose reading or terms cite one of the
    entry's own keys (its address, route or app name, translation key, or its label quoted), grouped by capability
    and support. A batch whose notes hold no coordinator's check is marked unchecked."""
    by = {e["entry_id"]: e for e in entries(a.platform)}
    lines = []
    for path in sorted(glob.glob(os.path.join(HELD, a.platform, "placements-*.tsv"))):
        b = os.path.basename(path)[len("placements-"):-len(".tsv")]
        if b == a.batch:
            continue
        notes = os.path.join(HELD, a.platform, f"notes-{b}.md")
        checked = os.path.exists(notes) and "## The coordinator's check" in open(notes, encoding="utf-8").read()
        for n, r in enumerate(rows(path), 2):
            # terms as `;term;`, so a label is found as a whole term as well as quoted in a reading (SH-70)
            lines.append((b if checked else b + "?", n, r.get("cap_id") or r.get("placement", ""),
                          r.get("supports", ""), (r.get("reading") or "") + " ;" + ";".join(t.strip() for t in (r.get("terms") or "").split(";")) + ";"))
    # an entry's twins: the platform's other entries at the same place in their own source (a page's pointer), such as
    # one pricing page in two languages, and the lines their batches gave them (SH-72)
    placed_at = collections.defaultdict(list)
    for path in sorted(glob.glob(os.path.join(HELD, a.platform, "placements-*.tsv"))):
        b = os.path.basename(path)[len("placements-"):-len(".tsv")]
        if b == a.batch:
            continue
        for n, r in enumerate(rows(path), 2):
            for x in (r.get("entry_id") or "").split(";"):
                placed_at[x.strip()].append((b, n, r.get("cap_id") or r.get("placement", ""), r.get("supports", "")))
    at_ptr = collections.defaultdict(list)
    for e in by.values():
        m = re.search(r"pointer (\S+)", e.get("locator") or "")
        if m:
            at_ptr[(e["structure"], m.group(1))].append(e["entry_id"])
    # and by a feature's name key (`card_rates_short`) under the same `within`, on pages laid out differently (SH-73)
    def name_key(e):
        m = re.search(r"(?:^|; )name: ([\w.-]+)", e["text"])
        w = re.search(r"(?:^|; )within: ([^;]+)", e["text"])
        return (e["structure"], w.group(1).strip() if w else "", m.group(1)) if m and "_" in m.group(1) else None
    at_name = collections.defaultdict(list)
    for e in by.values():
        k = name_key(e)
        if k:
            at_name[k].append(e["entry_id"])
    for i, eid in enumerate(batch_ids(a.batch), 1):
        if eid not in by or (a.__dict__.get("from") and i < a.__dict__["from"]) or (a.to and i > a.to):
            continue
        keys = earlier_keys(by[eid]["text"])
        found = []
        m = re.search(r"pointer (\S+)", by[eid].get("locator") or "")
        own = re.search(r"(?:^|; )name: ([\w.-]+)", by[eid]["text"])
        twins = []
        for twin in (at_ptr.get((by[eid]["structure"], m.group(1)), []) if m else []):
            tn = re.search(r"(?:^|; )name: ([\w.-]+)", by[twin]["text"])
            # the same place is the same thing only where a name key, where either has one, agrees: pages laid out
            # differently put other features at one place (SH-73)
            if twin != eid and (not (own or tn) or (own and tn and own.group(1) == tn.group(1))):
                twins.append((twin, "at the same place"))
        if own:
            twins += [(t, f"by its name {own.group(1)}") for t in at_name.get(name_key(by[eid]), []) if t != eid and t not in dict(twins)]
        for twin, how in [t for t in twins if placed_at.get(t[0])][:6]:
            # with the twin's own words, since one name key can state another kind of thing (SH-74: eg's and sa's
            # card_rates_short state the third-party fee, ae-ar's the card rate)
            words = clip(re.sub(r"^(?:(?:within|list): [^;]*; )+", "", by[twin]["text"]), 90)
            # and which rates a plan summary holds, which its line follows (SH-75)
            cr = re.search(r"card_rates: \{([^}]*)\}", by[twin]["text"])
            if cr:
                words += " | card_rates: " + ", ".join(k for k in re.findall(r"(?:^|; )(\w+):", cr.group(1)) if k != "lowest")
            found.append(f"   twin {twin} {how} [{words}]: " + "; ".join(f"{cap} {sup} ({b}:{n})" for b, n, cap, sup in placed_at[twin][:4]))
        for kind, v in keys:
            pat = earlier_pattern(kind, v)
            g = collections.OrderedDict()
            for b, n, cap, sup, txt in lines:
                if pat.search(txt):
                    g.setdefault((cap, sup), []).append(f"{b}:{n}")
            if g:
                parts = [f"{cap} {sup} ×{len(refs)} ({', '.join(refs[:3])}{' …' if len(refs) > 3 else ''})"
                         for (cap, sup), refs in sorted(g.items(), key=lambda x: -len(x[1]))[:a.groups]]
                found.append(f"   {kind} {v}: " + "; ".join(parts))
        head = f"{i} {eid}"
        if found:
            print(head); print("\n".join(found))
        else:
            print(f"{head}  (no earlier line cites {', '.join(v for _, v in keys) or 'a key of it'})")


MAKER_CUE = (r"\bwe['’](?:ve|re|ll)\b|\bwe (?:have|are|built|made|launched|released|introduced|upgraded|updated|improved|"
             r"added|shipped|rolled)\b|\bour\b|\bfirst-party\b")


def cmd_makers(a):
    """The platform's held entries whose own words may name it as the maker of a thing (the ruling after SH-37): each
    entry that holds the name in one sentence with a maker's cue ('we’ve', 'our', 'first-party', 'from <brand>',
    'by <brand>', a company of its group), with that sentence and the lines its batch gave the entry. A batch finds an
    app's maker statement in one call (SH-55). A cue is a lead: 'our APIs' beside an app's name doesn't make the app."""
    cue = re.compile(MAKER_CUE + rf"|\b(?:from|by) (?:{BRAND[a.platform]})\b"
                     + "".join("|" + re.escape(g) for g in GROUP.get(a.platform, [])), re.I)
    placed = collections.defaultdict(list)
    for path in sorted(glob.glob(os.path.join(HELD, a.platform, "placements-*.tsv"))):
        b = os.path.basename(path)[len("placements-"):-len(".tsv")]
        for n, r in enumerate(rows(path), 2):
            for x in (r.get("entry_id") or "").split(";"):
                placed[x.strip()].append(f"{r.get('cap_id') or r.get('placement', '')} {r.get('supports', '')} ({b}:{n})")
    es = entries(a.platform)
    for name in a.names:
        nm = re.compile(r"(?<!\w)" + re.escape(name) + r"(?!\w)", re.I)
        hits = []
        for e in es:
            if not nm.search(e["text"]):
                continue
            # the entry's sentences, and its fields
            for part in re.split(r"(?<=[.!?])\s+|\s*;\s*(?=[\w.*]+: )", e["text"]):
                if nm.search(part) and cue.search(part):
                    hits.append((e, part.strip()))
                    break
        print(f"{name}: {len(hits)} entr{'y' if len(hits) == 1 else 'ies'} name it in a sentence with a maker's cue")
        for e, part in hits[:a.limit]:
            print(f"   {e['entry_id']} [{e['structure']}] {clip(part, 260)}")
            if placed.get(e["entry_id"]):
                print(f"      lines: {'; '.join(placed[e['entry_id']][:4])}")


PARTNER = re.compile(r"collaborator|partner-api|app-install|stores-access-requests|portal-app-scopes", re.I)
# The companies of each platform's group, as its CM-ACC-002 cell names them: a group company is never a filler, and a
# line that names one as a third party is read again (the dry run's review, R1).
GROUP = {"bigcommerce": ["Commerce.com", "Commerce Software", "Feedonomics", "Makeswift"],
         "shopify": ["Shopify Inc", "Shopify Technology", "Shopify Commerce Singapore", "Shopify International"],
         "salla": ["شركة منصة سلة", "شركة تطبيق سلة", "شركة سلة القابضة", "Salla Holding"],
         "woocommerce": ["WooCommerce, Inc", "WooCommerce Ireland", "Automattic"],
         "zid": ["شركة القدرة التقنية", "Al-Qudrah Al-Taqniyah", "Zid Egypt", "زد مصر"]}
BRAND = {"shopify": "Shopify", "salla": "Salla", "zid": "Zid", "bigcommerce": "BigCommerce", "woocommerce": "WooCommerce|Woo"}
# a plan's or a provider's mark that a thing is included: scope, or a statement of the marked thing, never a quality
MARKS = {"✔", "✓", "✔️", "yes", "available", "included", "true", "نعم", "متاح", "متوفر", "مشمول"}
# a word's own marks (Arabic's vowel marks, as in 'مجاناً') are part of it: a quote never opens right after one (SA-48)
QUOTE = re.compile(r"(?<![\w\u064B-\u065F\u0670])['‘]([^'’\n]{8,}?)['’](?![\w\u064B-\u065F\u0670])")


def quote_norm(s):
    return fold(s.replace("’", "'").replace("‘", "'"))


def structure_text(platform, structure, cache={}):
    """The text a reading may quote besides its entry: the structure's own files, and the page or answer its meta.json
    names as its source (with the step's text beside an HTML or ARIA capture)."""
    if (platform, structure) in cache:
        return cache[(platform, structure)]
    repo, root, sub = REPOS[platform]
    base = folder(platform, structure)
    paths = [f for f in glob.glob(os.path.join(base, "**", "*"), recursive=True)
             if os.path.isfile(f) and (os.path.basename(f).startswith("source") or f.endswith((".jsonl", ".txt")))]
    titles = []
    for m in glob.glob(os.path.join(base, "**", "meta.json"), recursive=True):
        try:
            src = json.load(open(m, encoding="utf-8")).get("source") or {}
        except Exception:
            continue
        if isinstance(src, dict) and isinstance(src.get("title"), str):
            titles.append(quote_norm(src["title"]))     # the page's own title, as the capture held it (SH-1)
        for k in ("held_as", "answer"):
            v = src.get(k) if isinstance(src, dict) else None
            if isinstance(v, str):
                paths.append(os.path.join(root, v))
                paths.append(os.path.join(root, re.sub(r"\.(?:frame-\d+\.)?(?:html|aria\.yaml)$", ".text.txt", v)))
    out = []
    for f in dict.fromkeys(paths):
        if os.path.isfile(f) and os.path.getsize(f) < 30_000_000:
            out.append(quote_norm(open(f, encoding="utf-8", errors="replace").read()))
    cache[(platform, structure)] = "\n".join(out + titles)
    return cache[(platform, structure)]


def run_text(platform, cache={}):
    """Every page text the platform's runs hold (steps/*.text.txt), where a reading's quote from a run step is found."""
    if platform not in cache:
        repo, root, sub = REPOS[platform]
        fs = glob.glob(os.path.join(root, sub, "raw", "runs", "*", "steps", "*.text.txt"))
        if platform in ("zid", "bigcommerce", "woocommerce"):     # their answers are tens of megabytes; Shopify's 1.7 GB
            fs += [f for f in glob.glob(os.path.join(root, sub, "raw", "runs", "*", "answers", "**", "*.json"), recursive=True) if os.path.isfile(f)]
        cache[platform] = "\n".join(quote_norm(open(f, encoding="utf-8", errors="replace").read()) for f in fs)
    return cache[platform]


RELEASE_ROOTS = {"woocommerce": "/home/user/woocommerce-release/11.2.1/woocommerce"}


def whole_text(platform, e, cache={}):
    """The entry's words as its source holds them, where the build cut a long value: its row, or its item's JSON line,
    at the locator entries.tsv gives (`line N`). The terms and filler tests read it beside the entry's text."""
    k = (platform, e["entry_id"])
    if k not in cache:
        repo, root, sub = REPOS[platform]
        out = e["text"]
        m = re.match(r"line (\d+)", e.get("locator") or "")
        path = (e.get("source") or "").split(":", 1)[-1]
        f = os.path.normpath(os.path.join(root, path))
        if m and f.startswith(os.path.normpath(root)) and os.path.isfile(f):
            with open(f, encoding="utf-8", errors="replace") as fh:
                for i, l in enumerate(fh, 1):
                    if i == int(m.group(1)):
                        out = e["text"] + " " + l
                        break
        cache[k] = out
    return cache[k]
# a structure's label folder holds an @ (`ui-partners-portal-layout@prod`, `partner@en`), so a path segment may too;
# jsonl is tried before json, or items.jsonl reads as items.json and the file is never opened (SA-12's notes)
CITED_FILE = re.compile(r"(?:woocommerce-11\.2\.1:)?((?:[\w.@-]+/)+[\w.@-]+\.(?:jsonl|json|js|php|txt|tsv|html|yaml|md))(?![\w])")
STATEMENT_ID = re.compile(r"\b(SH|SA|WC|ZD|BC)-S-\d{4}\b")
CITED_RECORD = re.compile(r"((?:[\w.-]+/)*[\w.-]+\.warc\.gz)@(\d+)")


def cited_text(platform, reading, cache={}):
    """The text of what a reading cites by name: a held file by its path (from the platform's folder, its structures, or
    the WooCommerce release), and a statement by its id (the concern map's statements, which the model cites)."""
    from class_slice import citable, key, PREFIX
    repo, root, sub = REPOS[platform]
    bases = [os.path.join(root, sub), os.path.join(root, sub, "structures"), os.path.join(root, sub, "raw", "runs"), root]
    if platform in RELEASE_ROOTS:
        bases.append(RELEASE_ROOTS[platform])
    out = []
    for m in CITED_FILE.finditer(reading):
        rel = m.group(1)
        for b in bases:
            f = os.path.normpath(os.path.join(b, rel))
            if f.startswith(os.path.normpath(b)) and os.path.isfile(f) and os.path.getsize(f) < 30_000_000:
                if f not in cache:
                    cache[f] = quote_norm(open(f, encoding="utf-8", errors="replace").read())
                out.append(cache[f])
                break
    # an archive record the reading cites as <archive>@<offset> (method/warc_text.py), its body and its text
    for m in CITED_RECORD.finditer(reading):
        for b in bases:
            f = os.path.normpath(os.path.join(b, m.group(1)))
            if f.startswith(os.path.normpath(b)) and os.path.isfile(f):
                k = (f, int(m.group(2)))
                if k not in cache:
                    try:
                        import warc_text
                        _, _, headers, body = warc_text.read_record(f, int(m.group(2)))
                        t = body.decode("utf-8", "replace")
                        cache[k] = quote_norm(t) + "\n" + quote_norm(warc_text.html_text(t))
                    except Exception:
                        cache[k] = ""
                out.append(cache[k])
                break
    ids = {m.group(0) for m in STATEMENT_ID.finditer(reading)}
    if ids:
        if "statements" not in cache:
            st = {}
            for p in PREFIX:
                for x in citable(p):
                    sid = key(x).rsplit("/", 1)[-1]
                    st[sid] = quote_norm((x.get("identifier") or "") + " " + (x.get("statement") or ""))
            cache["statements"] = st
        out += [cache["statements"][i] for i in sorted(ids) if i in cache["statements"]]
    # a held entry by its id, as a reading cites another batch's maker statement or twin (SH-13, SH-40)
    eids = set(re.findall(r"\b[A-Z]{2}-E-[0-9a-f]{8}\b", reading))
    if eids:
        if ("entries", platform) not in cache:
            cache[("entries", platform)] = {e["entry_id"]: e for e in entries(platform)}
        by = cache[("entries", platform)]
        for i in sorted(eids):
            if i in by:
                out.append(quote_norm(by[i]["text"]))
                out.append(quote_norm(whole_text(platform, by[i])))
    return "\n".join(out)


def cmd_check(a):
    problems, notes = [], []
    ids = batch_ids(a.batch)
    es = {e["entry_id"]: e for e in entries(a.platform)}
    order = {i: n for n, i in enumerate(ids)}
    caps = {r["cap_id"]: r for r in rows(os.path.join(MODEL, "merged", "capabilities.tsv"))}
    cap_names = {fold(r["capability"].split(":")[0].split("(")[0]) for r in caps.values()} | {fold(c) for c in caps}
    new_tsv = os.path.join(MODEL, "held", "new.tsv")
    decided = {(r["platform"], fold(r["name"])) for r in rows(new_tsv) if r.get("decision")} if os.path.exists(new_tsv) else set()
    cells = {r["cap_id"]: r for r in rows(os.path.join(MODEL, "merged", "cells.tsv")) if r["platform"] == a.platform}
    changes = collections.defaultdict(list)
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
        # the scripts read with no quoting, but a spreadsheet or GitHub's table view takes a field that opens with a
        # double quote as quoted, so the files hold none: a reading quotes with ' or “ ”
        if '"' in l:
            problems.append(f"{w}: holds a double quote (\"), which this file can't carry: quote with ' or “ ”"); continue
        if len(f) != len(P_HEAD):
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
                # a second line on the same capability is for another thing the entry names with its own condition
                # (a post's payment methods, each in its own countries: SH-34), never the same scope and filler again
                if x in seen and any((c == r["cap_id"] and (sc, fl) == (r["scope"], r["filler"])) or pl == "out" for c, pl, sc, fl in seen[x]):
                    problems.append(f"{w}: {x} placed again on the same capability with the same scope and filler, or placed out too")
        elif r["placement"] == "new":
            m = re.match(r"^new:(\S.*\S|\S)$", r["cap_id"])
            if not m:
                problems.append(f"{w}: a new capability is named in cap_id as new:<its name, in the platform's words>")
            else:
                nm = m.group(1)
                # a new thing the coordinator has decided (held/new.tsv) may have become the capability of that name
                if (fold(nm) in cap_names or re.match(r"^CM-[A-Z]{3}-\d{3}$", nm)) and (a.platform, fold(nm)) not in decided:
                    problems.append(f"{w}: new:{nm} is an existing capability's name or id: place it there")
                new_names[fold(nm)].append(nm)
            if not ss or any(x not in SUPPORTS for x in ss):
                problems.append(f"{w}: a new thing says what the entry supports")
            for x in ok:
                if x in seen and any(c == r["cap_id"] or pl == "out" for c, pl, _, _ in seen[x]):
                    problems.append(f"{w}: {x} placed again as the same new thing, or placed out too")
        elif r["placement"] == "out":
            if any(r[k].strip() for k in ("cap_id", "supports", "scope", "terms", "filler", "quality")):
                problems.append(f"{w}: out names no capability, supports nothing, and has no scope, terms, filler or quality")
            for x in ok:
                if x in seen:
                    problems.append(f"{w}: {x} placed again")
        for t in [x.strip() for x in r["terms"].split(";") if x.strip()]:
            if not all(fold(t) in fold(es[x]["text"]) or fold(t) in fold(whole_text(a.platform, es[x])) for x in ok if x in es):
                problems.append(f"{w}: term {t!r} is not in the text of each of its entries")
        for fl in [x.strip() for x in r["filler"].split(";") if x.strip()]:
            named = re.sub(r"^(?:the )?law of ", "", re.sub(r"\s*\([^)]*\)", "", fl), flags=re.I).strip()
            # as written, or without a parenthesis of the filler's own: a parenthesis inside the source's words
            # ('United States-Mexico-Canada (USMCA) free trade agreement') stays in (SH-40)
            if not all(any(fold(n) in fold(es[x]["text"]) or fold(n) in fold(whole_text(a.platform, es[x])) for n in (named, fl))
                       for x in ok if x in es):
                problems.append(f"{w}: filler {fl!r} is not named in the text of each of its entries: a party known only from a source goes in reading")
            if any(fold(g) in fold(fl) for g in GROUP.get(a.platform, ())):
                problems.append(f"{w}: filler {fl!r} is a company of the platform's group (CM-ACC-002): never a filler")
        for q in [x.strip() for x in r["quality"].split(";") if x.strip()]:
            what, _, val = q.partition(":")
            pieces = [fold(re.sub(r"\s*\([^)]*\)", "", x)).strip(" .") for x in (val or what).split(",")]
            if pieces and all(x in MARKS for x in pieces if x) and any(pieces):
                problems.append(f"{w}: quality {q!r} is a mark of inclusion: it is the line's scope, or a statement of the marked thing, never a quality")
        if ok and ok[0] in es:
            e0 = es[ok[0]]
            for qt in QUOTE.findall(r["reading"]):
                qn = quote_norm(qt)
                if "..." in qt or "…" in qt:
                    qn = max((quote_norm(x) for x in re.split(r"\.\.\.|…", qt)), key=len)
                if (qn and qn not in quote_norm(e0["text"]) and qn not in structure_text(a.platform, e0["structure"])
                        and qn not in run_text(a.platform) and qn not in cited_text(a.platform, r["reading"])):
                    notes.append(f"line {i}: the quote '{clip(qt, 70)}' is found nowhere held, in the entry, its structure's sources, the platform's run pages, or a file or statement the reading cites: copy it exactly")
            if any(x in ss for x in ("extension-point", "outside")) and any(fold(g) in fold(e0["text"]) for g in GROUP.get(a.platform, ())):
                notes.append(f"line {i}: {'/'.join(ss)} on an entry that names a company of the platform's group: own-service? (rule 4)")
            # the line's own thing, by its terms: a changelog post names the brand's products in passing (SH-34)
            if "core" in ss and re.search(rf"\b(?:{BRAND[a.platform]})\s+[A-Z]\w+", r["terms"] or ""):
                notes.append(f"line {i}: core on a product named with the platform's brand, which names no maker: is it core by what the entry shows? (rule 4)")
            if re.search(r"\w\*(?=[\s;,)]|$)", e0["text"]):
                notes.append(f"line {i}: the entry marks a footnote (*): the footnote is part of the entry (rule 1)")
        if r["placement"] == "capability" and r["cap_id"] in cells:
            c = cells[r["cap_id"]]
            if c["held"] != "statements":
                changes[(r["cap_id"], "holds nothing: becomes held")].append(i)
            for x in ss:
                if x != "shows" and x not in set((c.get("placed_as") or "").split(";")):
                    changes[(r["cap_id"], f"gains {x}")].append(i)
        if not r["reading"].strip():
            problems.append(f"{w}: reading says why, as a reading")
        for x in ok:
            seen[x].append((r["cap_id"], r["placement"], r["scope"], r["filler"]))
        if "own-service" in ss and ok:
            notes.append(f"own-service on {r['cap_id']}: {clip(es.get(ok[0], {}).get('text', ''), 160)}")
        if "core" in ss and ok and PARTNER.search(es.get(ok[0], {}).get("structure", "")):
            notes.append(f"core on a partner's or an app's permission ({es[ok[0]]['structure']}): the dry run's S7 makes it shows")
    # per entry, over all its lines: a new thing with leads; a lead whose cell holds nothing that no line names; an app's
    # embedded page with no CM-APP-007 line; a page index's container
    idx = candidate_index(a.platform)
    caps_of = collections.defaultdict(set)
    lines_of = collections.defaultdict(list)
    for i, l in enumerate(raw[1:], 2):
        f = l.split("\t")
        if len(f) == len(P_HEAD):
            for x in [y.strip() for y in f[0].split(";") if y.strip()]:
                caps_of[x].add(f[2]); lines_of[x].append(i)
    keys = {x: re.search(r"pageKey: ([^;]+)", es[x]["text"]).group(1).strip() for x in ids if x in es and re.search(r"pageKey: ([^;]+)", es[x]["text"])}
    # an entry whose own id, title or path is another entry's parent, within or parentId holds others: a container
    # keyed by the parent's root and its last name, so the same title under another country or store is another container
    held_by = collections.Counter()
    for x in ids:
        if x in es:
            for m in re.finditer(r"(?:^|; )(?:parent|within|parentId): ([^;]+)", es[x]["text"]):
                segs = [g.strip() for g in m.group(1).split(" > ")]
                held_by[(segs[0] if len(segs) > 1 else "", segs[-1])] += 1
    own = {}
    for x in ids:
        if x in es:
            w = re.search(r"(?:^|; )within: ([^;]+)", es[x]["text"])
            root = w.group(1).split(" > ")[0].strip() if w else ""
            for f in ("id", "title", "text", "name", "label", "path"):
                m = re.search(rf"(?:^|; ){f}: ([^;]+)", es[x]["text"])
                if m and held_by.get((root, m.group(1).strip())):
                    own[x] = (root, m.group(1).strip()); break
    # a route whose own path begins other routes' paths, in the same app, holds them too (a section's own route)
    def route(x):
        m = re.search(r"(?:^|; )path: ([^;]+)", es[x]["text"])
        if not m:
            return None
        app = re.search(r"(?:^|; )app: ([^;]+)", es[x]["text"])
        return (app.group(1).strip() if app else "", re.sub(r"^(?:/+|:lang/)", "", m.group(1).strip()).rstrip("/"))
    paths = {x: route(x) for x in ids if x in es}
    under = collections.Counter()
    for rp in paths.values():
        if rp and rp[1]:
            segs = rp[1].split("/")
            for n in range(1, len(segs)):
                under[(rp[0], "/".join(segs[:n]))] += 1
    for x in ids:
        if x not in es or x not in caps_of:
            continue
        e, at = es[x], lines_of[x][0]
        leads = candidates(e, idx)
        if any(c.startswith("new:") for c in caps_of[x]) and leads:
            notes.append(f"line {at}: a new thing whose entry has leads ({', '.join(c for c, _ in leads)}): read their cells first (rule 2)")
        for c, w in leads[:1]:
            if idx[4].get(c) == "holds nothing" and c not in caps_of[x]:
                notes.append(f"line {at}: its first lead {c} ({', '.join(w)}) holds nothing on {a.platform}, and no line names it: is the entry also its thing? (rule 2)")
        if re.search(r"apps/[^;\s]*embedded", e["text"]) and "CM-APP-007" not in caps_of[x]:
            notes.append(f"line {at}: an app's embedded page with no CM-APP-007 line (rule 4)")
        k = keys.get(x)
        if k and any(v.startswith(k + ".") for v in keys.values()):
            notes.append(f"line {at}: pageKey {k} holds other pages: a container (rule 3)")
        elif x in own:
            notes.append(f"line {at}: {own[x][1]}{' (' + own[x][0] + ')' if own[x][0] else ''} holds {held_by[own[x]]} other entries: a container (rule 3)")
        elif paths.get(x) and paths[x][1] and under.get(paths[x], 0) >= 2:
            notes.append(f"line {at}: path {paths[x][1]} begins {under[paths[x]]} other entries' paths: a container (rule 3)")
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
    for (c, what), ls in sorted(changes.items()):
        print(f"CHANGES {c}@{a.platform} {what}, by line{'s' if len(ls) > 1 else ''} {', '.join(map(str, ls))}: read each again")
    for n in notes[:400]:
        print("NOTE", n)
    if len(notes) > 400:
        print(f"NOTE ... and {len(notes) - 400} more")
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
    s = sub.add_parser("batches"); s.add_argument("--size", type=int, default=300)
    s.add_argument("--min", type=float, default=0.5, help="a batch ends where a structure or section ends once it holds this share of --size")
    s.add_argument("--alone", type=int, default=0, help="a structure of this many entries or more starts and ends its own batches")
    s.set_defaults(f=cmd_batches)
    s = sub.add_parser("show"); s.add_argument("--platform", choices=PLATFORMS, required=True)
    s.add_argument("--batch"); s.add_argument("--structure"); s.add_argument("--from", type=int); s.add_argument("--to", type=int)
    s.add_argument("--width", type=int, default=1200); s.add_argument("--meta", action="store_true")
    s.add_argument("--candidates", action="store_true", help="each entry's leads: capabilities whose cited statements share its identifiers, or whose terms it holds")
    s.add_argument("--code", type=int, default=0, help="for a bundle route structure: this many characters of the bundle's code at each item's path, for the items that are more than a path")
    s.set_defaults(f=cmd_show)
    s = sub.add_parser("earlier", help="each entry's keys (address, route or app name, translation key, quoted label) as the platform's other batches' lines cite them")
    s.add_argument("--platform", choices=PLATFORMS, required=True); s.add_argument("--batch", required=True)
    s.add_argument("--from", type=int); s.add_argument("--to", type=int)
    s.add_argument("--groups", type=int, default=3, help="at most this many capability-and-support groups a key")
    s.set_defaults(f=cmd_earlier)
    s = sub.add_parser("makers", help="the held entries that name a thing in one sentence with a maker's cue ('we’ve', 'our', 'from Shopify')")
    s.add_argument("--platform", choices=PLATFORMS, required=True); s.add_argument("names", nargs="+")
    s.add_argument("--limit", type=int, default=8)
    s.set_defaults(f=cmd_makers)
    s = sub.add_parser("cells", help="each named capability's cell on the platform, compact")
    s.add_argument("--platform", choices=PLATFORMS, required=True); s.add_argument("cap_ids", nargs="+")
    s.add_argument("--width", type=int, default=500); s.add_argument("--rows", type=int, default=12)
    s.set_defaults(f=cmd_cells)
    s = sub.add_parser("check"); s.add_argument("--platform", choices=PLATFORMS, required=True)
    s.add_argument("--batch", required=True); s.set_defaults(f=cmd_check)
    a = ap.parse_args()
    a.f(a)


if __name__ == "__main__":
    main()
