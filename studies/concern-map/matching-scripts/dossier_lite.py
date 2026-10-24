"""Lighter dossier: terms, split note, inventory entries, and only those statement
identifiers that do not repeat an inventory entry. Usage: python3 -I dossier_lite.py <outdir>"""
import collections, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import load  # noqa: E402

def main(outdir):
    data = load.load_all()
    for p in load.PLATFORMS:
        concerns = data[p][0]
        with open(os.path.join(outdir, f"dossier-lite-{p}.txt"), "w", encoding="utf-8") as f:
            for cid, c in concerns.items():
                f.write(f"#### {cid} | {c['name']}\n  TERMS: {c['terms_raw']}\n")
                if c["split_note"]:
                    f.write(f"  SPLIT: {c['split_note']}\n")
                entries = set()
                for r in c["inv"]:
                    entries.add(r["entry"])
                    f.write(f"  INV {r['inv_id']} [{r['list']}] {r['entry']}\n")
                seen = collections.OrderedDict()
                for s in c["stmts"]:
                    if s["identifier"] in entries:
                        continue
                    seen.setdefault((s["placement"], s["identifier"]), s["statement"][:160])
                for (pl, ident), st in seen.items():
                    f.write(f"  ST {pl}: {ident} :: {st}\n")
                f.write("\n")

if __name__ == "__main__":
    main(sys.argv[1])
