"""Edit one root decision's phase B files row by row, for phase B's second pass: join a statement to a variant, add,
replace or remove a variant, record a task's outcome, and add a platform's words to a point's x_words.

Usage: python3 -I method/variants_edit.py SUBJECT_DIR RD COMMAND [ARGS]

Commands (ids are `;`- or `,`-separated):
  rows VP_ID [PLATFORM]          print the point's rows, its question and x_words, compactly
  join VARIANT_ID --stmts IDS [--evidence TEXT]
                                 add statements to an answer row; its kind and scope are taken again from all its
                                 statements (the brief's rule 6); TEXT is added to basis_evidence after "; ". A
                                 statement the row already holds isn't added twice: only TEXT is
  add VP_ID PLATFORM --variant EXCERPT --stmts IDS --basis BASES --evidence TEXT [--note TEXT]
  add VP_ID PLATFORM --gap --gaps IDS [--note TEXT]
  add VP_ID PLATFORM --absent --absences IDS [--note TEXT]
  add VP_ID PLATFORM --not-covered [--note TEXT]
                                 a new row, with the next free variant_id of the root decision's range (b/ranges.tsv)
                                 after the folder's last; prints the id
  replace VARIANT_ID ...         as add, keeping the row's id, point and platform: the brief's revisit
  remove VARIANT_ID              a revisited row whose answers all joined other rows
  done TASK ID BULLET OUTCOME    a row in b/RD/done.tsv, the ledger `method/second_pass_list.py --check` reads
  xwords VP_ID PLATFORM WORDS    the platform's words for X, added to the point's x_words
  vpnote VP_ID TEXT              TEXT added to the point's note after "; "
  rownote VARIANT_ID TEXT        TEXT added to the row's own note after "; ", such as what a later task changed

It reads the root decision's slice (statements, absences) for kinds, scopes and statement text, so an answer's
excerpt is checked to be in one of its statements, and refuses: an id outside the slice; a basis outside `term`,
`identifiers`, `definition` and `answers`; an excerpt not found verbatim in its statements (spaces aside); a point
not in the folder's variation-points.tsv. Each file is written whole, to a temporary file first, then renamed.
Each command holds a lock on the root decision's folder while it reads and writes, so two agents working on
different platforms of one root decision can't overwrite each other's rows.
"""
import csv, fcntl, os, re, sys

csv.field_size_limit(10**9)
PLATFORMS = ("shopify", "salla", "zid", "woocommerce", "bigcommerce")
BASES = ("term", "identifiers", "definition", "answers")
VHEAD = ["variant_id", "vp_id", "platform", "variant", "stmt_ids", "basis", "basis_evidence", "kind", "scope",
         "gap_ids", "absence_ids", "note"]


def table(path):
    if not os.path.exists(path):
        return [], []
    with open(path, encoding="utf-8", newline="") as f:
        r = list(csv.reader(f, delimiter="\t", quoting=csv.QUOTE_NONE))
    if not r:
        return [], []
    return r[0], [dict(zip(r[0], x)) for x in r[1:] if any(c.strip() for c in x)]


def write(path, head, recs):
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write("\t".join(head) + "\n")
        for r in recs:
            f.write("\t".join(clean(r.get(h, "")) for h in head) + "\n")
    os.replace(tmp, path)


def clean(s):
    return re.sub(r"[\t\r\n]+", " ", s or "").strip()


def ids(s):
    return [x for x in re.split(r"[,\s;]+", s or "") if x]


def squash(s):
    return re.sub(r"\s+", "", s or "")


class Folder:
    def __init__(self, subj, rd):
        self.subj, self.rd = subj, rd
        self.dir = os.path.join(subj, "b", rd)
        if not os.path.isdir(self.dir):
            sys.exit(f"no folder {self.dir}")
        _, st = table(os.path.join(subj, "slices", rd, "statements.tsv"))
        _, ab = table(os.path.join(subj, "slices", rd, "absences.tsv"))
        self.st = {r["stmt_id"]: r for r in st}
        self.ab = {r["absence_id"]: r for r in ab}
        _, rg = table(os.path.join(subj, "b", "ranges.tsv"))
        me = [r for r in rg if r["root_decision"] == rd]
        if not me:
            sys.exit(f"{rd} has no row in b/ranges.tsv")
        self.lo, self.hi = int(me[0]["variant_from"]), int(me[0]["variant_to"])
        self.vpath = os.path.join(self.dir, "variants.tsv")
        self.phead, self.points = table(os.path.join(self.dir, "variation-points.tsv"))
        head, self.var = table(self.vpath)
        if head and head != VHEAD:
            sys.exit(f"variants.tsv's header is {head}, expected {VHEAD}")

    def save(self):
        write(self.vpath, VHEAD, self.var)

    def row(self, vid):
        for r in self.var:
            if r["variant_id"] == vid:
                return r
        sys.exit(f"{vid} is not a row of b/{self.rd}/variants.tsv")

    def point(self, vp):
        for p in self.points:
            if p["vp_id"] == vp:
                return p
        sys.exit(f"{vp} is not a variation point of b/{self.rd}/variation-points.tsv")

    def next_id(self):
        used = [int(re.search(r"(\d+)$", r["variant_id"]).group(1)) for r in self.var]
        n = max([u for u in used if self.lo <= u <= self.hi] + [self.lo - 1]) + 1
        if n > self.hi:
            sys.exit(f"{self.rd}'s variant range ends at {self.hi}")
        return f"S02-V-{n:03d}"

    def stmts(self, s):
        out = []
        for x in ids(s):
            if x not in self.st:
                sys.exit(f"{x} is not in {self.rd}'s slice: it is under none of {self.rd}'s bullets")
            if x not in out:
                out.append(x)
        return out

    def kind_scope(self, sids):
        kinds = []
        for s in sids:
            for k in self.st[s]["kind"].split(";"):
                if k.strip() and k.strip() not in kinds:
                    kinds.append(k.strip())
        scopes = {}
        for s in sids:
            sc = self.st[s].get("scope", "").strip()
            if sc:
                scopes.setdefault(sc, []).append(s)
        if len(scopes) == 1 and sum(len(v) for v in scopes.values()) == len(sids):
            scope = next(iter(scopes))
        else:
            scope = "; ".join(f"{sc} ({', '.join(v)})" for sc, v in scopes.items())
        return ";".join(kinds), scope


def opts(args, flags=("--gap", "--absent", "--not-covered")):
    o, i = {}, 0
    while i < len(args):
        a = args[i]
        if a in flags:
            o[a] = True
            i += 1
        elif a.startswith("--") and i + 1 < len(args):
            o[a] = args[i + 1]
            i += 2
        else:
            sys.exit(f"unexpected argument {a!r}")
    return o


def build(F, vp, plat, o):
    """The fields of an add or a replace, from its options."""
    F.point(vp)
    if plat not in PLATFORMS:
        sys.exit(f"platform {plat!r} is not one of {', '.join(PLATFORMS)}")
    r = {h: "" for h in VHEAD}
    r.update(vp_id=vp, platform=plat, note=o.get("--note", ""))
    if o.get("--gap"):
        if not ids(o.get("--gaps", "")):
            sys.exit("a gap row names its --gaps")
        r.update(variant="gap", gap_ids=";".join(ids(o["--gaps"])))
    elif o.get("--absent"):
        ab = ids(o.get("--absences", ""))
        if not ab or any(a not in F.ab for a in ab):
            sys.exit(f"--absences must name absences of {F.rd}'s slice: {', '.join(a for a in ab if a not in F.ab)}")
        kinds = []
        for a in ab:
            if F.ab[a]["kind"] not in kinds:
                kinds.append(F.ab[a]["kind"])
        r.update(variant="absent", absence_ids=";".join(ab), kind=";".join(kinds))
    elif o.get("--not-covered"):
        r.update(variant="not covered")
    else:
        sids = F.stmts(o.get("--stmts", ""))
        if not sids:
            sys.exit("an answer row names its --stmts")
        exc = o.get("--variant", "")
        if not exc or not any(squash(exc) in squash(F.st[s]["statement"]) for s in sids):
            sys.exit("--variant must be an excerpt, verbatim, of one of its statements")
        bases = [b.strip() for b in re.split(r"[;,]", o.get("--basis", "")) if b.strip()]
        if not bases or any(b not in BASES for b in bases):
            sys.exit(f"--basis takes one or more of {', '.join(BASES)}")
        if not o.get("--evidence"):
            sys.exit("an answer row gives its --evidence")
        kind, scope = F.kind_scope(sids)
        r.update(variant=exc, stmt_ids=";".join(sids), basis=";".join(bases), basis_evidence=o["--evidence"],
                 kind=kind, scope=scope)
    return r


def main(subj, rd, cmd, args):
    F = Folder(subj, rd)
    if cmd == "rows":
        p = F.point(args[0])
        print(f"{p['vp_id']} ({p['bullet']}) {p['question']}\n  x_words: {p['x_words']}")
        for r in F.var:
            if r["vp_id"] == args[0] and (len(args) < 2 or r["platform"] == args[1]):
                print(f"  {r['variant_id']} {r['platform']}: {r['variant'][:120]} | {r['stmt_ids']} | {r['basis']} | "
                      f"{r['basis_evidence'][:160]} | kind {r['kind']} | gaps {r['gap_ids']} | absences {r['absence_ids']}")
    elif cmd == "join":
        r, o = F.row(args[0]), opts(args[1:])
        if r["variant"] in ("gap", "absent", "not covered"):
            sys.exit(f"{args[0]} is a '{r['variant']}' row: replace it instead")
        sids = ids(r["stmt_ids"]) + [s for s in F.stmts(o.get("--stmts", "")) if s not in ids(r["stmt_ids"])]
        missing = [s for s in sids if s not in F.st]
        if missing:
            sys.exit(f"the row names statements outside {rd}'s slice: {', '.join(missing)}")
        r["kind"], r["scope"] = F.kind_scope(sids)
        r["stmt_ids"] = ";".join(sids)
        if o.get("--evidence"):
            r["basis_evidence"] = (r["basis_evidence"] + "; " if r["basis_evidence"] else "") + o["--evidence"]
        F.save()
        print(f"{args[0]}: {len(sids)} statements; kind {r['kind']}")
    elif cmd == "add":
        r = build(F, args[0], args[1], opts(args[2:]))
        r["variant_id"] = F.next_id()
        F.var.append(r)
        F.save()
        print(r["variant_id"])
    elif cmd == "replace":
        old = F.row(args[0])
        r = build(F, old["vp_id"], old["platform"], opts(args[1:]))
        r["variant_id"] = old["variant_id"]
        F.var[F.var.index(old)] = r
        F.save()
        print(f"{args[0]} replaced: {r['variant'][:80]}")
    elif cmd == "remove":
        F.var.remove(F.row(args[0]))
        F.save()
        print(f"{args[0]} removed")
    elif cmd == "done":
        if len(args) != 4 or args[0] not in ("place", "revisit", "reread", "note"):
            sys.exit("done TASK ID BULLET OUTCOME, TASK being place, revisit, reread or note")
        path = os.path.join(F.dir, "done.tsv")
        head, recs = table(path)
        recs.append(dict(zip(["task", "id", "bullet", "outcome"], args)))
        write(path, ["task", "id", "bullet", "outcome"], recs)
        print(f"done.tsv: {args[0]} {args[1]} ({args[2]}) recorded")
    elif cmd == "rownote":
        r = F.row(args[0])
        r["note"] = (r["note"] + "; " if r["note"] else "") + clean(args[1])
        F.save()
        print(f"{args[0]}: note written")
    elif cmd in ("xwords", "vpnote"):
        p = F.point(args[0])
        if cmd == "xwords":
            plat, words = args[1], args[2]
            if plat not in PLATFORMS:
                sys.exit(f"platform {plat!r} is not one of {', '.join(PLATFORMS)}")
            parts = [x.strip() for x in p["x_words"].split(" | ")]
            for k, x in enumerate(parts):
                if x.startswith(plat + ":"):
                    parts[k] = x + "; " + words
                    break
            else:
                parts.append(f"{plat}: {words}")
            p["x_words"] = " | ".join(parts)
        else:
            p["note"] = (p["note"] + "; " if p["note"] else "") + args[1]
        write(os.path.join(F.dir, "variation-points.tsv"), F.phead, F.points)
        print(f"{args[0]}: {cmd} written")
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    if len(sys.argv) < 5:
        sys.exit(__doc__)
    subj, rd = sys.argv[1].rstrip("/"), sys.argv[2]
    folder = os.path.join(subj, "b", rd)
    if not os.path.isdir(folder):
        sys.exit(f"no folder {folder}")
    with open(os.path.join(folder, ".edit.lock"), "w") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)           # held until the command has read and written its files
        main(subj, rd, sys.argv[3], sys.argv[4:])
