# Extract the strings pushed with self.__next_f.push([1,"..."]) in a Next.js page, decoded, for reading.
import sys, re, json
raw = open(sys.argv[1], encoding="utf-8", errors="replace").read()
out = []
for m in re.finditer(r'self\.__next_f\.push\(\[1,("(?:[^"\\]|\\.)*")\]\)', raw):
    try:
        out.append(json.loads(m.group(1)))
    except Exception as e:
        out.append("<<undecodable>>")
print("\n".join(out))
