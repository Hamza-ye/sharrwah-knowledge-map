# PLAN.md Stage 0: checks every Q1 gap against what is held, and re-routes the gaps that went to the founder,
# or kept a kind, on a page or corpus we already hold. It closes no gap: a re-routed gap is read inside a subject.
#
# Rules, each recorded per row in held-check.tsv:
#   H1 held page        the run could not read the route's page (a browser save, a 403, a block), and the page is held:
#                       readable -> "page not read" for an agent; index only -> the founder commits the archive
#   H2 corpus unread    a "searched, not found" on a platform with a held text corpus that the search did not cover
#   H3 incorporated     an agreement a platform's terms incorporate may be read (PLAN.md section 6, agreed at G0)
#   H4 held structure   a dashboard page held as a structure under another address (named in ALIASES, with the reason)
#   H5 no source named  a "searched, not found" that names no source it read
# A row already re-routed (its why_not_held starts with "Stage 0") is left as it is, so the script can run again.
#
# Usage: python3 -I method/q1_held_check.py STUDY_DIR [--dry-run]
import csv, glob, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from held_index import CORPORA as HELD_CORPORA, Held, describe, names_a_source, urls_in

study = sys.argv[1]
DRY = "--dry-run" in sys.argv[2:]
HERE = os.path.dirname(os.path.abspath(__file__))
SKM = os.path.dirname(HERE)
ROOTS = {"observed-sa": os.environ.get("OBSERVED_SA", "/home/user/observed-sa"),
         "observed-sh": os.environ.get("OBSERVED_SH", "/home/user/observed-sh"),
         "sharrwah-knowledge-map": SKM}
H = Held(ROOTS, sorted(glob.glob(os.path.join(SKM, "evidence/product-class/runs/*"))))
SA = H.commits.get("observed-sa", "")[:8]
CORPORA = {p: (marker, f"observed-sa@{SA}:structures/salla/help-articles/ar/texts.jsonl and "
                         f"observed-sa@{SA}:structures/salla/help-articles/en/texts.jsonl")
           for p, (marker, _) in HELD_CORPORA.items()}
ALIASES = {  # route -> (held structure, why it is a candidate)
    "s.salla.sa/payments/kyc": (f"observed-sa@{SA}:structures/salla/kyc-schema",
                                "structures/REGISTER.tsv describes it as the store verification in the merchant dashboard"),
}
UNREAD = re.compile(r"403|bot[- ]challenge|could not be read|couldn't be read|cannot be read|can't be read|"
                    r"not reachable|unreachable|refus|blocked", re.I)
DATE = "12 October 2026"

def clean(s):
    return " ".join(s.split())

def apply(plat, r):
    """Returns (rule, new fields, held_at) or None."""
    route, why, means, kind, who = r["route"], r["why_not_held"], r["means"], r["gap_kind"], r["who_can"]
    if why.startswith("Stage 0"):
        return None
    before = f"Before: {kind}, {who}, {means}. {why}"
    for key, (loc, reason) in ALIASES.items():
        if key in route and os.path.isdir(os.path.join(ROOTS["observed-sa"], loc.split(":", 1)[1])):
            return "H4", {"gap_kind": "page not read", "who_can": "agent", "means": "read the held structure",
                          "route": f"{loc} (a candidate: {reason}); then {route}",
                          "why_not_held": f"Stage 0, {DATE}: a held structure may show it. {before}"}, loc
    could_not_read = "save a page from a browser" in means or (kind == "page not read" and who == "founder")
    if could_not_read or UNREAD.search(why):
        held, idx_only, unheld = [], [], []
        for u in urls_in(route):
            hs = H.lookup(u)
            if not could_not_read:
                # The note names something unreadable; a route page this repository captured was read by the run.
                if any(h["kind"] == "capture" for h in hs):
                    continue
                hs = [h for h in hs if h["kind"] != "capture"]
            readable = [h for h in hs if h["readable"]]
            if readable:
                held.append((u, readable[:2]))
            elif hs:
                idx_only.append((u, hs[0]))
            else:
                unheld.append(u)
        if held:
            parts = [f"{u} held at " + " and ".join(describe(h) for h in hs) for u, hs in held]
            parts += [f"{u} held only in an index: {describe(h)}" for u, h in idx_only]
            parts += [f"{u} not held" for u in unheld]
            return "H1", {"gap_kind": "page not read", "who_can": "agent", "means": "read the held page",
                          "route": "; ".join(parts),
                          "why_not_held": f"Stage 0, {DATE}: the page is held, and the run could not read it. {before}"}, \
                   "; ".join(describe(hs[0]) for _, hs in held)
        if idx_only:
            parts = [f"{u} held only in an index: {describe(h)}" for u, h in idx_only] + [f"{u} not held" for u in unheld]
            return "H1", {"gap_kind": "page not read", "who_can": "founder", "means": "commit the held archive",
                          "route": "; ".join(parts),
                          "why_not_held": f"Stage 0, {DATE}: the page is held, but its archive is not in git. {before}"}, \
                   "; ".join(describe(h) for _, h in idx_only)
    if plat == "woocommerce" and kind == "page not read" and who == "founder" and "Connected Account Agreement" in route:
        return "H3", {"who_can": "agent",
                      "why_not_held": f"Stage 0, {DATE}: PLAN.md section 6, agreed at G0, allows reading an agreement "
                                      f"a platform's terms incorporate. {before}"}, ""
    if kind == "searched, not found" and plat in CORPORA and CORPORA[plat][0] not in route + " " + why:
        return "H2", {"gap_kind": "page not read", "who_can": "agent", "means": "search the held corpus",
                      "route": f"{CORPORA[plat][1]}; then {route}",
                      "why_not_held": f"Stage 0, {DATE}: the held corpus was not searched. {before}"}, CORPORA[plat][1]
    if kind == "searched, not found" and not names_a_source(route + " " + why):
        return "H5", {"gap_kind": "page not read", "who_can": "agent",
                      "why_not_held": f"Stage 0, {DATE}: the search named no source it read. {before}"}, ""
    return None

log = [["platform", "concern_id", "placement", "rule", "before_kind", "before_who", "before_means",
        "after_kind", "after_who", "after_means", "held_at"]]
counts = {}
for plat in ("shopify", "salla", "woocommerce", "zid", "bigcommerce"):
    path = os.path.join(study, "platforms", plat, "gaps.tsv")
    if not os.path.exists(path):
        continue
    with open(path, encoding="utf-8", newline="") as f:
        rows = list(csv.reader(f, delimiter="\t", quoting=csv.QUOTE_NONE))
    head, body = rows[0], rows[1:]
    out = [head]
    for row in body:
        r = dict(zip(head, row))
        res = apply(plat, r) if r.get("concern_id") else None
        if res:
            rule, new, held_at = res
            log.append([plat, r["concern_id"], r["placement"], rule, r["gap_kind"], r["who_can"], r["means"],
                        new.get("gap_kind", r["gap_kind"]), new.get("who_can", r["who_can"]),
                        new.get("means", r["means"]), clean(held_at)])
            r.update({k: clean(v) for k, v in new.items()})
            counts[(plat, rule)] = counts.get((plat, rule), 0) + 1
        out.append([r.get(h, "") for h in head])
    if not DRY:
        with open(path, "w", encoding="utf-8", newline="") as f:
            for row in out:
                f.write("\t".join(row) + "\n")
if not DRY:
    lp = os.path.join(study, "held-check.tsv")
    new_file = not os.path.exists(lp)
    with open(lp, "a", encoding="utf-8", newline="") as f:
        for row in (log if new_file else log[1:]):
            f.write("\t".join(clean(c) for c in row) + "\n")
# The founder's list of pages to save: tick every address that is held, and say where.
TO_SAVE = os.path.join(SKM, "evidence/product-class/to-save-from-browser.md")
if os.path.exists(TO_SAVE):
    lines, ticked, open_ = open(TO_SAVE, encoding="utf-8").read().split("\n"), 0, 0
    for i, line in enumerate(lines):
        if not line.startswith("- [ ] "):
            continue
        us = urls_in(line)
        hs = [h for h in (H.lookup(us[-1]) if us else []) if h["readable"]]
        if hs:
            lines[i] = "- [x] " + line[6:] + f" (held: {describe(hs[0])})"
            ticked += 1
        else:
            open_ += 1
    note = (f"**Stage 0, {DATE}.** Every address below that observed-sa, observed-sh or this repository holds is ticked, "
            "with where it is held. Under `PLAN.md`, nothing here is asked of the founder until a subject needs it.")
    if note not in lines:
        lines.insert(2, note + "\n")
    if not DRY:
        open(TO_SAVE, "w", encoding="utf-8").write("\n".join(lines))
    print(f"to-save list: {ticked} newly ticked as held, {open_} not held")
print(f"held index: observed-sa {H.commits.get('observed-sa', '')[:8]}, observed-sh {H.commits.get('observed-sh', '')[:8]}")
for (plat, rule), n in sorted(counts.items()):
    print(f"{plat}\t{rule}\t{n}")
print("re-routed:", sum(counts.values()))
