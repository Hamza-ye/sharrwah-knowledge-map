import sys, re, collections
p = sys.argv[1]
sec = None
groups = collections.OrderedDict()
for line in open(p, encoding="utf-8"):
    line = line.rstrip("\n")
    if line.startswith("## "):
        sec = line[3:]; continue
    m = re.match(r"^- (.*?)\[([^\]]*)\]\((https://[^)]*)\)", line)
    if not m: continue
    crumb = m.group(1).strip()
    groups.setdefault((sec, crumb), []).append(m.group(2))
for (sec, crumb), names in groups.items():
    print(f"{sec} | {crumb or '(top)'} | {len(names)} | {'; '.join(names)[:200]}")
