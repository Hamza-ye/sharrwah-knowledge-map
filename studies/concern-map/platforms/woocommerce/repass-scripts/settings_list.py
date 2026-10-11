# List setting arrays in WooCommerce settings classes: id, type, default with line numbers.
# Usage: python3 -I settings_list.py RELEASE_ROOT FILE [FILE...]
import re, sys
root = sys.argv[1]
for rel in sys.argv[2:]:
    lines = open(f"{root}/{rel}", encoding="utf-8").read().split("\n")
    i = 0
    while i < len(lines):
        m = re.search(r"'id'\s*=>\s*([^,]+),", lines[i])
        if m:
            # look back for 'array(' start and forward for type/default/title until the closing '),'
            a = i
            while a > 0 and not re.search(r"array\(\s*$", lines[a]) and i - a < 12:
                a -= 1
            b = i
            info = {}
            depth = 0
            for j in range(a, min(len(lines), i + 40)):
                for key in ("title", "desc", "type", "default"):
                    mm = re.search(rf"'{key}'\s*=>\s*(.+?),?\s*$", lines[j])
                    if mm and key not in info:
                        info[key] = (j + 1, mm.group(1)[:90])
                if j > i and re.match(r"^\s*\),\s*$", lines[j]):
                    b = j
                    break
            print(f"{rel}:{a+1}-{b+1} id={m.group(1)} " + " ".join(f"{k}@{v[0]}={v[1]}" for k, v in info.items() if k in ("type", "default")))
        i += 1
