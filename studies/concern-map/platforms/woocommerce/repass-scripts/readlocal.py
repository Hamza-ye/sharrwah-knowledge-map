# Normalized text of a local working copy (HTML -> text as the checker does; markdown as is).
# Usage: python3 -I readlocal.py FILE [START_MARKER] [CHARS]
import os, sys, textwrap
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import qcheck
raw = open(sys.argv[1], encoding="utf-8", errors="replace").read()
t = qcheck.norm(qcheck.html_text(raw) if sys.argv[1].endswith(".html") else raw)
i = t.find(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2] else 0
n = int(sys.argv[3]) if len(sys.argv) > 3 else 4000
print(len(t), i)
print("\n".join(textwrap.wrap(t[max(i, 0):max(i, 0) + n], 240)))
