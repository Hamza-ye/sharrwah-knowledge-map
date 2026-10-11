# Parse the $country_extensions map in PaymentsExtensionSuggestions.php into per-country blocks (line ranges).
# Usage: python3 -I country_map.py RELEASE_ROOT
import re, sys, json
root = sys.argv[1]
path = root + "/src/Internal/Admin/Suggestions/PaymentsExtensionSuggestions.php"
lines = open(path, encoding="utf-8").read().split("\n")
start = next(i for i, l in enumerate(lines) if "private array $country_extensions = array(" in l)
blocks, cur, depth = [], None, 0
for i in range(start + 1, len(lines)):
    l = lines[i]
    m = re.match(r"^\t\t'([A-Z]{2})' => array\(", l)
    if m and cur is None:
        cur = {"cc": m.group(1), "a": i + 1}
        depth = 0
    if cur is not None:
        depth += l.count("(") - l.count(")")
        if depth <= 0:
            cur["b"] = i + 1
            txt = " ".join(x.strip() for x in lines[cur["a"] - 1:cur["b"]])
            cur["text"] = re.sub(r"\s+", " ", txt)
            cur["ids"] = re.findall(r"self::([A-Z_]+)", txt)
            blocks.append(cur)
            cur = None
    if l.startswith("\t);"):
        break
json.dump(blocks, sys.stdout, indent=0)
