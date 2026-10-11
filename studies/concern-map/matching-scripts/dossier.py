"""Write one dossier file per platform: each concern with its terms, inventory entries
and distinct statement identifiers, to read while judging candidates.

Usage: python3 -I dossier.py <outdir>
"""
import collections
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import load  # noqa: E402


def main(outdir):
    os.makedirs(outdir, exist_ok=True)
    data = load.load_all()
    for p in load.PLATFORMS:
        concerns = data[p][0]
        with open(os.path.join(outdir, f"dossier-{p}.txt"), "w", encoding="utf-8") as f:
            for cid, c in concerns.items():
                f.write(f"#### {cid} | {c['name']}\n")
                f.write(f"  TERMS: {c['terms_raw']}\n")
                if c["split_note"]:
                    f.write(f"  SPLIT: {c['split_note']}\n")
                for r in c["inv"]:
                    f.write(f"  INV {r['inv_id']} [{r['list']}] {r['entry']}  -> {r['concern_ids']}\n")
                ids = collections.OrderedDict()
                for s in c["stmts"]:
                    key = (s["placement"], s["identifier"])
                    ids.setdefault(key, 0)
                    ids[key] += 1
                for (pl, ident), n in ids.items():
                    f.write(f"  ST {pl}: {ident}" + (f" (x{n})" if n > 1 else "") + "\n")
                f.write("\n")


if __name__ == "__main__":
    main(sys.argv[1])
