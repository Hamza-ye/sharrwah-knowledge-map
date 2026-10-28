"""Write, show and check one root decision's phase C files for S-02 and later subjects: c/<RD>/points.tsv, a row per
variation point (its keys, letters and generality), c/<RD>/answers.tsv, a row per key of a point (what each platform
does on it, its cause and what follows), and notes-c.md. The brief is studies/subjects/<subject>/briefs/C-analysis.md.

Usage: python3 -I method/analysis_edit.py SUBJECT_DIR RD keys VP_ID [--keep] --row VID=KEY[;KEY] ... [--open VID=KEY[;KEY]]
                                                                 [--absent VID=KEY[;KEY]]
       python3 -I method/analysis_edit.py SUBJECT_DIR RD answer VP_ID KEY --cause TAG [--FIELD TEXT ...]
       python3 -I method/analysis_edit.py SUBJECT_DIR RD point VP_ID --coexistence TEXT [--FIELD TEXT ...]
       python3 -I method/analysis_edit.py SUBJECT_DIR RD show VP_ID [--full]
       python3 -I method/analysis_edit.py SUBJECT_DIR RD check [VP_ID ...]
       python3 -I method/analysis_edit.py SUBJECT_DIR RD notes PART TEXT
       python3 -I method/analysis_edit.py SUBJECT_DIR RD batch FILE

keys     gives each answer row of the point its keys (every answer row takes one at least), marks the gap rows that
         ask for a key (--open) and the absent rows that exclude one (--absent), and prints what each platform does on
         each key, with the cause the mechanical tests give. Answer rows of keys no longer given are dropped.
         With --keep, it starts from the point's stored keys, less those of rows no longer there or no longer of
         that form, and the rows named replace what they held: for a point that gained or changed rows.
answer   writes one key's row; flags --cause, --cause-basis, --scopes, --reading, --blocked-by, --follows,
         --expensive, --founder-item, --depends-on, --note. What each platform does comes from the keys.
point    writes the point's row; flags --coexistence, --coexistence-basis, --general, --general-basis, --follows,
         --note.
show     prints the point's keys, what each platform does on each, its answer rows and its point row; with --full,
         also each answer row's basis, scopes, reading, blocked_by and expense, and the point row's bases, never a note.
check    checks the rows of the points named (all the root decision's points without any), and names each key with no
         answer row, each answer row of the point with no key, and each point with no row. Exits 1 on a problem.
notes    appends TEXT to notes-c.md under a heading for PART.
refresh  works out again what each platform does on each key of the points named (all without any), from their
         stored keys, as after a change to this tool.
batch    runs the commands in FILE, one per line as they would follow RD (such as `answer S02-VP-41 'key' --cause ...`),
         under one lock, and says which lines failed.

Each command holds a lock on c/<RD>/ while it reads and writes; files are written whole, to a temporary file first.
What each platform does on a key:
  gives       an answer row of the platform's takes the key
  lacks       an absent row of the platform's is marked as excluding the key
  open        the platform has only gap or not covered rows for the point, or a gap row of its is marked as asking
              for the key
  not stated  the platform has answer or absent rows, none gives or excludes the key, and nothing makes it open
"""
import csv, fcntl, os, re, sys

csv.field_size_limit(10**9)
PLATFORMS = ("salla", "zid", "shopify", "bigcommerce", "woocommerce")
PHEAD = ["vp_id", "keys", "coexistence", "coexistence_basis", "general_variant", "general_basis", "follows", "note"]
AHEAD = ["vp_id", "key", "rows", "gives", "lacks", "open", "not_stated", "cause", "cause_basis", "scopes_compared",
         "cause_reading", "blocked_by", "follows", "expensive_because", "founder_item", "depends_on", "note"]
AFLAGS = {"--cause": "cause", "--cause-basis": "cause_basis", "--scopes": "scopes_compared", "--reading": "cause_reading",
          "--blocked-by": "blocked_by", "--follows": "follows", "--expensive": "expensive_because",
          "--founder-item": "founder_item", "--depends-on": "depends_on", "--note": "note"}
PFLAGS = {"--coexistence": "coexistence", "--coexistence-basis": "coexistence_basis", "--general": "general_variant",
          "--general-basis": "general_basis", "--follows": "follows", "--note": "note"}
CAUSES = ("no difference", "market, named rule", "maturity", "business model", "market, pattern", "vendor choice",
          "unknown")
COMMON = "a commonality, carried as the references carry it"
PER_MARKET = "a variation point bound per market"
FOUNDER = "a decision for the founder, on a recommendation"
BUILD = "left to the build"
OPEN = "kept open as a variation point until evidence settles it"
LETTERS = {"A": "the platform carries all the variants at once",
           "B": "a variation point behind one interface, bound per market, store or plan",
           "C": "bound per product"}


def table(path):
    if not os.path.exists(path):
        return [], []
    with open(path, encoding="utf-8", newline="") as f:
        r = list(csv.reader(f, delimiter="\t", quoting=csv.QUOTE_NONE))
    return (r[0], [dict(zip(r[0], x)) for x in r[1:] if any(c.strip() for c in x)]) if r else ([], [])


def write(path, head, recs):
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write("\t".join(head) + "\n")
        for x in recs:
            f.write("\t".join(clean(x.get(h, "")) for h in head) + "\n")
    os.replace(tmp, path)


def ids(s):
    return [x for x in re.split(r"[,\s;]+", s or "") if x]


def clean(s):
    return re.sub(r"\s+", " ", s or "").strip()


def phrases(s):
    return [x.strip() for x in (s or "").split(";") if x.strip()]


class Subject:
    def __init__(self, subj, rd):
        self.subj, self.rd = subj, rd
        self.dir = os.path.join(subj, "c", rd)
        os.makedirs(self.dir, exist_ok=True)
        self.ppath, self.apath = os.path.join(self.dir, "points.tsv"), os.path.join(self.dir, "answers.tsv")
        _, pts = table(os.path.join(subj, "b", rd, "variation-points.tsv"))
        self.points = [p["vp_id"] for p in pts]
        self.bullet = {p["vp_id"]: p["bullet"] for p in pts}
        self.all_points = set()
        self.rows, self.var = {}, {}
        for d in sorted(os.listdir(os.path.join(subj, "b"))):
            if not re.match(r"RD\d+$", d):
                continue
            _, ps = table(os.path.join(subj, "b", d, "variation-points.tsv"))
            self.all_points |= {p["vp_id"] for p in ps}
            _, vs = table(os.path.join(subj, "b", d, "variants.tsv"))
            for v in vs:
                self.var[v["variant_id"]] = v
                if d == rd:
                    self.rows.setdefault(v["vp_id"], {})[v["variant_id"]] = v
        self.records = set()
        for p in PLATFORMS:
            for name, col in (("statements.tsv", "stmt_id"), ("gaps.tsv", "gap_id"), ("absences.tsv", "absence_id")):
                _, rs = table(os.path.join(subj, p, name))
                self.records |= {r.get(col, "") for r in rs}
        self.records.discard("")
        self.marker, self.kind = {}, {}
        for p in PLATFORMS:
            _, rs = table(os.path.join(subj, p, "statements.tsv"))
            self.marker.update({r["stmt_id"]: r.get("marker", "") for r in rs})
        _, ks = table(os.path.join(subj, "kinds.tsv"))
        self.kind = {r["id"]: r["kind"] for r in ks}
        ph, self.prow = table(self.ppath)
        ah, self.arow = table(self.apath)
        if ph and ph != PHEAD:
            sys.exit(f"points.tsv's header is {ph}, expected {PHEAD}")
        if ah and ah != AHEAD:
            sys.exit(f"answers.tsv's header is {ah}, expected {AHEAD}")

    def form(self, vid):
        v = self.var[vid]["variant"]
        return v if v in ("gap", "absent", "not covered") else "answer"

    def point_row(self, vp):
        return next((r for r in self.prow if r["vp_id"] == vp), None)

    def parse_keys(self, text):
        """{'row': {vid: [keys]}, 'open': {vid: [keys]}, 'absent': {vid: [keys]}} from a points.tsv keys cell."""
        out = {"row": {}, "open": {}, "absent": {}}
        for part in [x.strip() for x in (text or "").split(" | ") if x.strip()]:
            kind = "row"
            for k in ("open", "absent"):
                if part.startswith(k + ": "):
                    kind, part = k, part[len(k) + 2:]
            for item in [x.strip() for x in part.split(" ;; ") if x.strip()]:
                vid, _, keys = item.partition("=")
                out[kind][vid.strip()] = [k.strip() for k in keys.split(";") if k.strip()]
        return out

    def keys_text(self, km):
        parts = [" ;; ".join(f"{v}={';'.join(ks)}" for v, ks in km["row"].items())]
        for k in ("open", "absent"):
            if km[k]:
                parts.append(f"{k}: " + " ;; ".join(f"{v}={';'.join(ks)}" for v, ks in km[k].items()))
        return " | ".join(parts)

    def matrix(self, vp, km):
        """{key: {platform: state}} and {key: [variant_ids that give it]}"""
        rows = self.rows.get(vp, {})
        keys = []
        for kind in ("row", "open", "absent"):             # a key may come from a gap or absence alone
            for ks in km[kind].values():
                keys += [k for k in ks if k not in keys]
        state, giving = {}, {}
        for key in keys:
            state[key], giving[key] = {}, [v for v, ks in km["row"].items() if key in ks]
            for p in PLATFORMS:
                mine = [v for v, r in rows.items() if r["platform"] == p]
                answers = [v for v in mine if self.form(v) == "answer"]
                if any(key in km["row"].get(v, []) for v in answers):
                    s = "gives"
                elif any(key in km["absent"].get(v, []) for v in mine):
                    s = "lacks"
                elif any(key in km["open"].get(v, []) for v in mine) or \
                        not [v for v in mine if self.form(v) in ("answer", "absent")]:
                    s = "open"                             # only gap or not covered rows, or a gap asking for it
                else:
                    s = "not stated"
                state[key][p] = s
        return state, giving

    @staticmethod
    def _tag(val):
        sa, zd, sh, bc, wc = (val[p] for p in PLATFORMS)
        if all(val.values()) or not any(val.values()):    # every platform gives the key, or none does
            return "no difference"
        hosted = [sa, zd, sh, bc]
        if len(set(hosted)) == 1 and wc != hosted[0]:
            return "business model"
        if sa == zd and sh == bc and sa != sh:
            return "market, pattern"
        if sa != zd or sh != bc:
            return "vendor choice"
        return "unknown"

    @classmethod
    def propose(cls, st):
        """The mechanical tags (tests 1, 4, 5, 6), trying each way an open platform could go: one tag if every way
        gives it, else unknown. Test 4 also needs a WooCommerce statement saying what it does or doesn't provide."""
        opened = [p for p in PLATFORMS if st[p] == "open"]
        tags = set()
        for n in range(2 ** len(opened)):
            val = {p: st[p] == "gives" for p in PLATFORMS}
            for i, p in enumerate(opened):
                val[p] = bool(n >> i & 1)
            tags.add(cls._tag(val))
        return tags.pop() if len(tags) == 1 else "unknown"

    @staticmethod
    def blocking(st):
        """The open platforms whose answer could change the mechanical tag."""
        return [p for p in PLATFORMS if st[p] == "open"
                and len({Subject._tag(dict({q: st[q] == "gives" for q in PLATFORMS}, **{p: b})) for b in (True, False)}) > 1]

    def answer_problems(self, vp, r, st=None):
        out = []
        prow = self.point_row(vp)
        km = self.parse_keys(prow["keys"]) if prow else {"row": {}, "open": {}, "absent": {}}
        state, _ = self.matrix(vp, km)
        st = state.get(r["key"])
        if st is None:
            return [f"key {r['key']!r} is not one of {vp}'s keys"]
        c = r["cause"]
        if c not in CAUSES:
            out.append(f"cause {c!r} is not one of step 3's tags")
        if c == "no difference" and not (all(st[p] == "gives" for p in PLATFORMS)
                                         or all(st[p] in ("lacks", "not stated") for p in PLATFORMS)):
            out.append("no difference, but the platforms don't agree on the key: every platform gives it, or none does")
        if c in ("market, named rule", "maturity", "business model") and not ids(r["cause_basis"]):
            out.append(f"{c} names its basis in cause_basis")
        if c != "no difference" and not r["cause_reading"].startswith("Reading:"):
            out.append("cause_reading begins 'Reading:'")
        for x in ids(r["cause_basis"]):
            if x not in self.records and x not in self.var:
                out.append(f"cause_basis: {x} is no statement, gap or absence of the subject, nor a row of a point")
        for x in ids(r["blocked_by"]):
            row = self.rows.get(vp, {}).get(x)
            if not row:
                out.append(f"blocked_by: {x} is not a row of {vp}")
            elif row["variant"] not in ("gap", "not covered"):
                out.append(f"blocked_by: {x} is {'an answer' if self.form(x) == 'answer' else 'absent'}, which leaves nothing open")
        if c == "unknown" and self.blocking(st) and not ids(r["blocked_by"]):
            out.append(f"unknown while {', '.join(self.blocking(st))} could change it: name the rows that leave it open in blocked_by")
        if c == "maturity":
            unmarked = [x for x in ids(r["cause_basis"]) if x in self.marker and not self.marker[x].strip()]
            if unmarked:
                out.append(f"maturity, but {', '.join(unmarked)} carries no release marker")
        fol = phrases(r["follows"])
        allowed = (COMMON, PER_MARKET, FOUNDER, BUILD, OPEN)
        for f in fol:
            if f not in allowed:
                out.append(f"follows: {f!r} is not in the key table's words")
        cheap = r["expensive_because"].startswith("cheap")
        if not r["expensive_because"].strip():
            out.append("expensive_because is empty")
        market = [BUILD if cheap else FOUNDER] if self.bullet.get(vp) in ("d", "e") else [PER_MARKET]
        want = {"no difference": [COMMON], "market, named rule": market, "market, pattern": market,
                "vendor choice": [BUILD if cheap else FOUNDER], "business model": [BUILD if cheap else FOUNDER],
                "maturity": [BUILD if cheap else OPEN], "unknown": [BUILD if cheap else OPEN]}.get(c)
        if want and sorted(fol) != sorted(want):
            out.append(f"follows for {c} ({'cheap' if cheap else 'expensive'}) is {want[0]!r}")
        if (FOUNDER in fol) != bool(r["founder_item"].strip()):
            out.append("a founder_item is given exactly when a decision for the founder follows")
        for x in ids(r["depends_on"]):
            if x == vp:
                out.append("depends_on names the point itself")
            elif x not in self.all_points:
                out.append(f"depends_on: {x} is not a variation point of the subject")
        return out

    def point_problems(self, vp, r):
        out = []
        seen, letters = [], set()
        for e in [e.strip() for e in r["coexistence"].split(";") if e.strip()]:
            m = re.fullmatch(r"(\w+)=(unknown|D|[ABC](?:\+[ABC])*)", e)
            if not m or m.group(1) not in PLATFORMS:
                out.append(f"coexistence entry {e!r}: write platform=letters, A to C joined by +, or D or unknown alone")
                continue
            if m.group(1) in seen:
                out.append(f"coexistence names {m.group(1)} twice")
            seen.append(m.group(1))
            letters |= set(m.group(2).split("+"))
            if m.group(2) == "D" and not ids(r["coexistence_basis"]):
                out.append(f"{e}: D cites its basis in coexistence_basis")
            if m.group(2) == "D" and any(v["platform"] == m.group(1) and v["variant"] in ("gap", "not covered")
                                         for v in self.rows.get(vp, {}).values()):
                out.append(f"{e}: a platform with an open gap on the point can't be D")
            if m.group(2) == "D":
                km = self.parse_keys(r["keys"])
                given = {k for v, ks in km["row"].items() if self.rows.get(vp, {}).get(v, {}).get("platform") == m.group(1) for k in ks}
                if len(given) > 1:
                    out.append(f"{e}: D is one answer, but {m.group(1)} gives {len(given)} keys")
        missing = [p for p in PLATFORMS if p not in seen]
        if missing:
            out.append(f"coexistence has no entry for {', '.join(missing)}")
        for x in ids(r["coexistence_basis"]) + ids(r["general_basis"]):
            if x not in self.records and x not in self.var:
                out.append(f"{x} is no statement, gap or absence of the subject, nor a row of a point")
        for x in ids(r["general_variant"]):
            if x not in self.rows.get(vp, {}) or self.form(x) != "answer":
                out.append(f"general_variant: {x} is not an answer row of {vp}")
        if ids(r["general_variant"]) and not ids(r["general_basis"]):
            out.append("general_variant names the statement that shows it reaches the other in general_basis")
        fol = phrases(r["follows"])
        if fol == ["none applies"]:
            if letters & set(LETTERS):
                out.append("none applies, but a letter's rule applies")
        else:
            for f in fol:
                if f not in LETTERS.values():
                    out.append(f"follows: {f!r} is not in the letter table's words")
            want = sorted(LETTERS[x] for x in letters if x in LETTERS)
            if sorted(fol) != want:
                out.append(f"follows lists each applicable letter's rule, no more: {'; '.join(want) or 'none applies'}")
        return out


def opts(args, flags):
    o, k = {}, 0
    while k < len(args):
        if args[k] not in flags or k + 1 >= len(args):
            sys.exit(f"unknown flag or missing value: {args[k]}")
        o[flags[args[k]]] = clean(args[k + 1])
        k += 2
    return o


def show(S, vp, full=False):
    prow = S.point_row(vp)
    if not prow:
        print(f"{vp}: no point row yet; run keys")
        return
    km = S.parse_keys(prow["keys"])
    state, giving = S.matrix(vp, km)
    print(f"{vp} keys: {prow['keys']}")
    for key, st in state.items():
        kinds = {}
        for v in giving[key]:
            row = S.rows[vp][v]
            kinds.setdefault(row["platform"], set()).update(S.kind.get(x, "?") for x in ids(row["stmt_ids"]))
        print(f"  {key!r}: " + "; ".join(f"{p} {st[p]}" for p in PLATFORMS) + f" | rows {';'.join(giving[key])}"
              f" | the tests give: {S.propose(st)}"
              + (f" | open and could change it: {', '.join(S.blocking(st))}" if S.blocking(st) else ""))
        print("      kinds of what gives it: " + "; ".join(f"{p} {'/'.join(sorted(k))}" for p, k in kinds.items()))
        for p in PLATFORMS:
            if st[p] == "gives" and any(key in km["absent"].get(v, []) for v in S.rows[vp]
                                        if S.rows[vp][v]["platform"] == p):
                print(f"      contradiction: {p} gives the key and an absent row of its excludes it: weigh it in cause_reading")
    for r in S.arow:
        if r["vp_id"] == vp:
            print(f"  answer {r['key']!r}: {r['cause']} | {r['follows']} | founder: {r['founder_item'] or '-'}"
                  f" | depends on: {r['depends_on'] or '-'}")
            if full:                                       # what a re-run weighs again; never the note
                for c in ("cause_basis", "scopes_compared", "cause_reading", "blocked_by", "expensive_because"):
                    if r[c].strip():
                        print(f"      {c}: {r[c]}")
    print(f"  point: {prow['coexistence'] or '-'} | general {prow['general_variant'] or '-'} | {prow['follows'] or '-'}")
    if full:
        for c in ("coexistence_basis", "general_basis"):
            if prow[c].strip():
                print(f"      {c}: {prow[c]}")


def keep_note(old, new):
    """A row written again keeps its earlier note, which an agent may not read: the new note follows it."""
    old, new = (old or "").strip(), (new or "").strip()
    if not old or new.startswith(old):
        return new or old
    return old if not new or new in old else f"{old} {new}"


def main(subj, rd, cmd, args):
    S = Subject(subj, rd)
    if cmd in ("keys", "answer", "point", "show") and (not args or args[0] not in S.points):
        sys.exit(f"{args[0] if args else '(none)'} is not a variation point of {rd}")
    if cmd == "keys":
        keep = "--keep" in args
        args = [a for a in args if a != "--keep"]
        vp, km = args[0], {"row": {}, "open": {}, "absent": {}}
        forms = {"row": ("answer",), "open": ("gap",), "absent": ("absent",)}
        if keep and S.point_row(vp):                       # start from the stored keys, less rows no longer there
            old = S.parse_keys(S.point_row(vp)["keys"])
            for flag in km:
                for vid, ks in old[flag].items():
                    if vid in S.rows.get(vp, {}) and S.form(vid) in forms[flag]:
                        km[flag][vid] = list(ks)
                    else:
                        print(f"dropped --{flag} {vid}={';'.join(ks)}: {vid} is no longer "
                              f"{'a row of ' + vp if vid not in S.rows.get(vp, {}) else 'a ' + forms[flag][0] + ' row'}")
        named = set()
        k = 1
        while k < len(args):
            flag = {"--row": "row", "--open": "open", "--absent": "absent"}.get(args[k])
            if not flag or k + 1 >= len(args):
                sys.exit(f"unknown flag or missing value: {args[k]}")
            vid, _, keys = args[k + 1].partition("=")
            vid, keys = vid.strip(), [clean(x) for x in keys.split(";") if x.strip()]
            if vid not in S.rows.get(vp, {}):
                sys.exit(f"{vid} is not a row of {vp}")
            want = forms[flag]
            if S.form(vid) not in want:
                sys.exit(f"--{flag} takes {want[0]} rows; {vid} is {S.form(vid)}")
            if not keys or any(re.search(r"[|=]|;;", x) for x in keys):
                sys.exit(f"{args[k + 1]}: give one key at least, without '|' or '='")
            if (flag, vid) not in named:                   # a row named replaces what it held, with --keep too
                km[flag][vid] = []
                named.add((flag, vid))
            km[flag][vid] += [x for x in keys if x not in km[flag][vid]]
            k += 2
        for vid, ks in km["open"].items():
            plat = S.rows[vp][vid]["platform"]
            given = {k for v, kk in km["row"].items() if S.rows[vp][v]["platform"] == plat for k in kk}
            if set(ks) & given:
                sys.exit(f"--open {vid}: {plat} gives {', '.join(sorted(set(ks) & given))}, so it isn't open on it")
        left = [v for v in S.rows.get(vp, {}) if S.form(v) == "answer" and v not in km["row"]]
        if left:
            sys.exit(f"every answer row takes a key: {', '.join(left)} has none")
        state, giving = S.matrix(vp, km)
        prow = S.point_row(vp)
        if prow:
            prow["keys"] = S.keys_text(km)
        else:
            S.prow.append(dict({h: "" for h in PHEAD}, vp_id=vp, keys=S.keys_text(km)))
        S.arow = [r for r in S.arow if r["vp_id"] != vp or r["key"] in state]
        for r in S.arow:                                   # what each platform does follows the keys
            if r["vp_id"] == vp:
                st = state[r["key"]]
                r.update(rows=";".join(giving[r["key"]]),
                         **{c: ";".join(p for p in PLATFORMS if st[p] == s) for c, s in
                            (("gives", "gives"), ("lacks", "lacks"), ("open", "open"), ("not_stated", "not stated"))})
        order = {p: i for i, p in enumerate(S.points)}
        S.prow.sort(key=lambda x: order.get(x["vp_id"], 10**6))
        write(S.ppath, PHEAD, S.prow)
        write(S.apath, AHEAD, S.arow)
        show(S, vp)
    elif cmd == "answer":
        if len(args) < 2:
            sys.exit(__doc__)
        vp, key = args[0], clean(args[1])
        prow = S.point_row(vp)
        if not prow:
            sys.exit(f"{vp} has no keys yet: run keys first")
        km = S.parse_keys(prow["keys"])
        state, giving = S.matrix(vp, km)
        if key not in state:
            sys.exit(f"{key!r} is not one of {vp}'s keys: {', '.join(repr(k) for k in state)}")
        r = dict({h: "" for h in AHEAD}, vp_id=vp, key=key, **opts(args[2:], AFLAGS))
        st = state[key]
        r.update(rows=";".join(giving[key]),
                 **{c: ";".join(p for p in PLATFORMS if st[p] == s) for c, s in
                    (("gives", "gives"), ("lacks", "lacks"), ("open", "open"), ("not_stated", "not stated"))})
        bad = S.answer_problems(vp, r)
        if bad:
            sys.exit("not written:\n  " + "\n  ".join(bad))
        was = next((x for x in S.arow if x["vp_id"] == vp and x["key"] == key), None)
        r["note"] = keep_note(was["note"] if was else "", r["note"])
        S.arow = [x for x in S.arow if not (x["vp_id"] == vp and x["key"] == key)] + [r]
        order = {p: i for i, p in enumerate(S.points)}
        S.arow.sort(key=lambda x: order.get(x["vp_id"], 10**6))
        write(S.apath, AHEAD, S.arow)
        print(f"{vp} {key!r}: written ({r['cause']}; {r['follows']}); the tests gave {S.propose(st)}")
    elif cmd == "point":
        vp = args[0]
        prow = S.point_row(vp)
        if not prow:
            sys.exit(f"{vp} has no keys yet: run keys first")
        new = {h: prow[h] if h in ("vp_id", "keys") else "" for h in PHEAD}
        new.update(opts(args[1:], PFLAGS))
        new["note"] = keep_note(prow["note"], new["note"])
        bad = S.point_problems(vp, new)
        if bad:
            sys.exit("not written:\n  " + "\n  ".join(bad))
        S.prow[S.prow.index(prow)] = new
        write(S.ppath, PHEAD, S.prow)
        print(f"{vp}: point row written ({new['coexistence']}; {new['follows']})")
    elif cmd == "show":
        show(S, args[0], full="--full" in args[1:])
    elif cmd == "check":
        unknown = [v for v in args if v not in S.points]
        if unknown:
            sys.exit(f"not variation points of {rd}: {', '.join(unknown)}")
        bad = 0
        for vp in (args or S.points):
            prow = S.point_row(vp)
            if not prow:
                print(f"{vp}: no point row")
                bad += 1
                continue
            km = S.parse_keys(prow["keys"])
            state, _ = S.matrix(vp, km)
            for v in S.rows.get(vp, {}):
                if S.form(v) == "answer" and v not in km["row"]:
                    print(f"{vp}: answer row {v} has no key (phase B may have added it since)")
                    bad += 1
            for v in list(km["row"]) + list(km["open"]) + list(km["absent"]):
                if v not in S.rows.get(vp, {}):
                    print(f"{vp}: {v} is no longer a row of the point")
                    bad += 1
            for key in state:
                r = next((x for x in S.arow if x["vp_id"] == vp and x["key"] == key), None)
                if not r:
                    print(f"{vp}: key {key!r} has no answer row")
                    bad += 1
                    continue
                for p in S.answer_problems(vp, r):
                    print(f"{vp} {key!r}: {p}")
                    bad += 1
            for v, row in S.rows.get(vp, {}).items():
                if row["variant"] == "gap" and v not in km["open"]:
                    print(f"{vp}: note: gap row {v} marks no key; mark the key it asks for with --open, if any")
            if not prow["coexistence"]:
                print(f"{vp}: the point row has no coexistence yet")
                bad += 1
            else:
                for p in S.point_problems(vp, prow):
                    print(f"{vp}: {p}")
                    bad += 1
        print(f"{len(args or S.points)} points checked; {bad} problems")
        sys.exit(1 if bad else 0)
    elif cmd == "refresh":                                 # what each platform does, from the stored keys again
        for vp in (args or S.points):
            prow = S.point_row(vp)
            if not prow:
                continue
            state, giving = S.matrix(vp, S.parse_keys(prow["keys"]))
            for r in S.arow:
                if r["vp_id"] == vp and r["key"] in state:
                    st = state[r["key"]]
                    r.update(rows=";".join(giving[r["key"]]),
                             **{c: ";".join(p for p in PLATFORMS if st[p] == x) for c, x in
                                (("gives", "gives"), ("lacks", "lacks"), ("open", "open"), ("not_stated", "not stated"))})
        write(S.apath, AHEAD, S.arow)
        print(f"refreshed: {', '.join(args or S.points)}")
    elif cmd == "batch":
        import shlex
        if len(args) != 1 or not os.path.exists(args[0]):
            sys.exit("batch FILE: a file of commands, one per line, as you would give them after the root decision")
        failed = 0
        for n, line in enumerate(open(args[0], encoding="utf-8"), start=1):
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            words = shlex.split(line)
            if words[0] == "batch":
                sys.exit(f"line {n}: a batch can't hold a batch")
            try:
                main(subj, rd, words[0], words[1:])
            except SystemExit as e:
                if e.code not in (None, 0):
                    print(f"line {n} failed: {e.code}")
                    failed += 1
        print(f"batch: {failed} lines failed")
        sys.exit(1 if failed else 0)
    elif cmd == "notes":
        if len(args) != 2:
            sys.exit(__doc__)
        path = os.path.join(S.dir, "notes-c.md")
        text = open(path, encoding="utf-8").read() if os.path.exists(path) else ""
        head = f"## {clean(args[0])}"
        lines = text.splitlines()
        if head not in lines:
            lines += ([""] if lines else []) + [head]
        at = lines.index(head) + 1                 # the end of the part's own section, before the next part's heading
        while at < len(lines) and not lines[at].startswith("## "):
            at += 1
        while at > 0 and not lines[at - 1].strip():
            at -= 1
        lines[at:at] = ["", args[1].strip()]
        text = "\n".join(lines).rstrip("\n") + "\n"
        tmp = path + ".tmp"
        open(tmp, "w", encoding="utf-8").write(text)
        os.replace(tmp, path)
        print(f"notes-c.md: appended under {head}")
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    if len(sys.argv) < 4:
        sys.exit(__doc__)
    subj, rd = sys.argv[1].rstrip("/"), sys.argv[2]
    folder = os.path.join(subj, "c", rd)
    os.makedirs(folder, exist_ok=True)
    with open(os.path.join(folder, ".edit.lock"), "w") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        main(subj, rd, sys.argv[3], sys.argv[4:])
