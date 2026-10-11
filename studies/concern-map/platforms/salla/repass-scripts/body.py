# Prints a help.salla.sa working copy's article body with line numbers (title to the 'ask' footer). python3 -I body.py FILE
import sys, re
lines = open(sys.argv[1], encoding="utf-8").read().split("\n")
start = 0
for i, l in enumerate(lines):
    if "تاريخ اخر تحديث" in l:
        start = max(0, i - 3); break
end = len(lines)
for i in range(start, len(lines)):
    if lines[i].startswith("اسأل, واطلب الدعم") or lines[i].strip() == "تصنيفات ذات صلة":
        end = i; break
for i in range(start, end):
    if lines[i].strip():
        print(f"{i+1}: {lines[i]}")
