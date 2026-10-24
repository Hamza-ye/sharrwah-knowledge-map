# Print question + answer block of a rendered help FAQ page: the block after the last occurrence of the question title.
import sys, re
for p in sys.argv[1:]:
    lines = [l.strip() for l in open(p, encoding="utf-8").read().split("\n")]
    # title is the line after 'مركز المساعدة'
    t = next((l.split("مركز المساعدة", 1)[1].strip() for l in lines if l.startswith("مركز المساعدة") and len(l) > 20), "")
    idx = [i for i, l in enumerate(lines) if t and l.strip() == t]
    print("########", p.rsplit("/", 1)[-1], "|", t)
    if idx:
        i = idx[-1]
        out = []
        for l in lines[i+1:i+25]:
            if re.match(r"^(هل كانت|سوف تتعلم|مقالات|التقييمات|تواصل معنا|الأسئلة الشائعة ذات|أسئلة ذات)", l): break
            if l: out.append(l)
        print("\n".join(out[:14]))
