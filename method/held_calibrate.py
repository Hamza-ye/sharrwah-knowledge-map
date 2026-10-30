# Compares a calibration batch of the held pass with the reviewed placements of the same entries (Stage 4A; the dry
# run's review, held/review-H.md, section 7): the calibration places again entries a batch placed and the review
# corrected, under the rewritten brief, at an effort the coordinator sets, and this measures how far it lands from the
# corrected result. It reads only placement files; it writes nothing.
#
# Usage: python3 -I method/held_calibrate.py --platform P --key BATCH --batch CAL_BATCH [--file PATH] [--show]
#   per entry: the (capability, supports) pairs the key and the calibration give, and what differs:
#     missing   a pair the key holds and the calibration doesn't (a line left out, or another capability)
#     extra     a pair the calibration holds and the key doesn't
#     supports  the same capability with another supports
#   and, for each difference, whether it would change the model once held_amend writes it: a cell that holds nothing, or
#   a placement (core, own-service, extension-point, outside) the cell doesn't hold yet. That is the review's "important
#   detail" (review-H.md, section 3).
import argparse, collections, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from class_slice import MODEL, PLATFORMS, rows

HELD = os.path.join(MODEL, "held")
PLACED = {"core", "own-service", "extension-point", "outside"}


def pairs(platform, batch, ids, path=None):
    out = collections.defaultdict(set)
    for r in rows(path or os.path.join(HELD, platform, f"placements-{batch}.tsv")):
        for e in [x.strip() for x in r["entry_id"].split(";") if x.strip()]:
            if e in ids:
                cap = r["cap_id"] if r["placement"] != "out" else "out"
                if cap.startswith("new:"):
                    cap = "new"
                for s in [x.strip() for x in r["supports"].split(";") if x.strip()] or ["-"]:
                    out[e].add((cap, s))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--platform", choices=PLATFORMS, required=True)
    ap.add_argument("--key", required=True)
    ap.add_argument("--batch", required=True)
    ap.add_argument("--show", action="store_true")
    ap.add_argument("--file", help="the calibration's placements, where they aren't held/<platform>/placements-<batch>.tsv")
    a = ap.parse_args()
    ids = [l.strip() for l in open(os.path.join(HELD, "batches", f"{a.batch}.txt"), encoding="utf-8") if l.strip()]
    key, cal = pairs(a.platform, a.key, set(ids)), pairs(a.platform, a.batch, set(ids), a.file)
    cells = {r["cap_id"]: r for r in rows(os.path.join(MODEL, "merged", "cells.tsv")) if r["platform"] == a.platform}

    def matters(cap, s):
        c = cells.get(cap)
        if cap in ("new", "out") or not c:
            return True
        return c["held"] != "statements" or (s in PLACED and s not in set((c.get("placed_as") or "").split(";")))

    n = collections.Counter()
    for e in ids:
        k, c = key.get(e, set()), cal.get(e, set())
        kc, cc = {x for x, _ in k}, {x for x, _ in c}
        diffs = []
        for cap, s in sorted(k - c):
            diffs.append(("supports" if cap in cc else "missing", cap, s, matters(cap, s)))
        for cap, s in sorted(c - k):
            if cap not in kc:
                diffs.append(("extra", cap, s, matters(cap, s)))
        n["entries"] += 1
        n["lines in key"] += len(k)
        n["matching pairs"] += len(k & c)
        if not diffs:
            n["entries matching whole"] += 1
        for kind, cap, s, imp in diffs:
            n[kind] += 1
            if imp:
                n[f"{kind}, changing the model"] += 1
        if a.show and diffs:
            print(f"{e}: key {sorted(k)} | calibration {sorted(c)}")
            for kind, cap, s, imp in diffs:
                print(f"    {kind} {cap} {s}{'  (changes the model)' if imp else ''}")
    print(f"{a.batch} against {a.key} ({a.platform}):")
    for k in ("entries", "entries matching whole", "lines in key", "matching pairs", "missing", "missing, changing the model",
              "supports", "supports, changing the model", "extra", "extra, changing the model"):
        print(f"  {k}: {n[k]}")


if __name__ == "__main__":
    main()
