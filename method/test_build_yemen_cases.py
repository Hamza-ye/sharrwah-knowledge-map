# Tests method/build_yemen_cases.py against the rules of studies/yemen-cases/brief.md ("The build"), on a small
# made-up study: each test names the rule it checks. Run: python3 -I method/test_build_yemen_cases.py
import os, sys, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_yemen_cases as B

# condition_id: (group, label, place, held_at, holds, now, source)
ROWS = {
    # G1: latest per place; precision tie gives a dispute
    "YQ-A001": ("G1", "banned", "North", "2019-12-18", "held", "", "s1"),
    "YQ-A002": ("G1", "allowed", "South", "2017-01", "held", "", "s2"),
    "YQ-A003": ("G1", "old only", "North", "2020-01", "held", "", "s3"),
    "YQ-A004": ("G1", "allowed", "Coast", "2024", "held", "", "s4"),
    "YQ-A005": ("G1", "banned", "Coast", "2024-05", "held", "", "s5"),
    # G2: a later across-Yemen state supersedes; an older one doesn't; an undated one loses to dated ones
    "YQ-A006": ("G2", "common", "across Yemen", "2024", "held", "", "s6"),
    "YQ-A007": ("G2", "rare", "South", "2020", "held", "", "s7"),
    "YQ-A008": ("G2", "rare", "North", "2019-12-18", "held", "", "s1"),
    "YQ-A009": ("G2", "rare", "place not stated", "no date", "held", "", "s8"),
    "YQ-A010": ("G2", "none", "East", "2025", "held", "", "s9"),
    # G3: one source, two states: `now` wins, and another source agreeing with it is no dispute
    "YQ-A011": ("G3", "fee 1%", "South", "2025-01", "held", "yes", "s10"),
    "YQ-A012": ("G3", "fee 2%", "South", "2025-01", "held", "", "s10"),
    "YQ-A013": ("G3", "fee 1%", "South", "2025-01", "held", "", "s11"),
    # G4: provided for only, at one place; a proposed state is never today and builds no case
    "YQ-A014": ("G4", "licence required", "North", "2027-01-01", "provided for", "", "s12"),
    "YQ-A015": ("G4", "no licence", "South", "2023", "held", "", "s13"),
    "YQ-A016": ("G4", "licence and bond", "South", "2026", "proposed", "", "s14"),
    # G5: an across-Yemen state that is only provided for makes no part of today
    "YQ-A017": ("G5", "open", "across Yemen", "2026", "provided for", "", "s15"),
    "YQ-A018": ("G5", "closed", "South", "2024", "held", "", "s16"),
    "YQ-A019": ("G5", "open", "North", "2022", "held", "", "s17"),
    # G6: one label at two places, plus a proposed one: a constant
    "YQ-A020": ("G6", "available", "North", "2025", "held", "", "s18"),
    "YQ-A021": ("G6", "available", "South", "2025", "held", "", "s19"),
    "YQ-A022": ("G6", "withdrawn", "South", "2026", "proposed", "", "s20"),
    # combinations: s1 shows G1 and G2 together on 2019-12-18; s21 shows two states at the same date but one
    # with a time of day, which is the same time; s22's rows are undated, so they form no combination
    "YQ-A023": ("G3", "fee 3%", "North", "2021-03-01", "held", "", "s21"),
    "YQ-A024": ("G1", "banned", "East", "2021-03-01 09:30", "held", "", "s21"),
    "YQ-A025": ("G3", "fee 5%", "West", "no date", "held", "", "s22"),
    "YQ-A026": ("G1", "allowed", "West", "no date", "held", "", "s22"),
}
GROUPS = ["G1", "G2", "G3", "G4", "G5", "G6"]

def make(study):
    with open(os.path.join(study, "conditions.tsv"), "w") as f:
        f.write("condition_id\tcondition\tstate\tplace\theld_at\tdate_basis\tcite_ids\tnote\n")
        for cid, (g, l, p, h, *_ ) in ROWS.items():
            f.write(f"{cid}\t{g}\t{l}\t{p}\t{h}\tstated\tYE-{cid[3:]}\t\n")
    with open(os.path.join(study, "citations.tsv"), "w") as f:
        f.write("cite_id\tsource\tlocator\tquote\tsource_date\tdate_basis\tfetched_from\turl\n")
        for cid, r in ROWS.items():
            f.write(f"YE-{cid[3:]}\tsharrwah-knowledge-map@0000000:evidence/yemen/runs/{r[6]}.txt\tL1\tq\t2025\tpublished\toutside Yemen\t\n")
    with open(os.path.join(study, "groups.tsv"), "w") as f:
        f.write("group_id\tcondition\twhat_varies\tcondition_ids\tnote\n")
        for n, g in enumerate(GROUPS, start=1):
            f.write(f"YG-{n:03d}\t{g}\tvaries\t{', '.join(c for c, r in ROWS.items() if r[0] == g)}\t\n")
    with open(os.path.join(study, "states.tsv"), "w") as f:
        f.write("condition_id\tgroup_id\tlabel\tplace\tholds\tnow\tnote\n")
        for cid, (g, l, p, h, holds, now, s) in ROWS.items():
            f.write(f"{cid}\tYG-{GROUPS.index(g) + 1:03d}\t{l}\t{p}\t{holds}\t{now}\t\n")

def main():
    failures = []
    def check(what, got, want):
        if got != want:
            failures.append(f"{what}:\n    got  {got!r}\n    want {want!r}")
    with tempfile.TemporaryDirectory() as study:
        make(study)
        out, summary = B.build(study)
        axes = {r[1]: r for r in out["axes.tsv"]}
        consts = {r[1]: r for r in out["constants.tsv"]}
        cases = out["cases.tsv"]
        check("axis or constant", (sorted(axes), sorted(consts)), (["G1", "G2", "G3", "G4", "G5"], ["G6"]))
        check("G1 today: latest per place; 2024 and 2024-05 tie, so Coast is disputed",
              axes["G1"][5], "disputed @ Coast + banned @ East + old only @ North + allowed @ South + allowed @ West")
        check("G2 today: a later across-Yemen state supersedes South and North and the undated place; East's later one stands",
              axes["G2"][5], "common + none @ East")
        check("G3 today: the source's `now` state, with another source agreeing, is no dispute",
              axes["G3"][5], "fee 3% @ North + fee 1% @ South + fee 5% @ West")
        check("G4 today: a place with only a provided-for state is unknown; a proposed state is never today",
              axes["G4"][5], "unknown @ North + no licence @ South")
        check("G5 today: an across-Yemen state that is only provided for makes no part",
              axes["G5"][5], "open @ North + closed @ South")
        check("G6: one shown label is a constant, with the proposed one in its note",
              (consts["G6"][2], consts["G6"][3], consts["G6"][6]),
              ("available", "North; South", "proposed: withdrawn @ South [YE-A022]"))
        check("G4 lists its proposed state, tagged", "licence and bond @ South (proposed)" in axes["G4"][4], True)
        names = [c[1] for c in cases]
        ax = {r[1]: r[0] for r in out["axes.tsv"]}
        g3_2 = f"{ax['G3']}=fee 3% @ North + fee 2% @ South + fee 5% @ West"
        check("the dropped state of a `now` pair is a case that occurred, not one in force",
              [c[3] for c in cases if c[1] == g3_2], ["occurred"])
        check("no case is built from a proposed state", any("licence and bond" in n for n in names), False)
        check("a provided-for state builds a case with basis provided for",
              [c[3] for c in cases if "licence required @ North" in c[1]], ["provided for"])
        combo = [c for c in cases if c[5].startswith("shown together by evidence/yemen/runs/s1.txt")]
        check("s1 shows G1 and G2 together on 2019-12-18: one combination case",
              [(c[1], c[3]) for c in combo],
              [(f"{ax['G1']}=disputed @ Coast + banned @ East + banned @ North + allowed @ South + allowed @ West; "
                f"{ax['G2']}=common + none @ East + rare @ North", "occurred")])
        check("a time of day doesn't make a different time; both s21 states are already today's, so no case",
              [c for c in cases if "s21" in c[5]], [])
        check("undated rows form no combination", [c for c in cases if "s22" in c[5]], [])
        check("disputed states count as non-today, and hold now: in force",
              sorted(c[3] for c in cases if c[1].startswith(f"{ax['G1']}=") and "Coast" in c[1] and ";" not in c[1]
                     and "disputed" not in c[1]), ["in force", "in force"])
        B.MAX_AXES = 2
        out2, summary2 = B.build(study)
        check("past the cap, no cases until review-axes.md exists", (len(out2["cases.tsv"]), "stops for review" in summary2), (0, True))
        open(os.path.join(study, "review-axes.md"), "w").write("reviewed")
        out3, _ = B.build(study)
        check("after the review, the cases are built", len(out3["cases.tsv"]) == len(cases), True)
    print(summary)
    if failures:
        print(f"{len(failures)} failed:\n  " + "\n  ".join(failures))
        sys.exit(1)
    print("all build tests pass")

if __name__ == "__main__":
    main()
