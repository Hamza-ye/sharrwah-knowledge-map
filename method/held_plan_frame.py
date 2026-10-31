"""The held pass, Shopify's SH-91 (the coordinator's re-plan of 31 October): the last entries of `plan-page-admin` are
ibx5bt-xy's plan page as rendered in a settings dialog, its items read from <body>, so they hold the admin's own frame.
SH-89's R89.9, which its check kept, places that frame `out`: the main navigation (items lines 8 to 23), a repeat of what
`admin-main-nav` holds and places for ibx5bt-xy; the keyboard shortcuts (lines 27 to 87), each naming another place as a
key's target; and the UI strings (the skip link, the search, the store's name, the dialog's Close, the drag hint). The
trial banner takes SH-3's line 9 (CM-PLN-001 `core`), and 'Plus+' is the Plus card's title, SH-89's line 69. Any other
entry stops the script, for an agent.

Usage:
  python3 -I method/held_plan_frame.py            prints what it would place
  python3 -I method/held_plan_frame.py --apply    writes SH-91's lines
"""
import csv, os, re, sys

if any(a in ("-h", "--help") for a in sys.argv[1:]):
    sys.exit(__doc__)

H = "/home/user/sharrwah-knowledge-map/studies/class-model/held"
BATCH = "SH-91"
csv.field_size_limit(10**9)
E = {}
with open(f"{H}/shopify/entries.tsv", newline="", encoding="utf-8") as f:
    for r in csv.DictReader(f, delimiter="\t", quoting=csv.QUOTE_NONE):
        E[r["entry_id"]] = r
HEAD = open(f"{H}/shopify/placements-SH-1.tsv", encoding="utf-8").readline().rstrip("\n").split("\t")


def line_of(batch, n):
    L = open(f"{H}/shopify/placements-{batch}.tsv", encoding="utf-8").read().split("\n")
    return dict(zip(L[0].split("\t"), L[n - 1].split("\t")))


BANNER = line_of("SH-3", 9)
PLUS = line_of("SH-89", 69)
assert BANNER["entry_id"] == "SH-E-71d2ecf6" and BANNER["cap_id"] == "CM-PLN-001", BANNER
assert PLUS["entry_id"] == "SH-E-b0614809" and PLUS["cap_id"] == "CM-PLN-001", PLUS
TAIL = "; placed by method/held_plan_frame.py (SH-89's R89.9)"

out, kinds = [], {}
for e in [x.strip() for x in open(f"{H}/batches/{BATCH}.txt") if x.strip()]:
    t, loc = E[e]["text"], E[e]["locator"]
    m = re.match(r"line (\d+)", loc)
    n = int(m.group(1)) if m else 0
    row = {h: "" for h in HEAD}
    row["entry_id"] = e
    banner = re.match(r"tag: (p|s-internal-button); text: (Trial ends in 2 days|Subscribe for \$1|Select a plan)", t)
    if banner:
        row.update(placement="capability", cap_id="CM-PLN-001", supports="core", scope="ibx5bt-xy", terms=banner.group(2))
        row["reading"] = (f"a reading: the trial banner on ibx5bt-xy's plan page, '{banner.group(2)}', opening the plan "
                          f"checkout (/store/ibx5bt-xy/subscribe/checkout), the same banner SH-3's line 9 places on the "
                          f"store's home (SH-E-71d2ecf6): CM-PLN-001 core, the store's days left its own" + TAIL)
        kind = "the trial banner"
    elif t.startswith("tag: h3; text: Plus+"):
        row.update(placement="capability", cap_id="CM-PLN-001", supports=PLUS["supports"], scope=PLUS["scope"], terms="Plus")
        row["reading"] = ("a reading: the Plus card's title, 'Plus' with an aria-hidden '+', as SH-89's line 69 places "
                          "fake-demo-sharrwah's card title (SH-E-b0614809)" + TAIL)
        kind = "the Plus card's title"
    elif n < 8 or n == 493 or re.match(r"tag: (div; text: To pick up a draggable|s-internal-button; text: Close)", t):
        row["placement"] = "out"
        row["reading"] = ("a reading: a UI string of the admin's frame on the plan page (the skip link, the search, the "
                          "store's name, the dialog's Close or the drag hint), which names no capability" + TAIL)
        kind = "the UI strings"
    elif 8 <= n <= 23:
        row["placement"] = "out"
        row["reading"] = ("a reading: the admin's main navigation, repeated on the plan page because its items were read "
                          "from <body>; admin-main-nav holds it for ibx5bt-xy (ibx5bt-xy@home) and its batches place each "
                          "item, so here it is the page's frame" + TAIL)
        kind = "the main navigation"
    elif 27 <= n <= 87:
        row["placement"] = "out"
        row["reading"] = ("a reading: the admin's keyboard shortcuts list, the page's frame: a shortcut names another "
                          "place as a key's target, not its own thing, as a route's nextRoutes does" + TAIL)
        kind = "the keyboard shortcuts"
    else:
        sys.exit(f"{e} (line {n}) is none of R89.9's kinds: {t[:120]}")
    assert '"' not in "".join(row.values())
    out.append(row)
    kinds[kind] = kinds.get(kind, 0) + 1

print(f"{len(out)} entries: " + ", ".join(f"{k} {v}" for k, v in kinds.items()))
if "--apply" in sys.argv:
    p = f"{H}/shopify/placements-{BATCH}.tsv"
    assert not os.path.exists(p), f"{p} exists"
    with open(p, "w", encoding="utf-8") as f:
        f.write("\t".join(HEAD) + "\n")
        for r in out:
            f.write("\t".join(r[h] for h in HEAD) + "\n")
    print(f"wrote {p}")
