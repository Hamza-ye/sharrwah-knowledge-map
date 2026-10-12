# Verify statements (and their citation quotes) of the given statement modules against the working copies.
import importlib, json, os, sys
Z = "/tmp/claude-0/-home-user/9f45def8-b710-5f9c-84f3-6a0fa7e617c8/scratchpad/q1n/zid"
sys.path.insert(0, os.path.join(Z, "scripts"))
import stlib, zverify
for m in sys.argv[1:]: importlib.import_module(m)
reg = json.load(open(os.path.join(Z, "fetched", "registry.json"), encoding="utf-8"))
bad = 0; n = 0
for s in stlib.STATEMENTS:
    n += 1
    files = reg.get(s["url"], {}).get("files")
    if not files:
        print("NO SOURCE", s["c"], s["p"], s["url"]); bad += 1; continue
    for kind, txt in (("statement", s["text"]), ("quote", s["quote"])):
        if not txt: continue
        r = zverify.check(txt, files)
        if not r.startswith("found"):
            bad += 1; print("NOT FOUND", kind, s["c"], s["p"], s["url"][:70], "|", txt[:120])
    if not s["quote"] and len(s["text"]) > 400: print("LONG (needs quote)", s["c"], s["p"], len(s["text"]))
print(f"statements {n}, gaps {len(stlib.GAPS)}, problems {bad}")
