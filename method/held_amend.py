# The coordinator's amendments from the held pass (Stage 4A; briefs/H-held.md, "After the batches"): each checked
# placement of an entry on a capability becomes an evidence row of that platform's cell, in the part that holds the
# cell, with its terms added to the cell's, its slot filler and its quality in the part's own files; the cell's reading
# says what the held pass added, and a cell that held nothing becomes held. The entry's scope is read from its
# placement by class_slice.py. A `new` thing is placed only once the coordinator has decided it in held/new.tsv: the
# capability it is (made in an amendment part first), an existing one it turned out to be, or out.
#
# The held pass's second stage (briefs/S2-held.md; method/s2_held.py's `land`) lands each platform's rows as the batch
# S2-<XX>: its placements, as above; its rows that name a statement of the concern map (held/<platform>/s2-keys.tsv),
# each an evidence row citing the statement; and its other outcomes (held/<platform>/s2-outcomes.tsv). For each cell
# still holding nothing after the batch, `apply` writes into the cell's reading what the second stage read, at its
# commits, and its outcome (not found, not held, absent from a complete list with its source, unreadable or unclear),
# and adds the terms it searched to the cell's `searched` (the coordinator's decisions 2 and 3, S2-held-design.md).
# A held cell whose statements state no placement (`placed_as` only `not-stated`) is treated, for a second-stage batch,
# as a cell holding nothing: its outcome's sentence says no passage read in this stage states a placement, and is added
# to its reading (the coordinator's decision on inspection-S2.md, S2I-21). A cell's earlier reading and outcome
# sentences are kept and added to, never overwritten, when a batch makes it held (S2I-30); an outcome row a later batch
# changed replaces its earlier sentence, and a row marked `superseded` is not planned (S2I-22).
#
# Usage:
#   python3 -I method/held_amend.py plan --platform P [--batch B ...]    what the amendment would write, per part and
#                                                                        cell (no change)
#   python3 -I method/held_amend.py apply --platform P [--batch B ...]   writes it; then run check_class_part.py on each
#                                                                        part it names, and class_merge.py --complete
# Without --batch, every batch held/batches.tsv lists for the platform is planned, and apply refuses a part whose
# evidence already cites any planned entry: run it once per platform, after all its batches are checked. With --batch
# (repeatable, such as --batch S2-ZD), only those batches are planned, their rows of s2-keys.tsv and s2-outcomes.tsv
# with them, and only their new things wait on held/new.tsv; apply refuses a part only where the same capability,
# platform and entry or statement are already in its evidence (that batch, or that line, was applied before), since an
# entry the held pass placed on another capability may take a second line (inspection-Q3M.md, Q3M-19).
import argparse, collections, glob, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from class_slice import MODEL, PLATFORMS, rows, citable, key as skey, fold

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HELD = os.path.join(MODEL, "held")
PARTS = os.path.join(MODEL, "parts")
NEW_HEAD = ["platform", "name", "decision", "reading"]
OUTCOME_WORDS = {"not-found": "not found", "not-held": "not held: the place that would state it isn't held",
                 "absent": "absent from a complete list the platform publishes", "unreadable": "held, but not in a form the tools read",
                 "unclear": "a passage may be the thing, but its words don't settle it"}


def clip(s, n):
    s = " ".join(str(s).split())
    return s if len(s) <= n else s[: n - 1] + "…"


def table(path):
    raw = open(path, encoding="utf-8").read().split("\n")
    head = raw[0].split("\t")
    return head, [dict(zip(head, l.split("\t"))) for l in raw[1:] if l.strip()]


def write(path, head, rs):
    with open(path, "w", encoding="utf-8") as f:
        f.write("\t".join(head) + "\n")
        for r in rs:
            f.write("\t".join(r.get(h, "") for h in head) + "\n")


def semi(s):
    return [x.strip() for x in (s or "").split(";") if x.strip()]


def held_entries(p):
    """The held pass's entries, then its second stage's (entries-s2.tsv)."""
    return {r["entry_id"]: r for f in ("entries.tsv", "entries-s2.tsv") for r in rows(os.path.join(HELD, p, f))}


def is_s2(batch):
    return batch.startswith("S2-")


def not_placed(c):
    """A held cell whose statements state no placement (s2_held.not_placed)."""
    return c.get("held") == "statements" and set(semi((c.get("placed_as") or "").replace(",", ";"))) <= {"not-stated"}


def holds_nothing(c, s2=True):
    """A cell holding nothing, or, for a second-stage batch, held with no placement stated (S2I-21)."""
    return c.get("held") != "statements" or (s2 and not_placed(c))


def plan(p, batches=None):
    entries = held_entries(p)
    cells = {(r["cap_id"], r["platform"]): r for r in rows(os.path.join(MODEL, "merged", "cells.tsv"))}
    caps = {r["cap_id"] for r in rows(os.path.join(MODEL, "merged", "capabilities.tsv"))}
    new = {}
    if os.path.exists(os.path.join(HELD, "new.tsv")):
        for r in rows(os.path.join(HELD, "new.tsv")):
            if r["platform"] == p:
                new[r["name"]] = r["decision"]
    rowsout, pending = collections.defaultdict(list), []
    extra = collections.defaultdict(lambda: {"terms": [], "fillers": [], "qualities": []})
    outcomes = collections.defaultdict(list)
    listed = {r["batch"] for r in rows(os.path.join(HELD, "batches.tsv"))}     # a calibration's batches aren't listed
    if batches:
        unlisted = [b for b in batches if b not in listed]
        if unlisted:
            sys.exit(f"{', '.join(unlisted)}: not listed in held/batches.tsv")
        paths = [os.path.join(HELD, p, f"placements-{b}.tsv") for b in batches]
        for path in paths:
            if not os.path.exists(path):
                sys.exit(f"no {os.path.relpath(path, ROOT)}")
    else:
        paths = sorted(glob.glob(os.path.join(HELD, p, "placements-*.tsv")))
    take = set(batches) if batches else {b for b in listed if is_s2(b)}

    def place(batch, cap, ids, ss, why, r):
        """One placement on a capability, or on a new thing once decided: its evidence rows and side files."""
        cs = [cap] if cap else []
        if r["placement"] == "new":
            d = new.get(cap[4:].strip())
            if not d:
                pending.append((batch, cap, ids))
                return
            if d == "out":
                return
            cs = [d.split(":", 1)[1]]
        elif r["placement"] != "capability":
            return
        for c in cs:
            if c not in caps or (c, p) not in cells:
                sys.exit(f"{batch}: {c} has no cell for {p} in the merged model; make it first")
            for e in ids:
                for s in ss or ["shows"]:
                    rowsout[(c, p)].append({"cap_id": c, "platform": p, "supports": s, "key": e, "why": why(e), "_batch": batch})
                x = extra[(c, p)]
                x["terms"] += [t.strip() for t in r.get("terms", "").split(";") if t.strip()]
                for fl in [t.strip() for t in r.get("filler", "").split(";") if t.strip()]:
                    x["fillers"].append({"cap_id": c, "platform": p, "filler": fl, "key": e})
                for q in [t.strip() for t in r.get("quality", "").split(";") if t.strip()]:
                    what, _, val = q.partition(":")
                    x["qualities"].append({"cap_id": c, "platform": p, "quality": what.strip(), "value": val.strip() or what.strip(), "key": e})

    for path in paths:
        batch = re.search(r"placements-(.+)\.tsv$", path).group(1)
        if batch not in listed:
            continue
        for r in rows(path):
            ids = [x.strip() for x in r["entry_id"].split(";") if x.strip()]
            ss = [s.strip() for s in r["supports"].split(";") if s.strip()]
            if is_s2(batch):
                why = lambda e, r=r, batch=batch: f"(the held pass's second stage, {batch}) {' '.join(r['reading'].split())}: {clip(entries[e]['text'], 120)}"
            else:
                why = lambda e, r=r, batch=batch: f"(the held pass, {batch}) {' '.join(r['reading'].split())}: {clip(entries[e]['text'], 120)}"
            place(batch, r["cap_id"].strip(), ids, ss, why, r)
    # the second stage's rows that name a statement of the concern map, a placed inventory entry or a subject's statement
    for r in rows(os.path.join(HELD, p, "s2-keys.tsv")):
        if r["batch"] in take and r["batch"] in listed:
            r = dict(r, placement="new" if r["cap_id"].startswith("new:") else "capability")
            place(r["batch"], r["cap_id"].strip(), [r["key"]], semi(r["supports"]), lambda e, r=r: r["why"], r)
    # and its other outcomes, for the cells they name
    for r in rows(os.path.join(HELD, p, "s2-outcomes.tsv")):
        if r["batch"] in take and r["batch"] in listed and (r["subject"], p) in cells and not r.get("superseded"):
            outcomes[(r["subject"], p)].append(r)
    return cells, rowsout, pending, extra, outcomes


def summary(evs, entries, stm):
    """What the batches add to a cell, for its reading: the held pass's entries, then its second stage's passages."""
    out = []
    first_pass = [e for e in evs if not is_s2(e["_batch"])]
    if first_pass:
        by = collections.Counter(e["supports"] for e in first_pass)
        structs = list(dict.fromkeys(entries[e["key"]]["structure"] for e in first_pass))
        ids = list(dict.fromkeys(e["key"] for e in first_pass))
        first = "; ".join(clip(entries[i]["text"], 70) for i in ids[:3])
        out.append(f"The held pass adds {', '.join(f'{v} {k}' for k, v in by.items())} from {len(ids)} "
                   f"entr{'y' if len(ids) == 1 else 'ies'} of {', '.join(structs)} ({', '.join(ids[:6])}{' …' if len(ids) > 6 else ''}: {first})")
    second = [e for e in evs if is_s2(e["_batch"])]
    if second:
        bs = list(dict.fromkeys(e["_batch"] for e in second))
        by = collections.Counter(e["supports"] for e in second)
        ids = list(dict.fromkeys(e["key"] for e in second))
        quoted = [i for i in ids if entries.get(i, {}).get("structure") == "second-stage"]
        earlier = [i for i in ids if i in entries and i not in quoted]
        ks = [i for i in ids if i not in entries]
        text = lambda i: entries[i]["text"] if i in entries else (stm.get(i, {}).get("statement") or "")
        what = []
        for xs, one, many in ((quoted, "entry it quoted", "entries it quoted"),
                              (earlier, "entry of the held pass", "entries of the held pass"),
                              (ks, "statement already in the concern map", "statements already in the concern map")):
            if xs:
                what.append(f"{len(xs)} {one if len(xs) == 1 else many}")
        first = "; ".join(clip(text(i), 70) for i in ids[:3])
        out.append(f"The held pass's second stage ({', '.join(bs)}) adds {', '.join(f'{v} {k}' for k, v in by.items())} from "
                   f"{' and '.join(what)} ({', '.join(ids[:6])}{' …' if len(ids) > 6 else ''}: {first})")
    return ". ".join(out)


def bare(t):
    """A term without a language prefix (`en: payment terms`), for comparing (inspection-S2.md, S2I-31)."""
    return re.sub(r"^[a-z]{2}:\s*", "", t.strip())


def search_terms(searched):
    """The terms of a second-stage row's searches (`<tool> <language>: <term>, <term>`), for the cell's `searched`; an
    address (held_index: <address>) is what it read, not a term."""
    out = []
    for piece in semi(searched):
        m = re.match(r"^(.+?)\s+([a-z]{2}):\s*(.+)$", piece)
        if not m:
            continue
        for t in m.group(3).split(","):
            t = re.sub(r"\s*(?::|—|-|->|→|\()\s*nothing\)?\s*$", "", t.strip()).strip()
            if t and t.casefold() != "nothing":
                out.append(t)
    return out


def outcome_sentence(o, p, placed_none=False):
    """What the second stage read for a cell still holding nothing, at its commits (PLAN.md, section 6: 'A searched,
    not found lists what it read, at a commit'). For a held cell whose statements state no placement, it says that no
    passage read in this stage states one (S2I-21). What it read is clipped, and a capture's raw form stays in
    s2-outcomes.tsv (S2I-24)."""
    ref = f"held/{p}/s2/{o['part']}.tsv line {o['line']}"
    words = OUTCOME_WORDS.get(o["outcome"], o["outcome"])
    if placed_none:
        words = f"no passage read in this stage states a placement for it ({words})"
    s = f"The held pass's second stage ({o['batch']}) read the held pages at {', '.join(semi(o['commits']))} ({ref}): {words}"
    if o["outcome"] in ("absent", "unclear") and o.get("source"):
        at = o["entry_id"] + ", " if o.get("entry_id") else ""
        s += f", from {at}{o['source']} {o.get('locator', '')}".rstrip() + f" ('{clip(o.get('quote', ''), 160)}')"
    if o["outcome"] == "unclear" and o.get("capture"):
        s += f"; what would settle it: {clip(o['capture'], 240)}"
    elif o["outcome"] == "not-held" and o.get("capture"):
        s += f"; capture requested (held/{p}/s2-outcomes.tsv)"
    elif o["outcome"] == "unreadable" and o.get("capture"):
        s += f"; the reader to be extended (held/{p}/s2-outcomes.tsv)"
    return s + f". It read: {clip(' '.join(o.get('read', '').split()), 200)}.", ref


def main():
    ap = argparse.ArgumentParser(description="the coordinator's amendments from the held pass and its second stage")
    ap.add_argument("cmd", choices=["plan", "apply"])
    ap.add_argument("--platform", choices=PLATFORMS, required=True)
    ap.add_argument("--batch", action="append", help="plan only this batch (repeatable): such as S2-ZD")
    a = ap.parse_args()
    p = a.platform
    entries = held_entries(p)
    stm = {skey(x): x for x in citable(p)}
    cells, out, pending, extra, outcomes = plan(p, a.batch)
    for b, name, ids in pending:
        print(f"PENDING {b}: {name} ({len(ids)} entries) waits on the coordinator's decision in held/new.tsv")
    by_part = collections.defaultdict(list)
    for k, evs in out.items():
        by_part[cells[k]["part"]].append((k, evs))
    # a cell the batch leaves holding nothing takes its outcomes into its reading and searched
    s2 = bool(a.batch) and all(is_s2(b) for b in a.batch)
    still = {k: os_ for k, os_ in outcomes.items() if k not in out and holds_nothing(cells[k])}
    earlier_out = collections.defaultdict(list)       # each subject's outcome rows that a later batch superseded
    for r in rows(os.path.join(HELD, p, "s2-outcomes.tsv")):
        if r.get("superseded"):
            earlier_out[(r["subject"], r.get("superseded"))].append(r)
    for k in still:
        if not any(k == x for x, _ in by_part[cells[k]["part"]]):
            by_part[cells[k]["part"]].append((k, []))
    became = sum(1 for k in out if holds_nothing(cells[k], s2))
    print(f"{p}: {sum(len(v) for v in out.values())} evidence rows for {len(out)} cells in {len(by_part)} parts; "
          f"{became} cells that held nothing become held"
          + (f"; {len(still)} cells still holding nothing take the second stage's outcomes" if still else ""))
    for part, ks in sorted(by_part.items()):
        print(f"   {part}: {len(ks)} cells, {sum(len(v) for _, v in ks)} rows")
    PLACED = {"core", "own-service", "extension-point", "outside"}
    for k, evs in sorted(out.items()):
        was = set((cells[k].get("placed_as") or "").split(";")) - {"", "not-stated"}
        now = {e["supports"] for e in evs} & PLACED
        if holds_nothing(cells[k], s2) or now - was:
            print(f"   CHANGES {k[0]}@{k[1]}: {cells[k]['held']}, placed {';'.join(sorted(was)) or 'nowhere'} -> adds {';'.join(sorted(now - was)) or 'shows only'} ({len(evs)} rows)")
    for k, os_ in sorted(still.items()):
        for o in os_:
            print(f"   OUTCOME {k[0]}@{k[1]}: {o['outcome']} ({o['batch']}, s2/{o['part']}.tsv line {o['line']}){', ' + o['could_change'] if o.get('could_change') else ''}")
    if a.cmd == "plan":
        return
    if pending:
        sys.exit("decide every new thing in held/new.tsv first")
    # every part is tested before any is written, so a refusal leaves the model as it was
    for part, ks in sorted(by_part.items()):
        eh, ev = table(os.path.join(PARTS, part, "evidence.tsv"))
        if a.batch:
            have = {(r["cap_id"], r["platform"], r["key"]) for r in ev}
            again = sorted({(e["cap_id"], e["key"]) for _, evs in ks for e in evs if (e["cap_id"], e["platform"], e["key"]) in have})
            if again:
                sys.exit(f"{part}: its evidence already holds {again[0][1]} on {again[0][0]}@{p}"
                         f"{f' and {len(again) - 1} more' if len(again) > 1 else ''}: applied before")
        else:
            have = {r["key"] for r in ev}
            if any(e["key"] in have for _, evs in ks for e in evs):
                sys.exit(f"{part}: its evidence already cites entries of {p}: applied before")
    for part, ks in sorted(by_part.items()):
        d = os.path.join(PARTS, part)
        eh, ev = table(os.path.join(d, "evidence.tsv"))
        ch, cl = table(os.path.join(d, "cells.tsv"))
        idx = {(r["cap_id"], r["platform"]): r for r in cl}
        for k, evs in ks:
            ev += evs
            c = idx[k]
            placed_none = not_placed(cells[k]) and bool(still.get(k))
            if evs:
                note = summary(evs, entries, stm)
                # the cell's earlier reading, the concern map's and any outcome sentence, is kept and added to (S2I-30)
                if c["held"] != "statements":
                    c["held"] = "statements"
                    each = "each" if any(is_s2(e["_batch"]) for e in evs) else "each entry"
                    c["reading"] = (c["reading"].rstrip() + " " + note + f" (a reading of {each}, in its evidence row).").strip()
                else:
                    c["reading"] = (c["reading"].rstrip() + " " + note + ".").strip()
                c["terms"] = ";".join(dict.fromkeys([t for t in c.get("terms", "").split(";") if t] + extra[k]["terms"]))
            for o in still.get(k, []):
                sentence, ref = outcome_sentence(o, p, placed_none)
                if sentence in c["reading"]:
                    continue                # written by an earlier apply of the same batch
                # an earlier batch's sentence for the same subject, which this batch's row changed, is replaced (S2I-22)
                olds = [outcome_sentence(x, p, placed_none)[0] for x in earlier_out.get((o["subject"], o["batch"]), [])]
                old = next((x for x in olds if x in c["reading"]), None)
                if old:
                    c["reading"] = c["reading"].replace(old, sentence)
                else:
                    c["reading"] = (c["reading"].rstrip() + " " + sentence).strip()
                have_t = {fold(bare(t)) for t in semi(c.get("searched", ""))}
                add = [t for t in dict.fromkeys(search_terms(o.get("searched", ""))) if fold(bare(t)) not in have_t]
                c["searched"] = ";".join(semi(c.get("searched", "")) + add)
        write(os.path.join(d, "evidence.tsv"), eh, ev)
        write(os.path.join(d, "cells.tsv"), ch, cl)
        for fname, key in (("slot-fillers.tsv", "fillers"), ("qualities.tsv", "qualities")):
            add = [x for k, _ in ks for x in extra[k][key]]
            path = os.path.join(d, fname)
            if not os.path.exists(path):
                # a back-fill part may leave the file out (check_class_part.py's BACKFILL_FILES); it is made, with the
                # anchor's header, only where the part's cells now hold a filler or a quality
                if not add:
                    continue
                fh_, fr = table(os.path.join(PARTS, part.split("-")[0] + "-anchor", fname))[0], []
            else:
                fh_, fr = table(path)
            fr += add
            write(path, fh_, fr)
        where = os.path.relpath(d) if not os.path.relpath(d).startswith("..") else d
        print(f"wrote {part}: check it with python3 -I method/check_class_part.py {where}")


if __name__ == "__main__":
    main()
