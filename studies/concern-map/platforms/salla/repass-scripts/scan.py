# Scans help-article working copies (article body only) for sentences that may state a reason,
# a responsibility or a boundary. Prints them per article for a person to read; it decides nothing.
# Usage: python3 -I scan.py LIST_FILE
import sys, os, re, urllib.parse
SP = "/tmp/claude-0/-home-user/9f45def8-b710-5f9c-84f3-6a0fa7e617c8/scratchpad/q1r/salla"
MARK = {
 "reason": r"لماذا|لأن|لان |بهدف|يهدف|تهدف|لضمان|حرص|نظرًا|نظراً|بسبب|لأسباب|من أجل|حتى لا|لتجنب|لتفادي|يساعد|تساعد|يتيح لك",
 "responsible": r"مسؤول|يتحمل|تتحمل|يلتزم|تلتزم|ملزم|عقد|اتفاقية|سياسة|شروط|الطرف|بالنيابة|نيابة|طرف ثالث|مزود|شركة سلة|تخلي|إخلاء",
 "boundary": r"API|Webhook|ويب هوك|ربط|يرتبط|ينعكس|تنعكس|تلقائي|مزامنة|محفظة|رصيد|تطبيق|الطلبات|إشعار",
}
def body(path):
    lines = open(path, encoding="utf-8").read().split("\n")
    s = next((i for i, l in enumerate(lines) if "تاريخ اخر تحديث" in l), 0)
    e = next((i for i in range(s, len(lines)) if lines[i].startswith("اسأل, واطلب الدعم") or lines[i].strip() == "تصنيفات ذات صلة"), len(lines))
    return [(i + 1, lines[i]) for i in range(max(0, s - 3), e) if lines[i].strip()]
for u in [l.strip() for l in open(sys.argv[1], encoding="utf-8") if l.startswith("http")]:
    p = urllib.parse.urlparse(u)
    s = urllib.parse.unquote(p.path).strip("/").replace("/", "_")
    s = re.sub(r"[^\w؀-ۿ.\-]+", "-", s)[-120:]
    f = f"{SP}/fetched/{p.netloc}/{s}.txt"
    if not os.path.exists(f):
        print("MISSING", u); continue
    b = body(f)
    date = next((l for _, l in b if "تاريخ اخر تحديث" in l), "")
    print("=" * 8, urllib.parse.unquote(u).replace("https://help.salla.sa/article/", ""), "|", date.strip())
    for n, l in b:
        tags = [k for k, rx in MARK.items() if re.search(rx, l)]
        if "reason" in tags or "responsible" in tags:
            print(f"  {n} [{','.join(t[:4] for t in tags)}] {l.strip()[:260]}")
