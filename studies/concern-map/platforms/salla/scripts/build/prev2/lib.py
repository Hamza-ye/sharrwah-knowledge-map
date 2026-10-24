# Shared helpers for the Salla Q1 build: local sources, verbatim quotes, dates.
import json, os, re

OBS = "/home/user/observed-sa"
OUT = "/tmp/claude-0/-home-user/9f45def8-b710-5f9c-84f3-6a0fa7e617c8/scratchpad/q1/salla"
FETCHED = os.path.join(OUT, "fetched")
COMMIT = "145f137"
ACCESSED = "2026-10-10"
MAXQ = 290

_lines = {}


def local_source(rel):
    return f"observed-sa@{COMMIT}:{rel}"


def lines(rel):
    if rel not in _lines:
        with open(os.path.join(OBS, rel), encoding="utf-8") as f:
            _lines[rel] = f.read().split("\n")
    return _lines[rel]


def clean(s):
    return s.replace("\t", " ").replace("\r", " ").replace("\n", " ")


def window(line, needle, maxlen=MAXQ):
    """A verbatim substring of `line` that contains `needle`, at most about maxlen characters."""
    if len(line) <= maxlen:
        return line
    i = line.find(needle)
    if i < 0:
        raise ValueError(f"needle not in line: {needle!r}")
    # start at a key boundary shortly before the needle
    start = i
    j = line.rfind(', "', max(0, i - 100), i)
    if j >= 0:
        start = j + 2
    elif i < 100:
        start = 0
    end = min(len(line), start + maxlen)
    if end < i + len(needle):
        start, end = i, min(len(line), i + maxlen)
    q = line[start:end]
    if end < len(line):
        k = q.rfind(', "')
        if k > (i - start) + len(needle):
            q = q[:k]
    return q


def meta_date(meta):
    """Capture date (YYYY-MM-DD) of a structure from its meta.json."""
    s = meta.get("source", {}) if isinstance(meta.get("source"), dict) else {}
    for k in ("date", "captured", "started", "t", "dateUpdated", "rendered_at"):
        v = s.get(k) or meta.get(k)
        if isinstance(v, str) and re.match(r"20\d\d-\d\d-\d\d", v):
            return v[:10]
    for k in ("run_id", "run"):
        v = s.get(k)
        if isinstance(v, str):
            m = re.match(r"(20\d\d)(\d\d)(\d\d)T", v)
            if m:
                return f"{m.group(1)}-{m.group(2)}-{m.group(3)}"
    runs = s.get("run_ids") or s.get("runs") or []
    dates = []
    for v in runs:
        m = re.match(r"(20\d\d)(\d\d)(\d\d)T", v)
        if m:
            dates.append(f"{m.group(1)}-{m.group(2)}-{m.group(3)}")
    if dates:
        return max(dates)
    return ""


def load_meta(rel_dir):
    p = os.path.join(OBS, rel_dir, "meta.json")
    return json.load(open(p, encoding="utf-8"))


def find_line(rel, needle, start=0):
    """1-based line number of the first line containing needle at or after line index start."""
    ls = lines(rel)
    for n in range(start, len(ls)):
        if needle in ls[n]:
            return n + 1
    raise ValueError(f"{needle!r} not found in {rel}")
