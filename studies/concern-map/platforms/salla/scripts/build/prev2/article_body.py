# Print the body of a rendered help.salla.sa article: from the breadcrumb before the title
# to the closing support line, dropping the site navigation tree and footer.
# Usage: python3 -I article_body.py FILE [FILE ...]
import sys

END_MARKERS = ("اسأل, واطلب الدعم", "Ask, and get support", "Ask and get support")

for path in sys.argv[1:]:
    lines = open(path, encoding="utf-8").read().split("\n")
    # the article title appears twice in a row after the breadcrumb; find the date line
    start = 0
    for i, l in enumerate(lines):
        if l.startswith("تاريخ اخر تحديث") or l.startswith("تاريخ آخر تحديث") or l.lower().startswith("last update"):
            start = max(0, i - 6)
            break
    else:
        # fall back: first repeated line pair (title twice)
        for i in range(1, len(lines)):
            if lines[i] and lines[i] == lines[i - 1] and len(lines[i]) > 8:
                start = max(0, i - 4)
                break
    end = len(lines)
    for j in range(start, len(lines)):
        if any(lines[j].startswith(m) for m in END_MARKERS):
            end = j + 1
            break
    print(f"##### {path.rsplit('/', 1)[-1]}  (lines {start + 1}-{end})")
    out = []
    for l in lines[start:end]:
        if l.strip() == "" and out and out[-1].strip() == "":
            continue
        out.append(l)
    print("\n".join(out))
