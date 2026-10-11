# Flattens held dashboard translation files (work/tr/<lang>_<ns>.json) and prints keys whose value matches a regex.
# Usage: python3 -I trgrep.py <lang> <regex> [ns-regex]
import sys, os, json, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *
lang, pat = sys.argv[1], re.compile(sys.argv[2])
nsre = re.compile(sys.argv[3]) if len(sys.argv) > 3 else None
d = f"{SP}/work/tr"
def flat(o, p=""):
    if isinstance(o, dict):
        for k, v in o.items():
            yield from flat(v, f"{p}.{k}" if p else k)
    elif isinstance(o, list):
        for i, v in enumerate(o):
            yield from flat(v, f"{p}[{i}]")
    else:
        yield p, o
for fn in sorted(os.listdir(d)):
    if not fn.startswith(lang + "_"): continue
    ns = fn[len(lang)+1:-5]
    if nsre and not nsre.search(ns): continue
    try:
        o = json.load(open(os.path.join(d, fn), encoding="utf-8"))
    except Exception as e:
        print("ERR", fn, e); continue
    for k, v in flat(o):
        if isinstance(v, str) and pat.search(v):
            print(f"{ns}\t{k}\t{v}")
