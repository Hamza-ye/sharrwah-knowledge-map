# Extract the compare-plans table (groups, features, per-plan values) from the pricing JS chunk, keeping the raw object text.
import sys, re
s = open(sys.argv[1], encoding="utf-8").read()
for g in re.finditer(r'\{group:\{ar:"([^"]*)",en:"([^"]*)"\},features:\[', s):
    start = g.end()
    # find matching closing bracket of features array
    depth, i = 1, start
    while depth and i < len(s):
        if s[i] == "[": depth += 1
        elif s[i] == "]": depth -= 1
        i += 1
    feats = s[start:i-1]
    print(f"## GROUP\t{g.group(2)}\t{g.group(1)}")
    for f in re.finditer(r'\{name:\{ar:"([^"]*)",en:"([^"]*)"\},description:\{ar:"([^"]*)",en:"([^"]*)"\},plans:\{([^}]*)\}\}', feats):
        print(f"{f.group(2)}\t{f.group(1)}\t{f.group(5)}\t{f.group(4)[:100]}")
