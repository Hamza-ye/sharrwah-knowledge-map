# First prose sentence(s) after the H1 of a markdown page, with links, bold and code marks removed.
import re, sys
sys.path.insert(0, "/tmp/claude-0/-home-user/9f45def8-b710-5f9c-84f3-6a0fa7e617c8/scratchpad/q1n/bigcommerce/scripts")
import bcsrc

def plain(s):
    s = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", s)
    s = s.replace("**", "").replace("`", "").replace("\\", "")
    return re.sub(r"\s+", " ", s).strip()

def first(key, maxlen=300):
    _, files, _, _, _ = bcsrc.resolve(key)
    seen = False
    for l in open(files[0], encoding="utf-8"):
        l = l.strip()
        if l.startswith("# ") and not seen:
            seen = True; continue
        if seen and l and not l.startswith(("#", "```", "|", "![", "[![", "* ", "- ")):
            t = plain(l.lstrip("> ").strip())
            if not t or t.startswith(("This page is for", "For clean Markdown")): continue
            if len(t) <= maxlen: return t
            cut = t[:maxlen]; i = cut.rfind(". ")
            return cut[:i + 1] if i > 60 else cut
    return ""

if __name__ == "__main__":
    for k in sys.argv[1:]:
        print(k, "=>", first(k))
