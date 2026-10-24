# Print the main text of a captured page: from the second occurrence of its title (page heading) on.
# Usage: python3 -I main_text.py TXT_FILE [CHARS] [START_MARKER]
import sys, textwrap
t = open(sys.argv[1]).read()
n = int(sys.argv[2]) if len(sys.argv) > 2 else 4000
if len(sys.argv) > 3:
    i = t.find(sys.argv[3])
else:
    title = t.split(" Documentation - ")[0].split(" - WooCommerce")[0][:60]
    i = t.find(title, len(title))
    i = t.find(title, i + 1) if t.find(title, i + 1) > 0 else i
print(len(t), i)
print("\n".join(textwrap.wrap(t[max(i, 0):max(i, 0) + n], 240)))
