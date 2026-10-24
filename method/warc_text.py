# Prints one record of a fetch archive (WARC) held in git: the HTTP body as the site sent it, decoded.
# With --text, an HTML body is printed as its text (block tags break lines; scripts and styles dropped).
#
# Usage: python3 -I method/warc_text.py REPO_ROOT WARC_PATH@OFFSET [--text]
#   e.g. python3 -I method/warc_text.py /home/user/observed-sa raw/runs/20261006T030341Z-com-toplevel/fetch.warc.gz@15012459 --text
# The location is the one method/held_index.py reports. A citation to it names the repository at its commit,
# the archive path and offset, the record's target URI and the sha256 of the decoded body (printed to stderr).
import gzip, hashlib, html, os, re, sys, zlib

def read_record(path, offset):
    with open(path, "rb") as f:
        return read_record_fp(f, offset)

def read_record_fp(f, offset):
    """The record at offset in a seekable fetch archive: (WARC headers, HTTP status line, HTTP headers, body)."""
    f.seek(offset)
    d = zlib.decompressobj(16 + zlib.MAX_WBITS)   # one gzip member holds one WARC record
    out = b""
    while not d.eof:
        chunk = f.read(65536)
        if not chunk:
            break
        out += d.decompress(chunk)
    head, _, rest = out.partition(b"\r\n\r\n")
    warc = dict(l.split(": ", 1) for l in head.decode("utf-8", "replace").split("\r\n")[1:] if ": " in l)
    http_head, _, body = rest.partition(b"\r\n\r\n")
    hh = http_head.decode("iso-8859-1").split("\r\n")
    headers = {l.split(":", 1)[0].strip().lower(): l.split(":", 1)[1].strip() for l in hh[1:] if ":" in l}
    if "chunked" in headers.get("transfer-encoding", "").lower():
        body, rest = b"", body
        while True:
            size_line, _, rest = rest.partition(b"\r\n")
            size = int(size_line.split(b";")[0] or b"0", 16)
            if size == 0:
                break
            body, rest = body + rest[:size], rest[size + 2:]
    enc = headers.get("content-encoding", "").lower()
    if enc == "gzip":
        body = gzip.decompress(body)
    elif enc == "br":
        raise ValueError("the body is brotli-encoded; install brotli to read it")
    return warc, hh[0], headers, body

def html_text(raw):
    raw = re.sub(r"(?is)<(script|style|noscript)[^>]*>.*?</\1>", " ", raw)
    raw = re.sub(r"(?is)</?(p|div|li|ul|ol|br|hr|h[1-6]|tr|td|th|table|section|article|header|footer|nav|main|aside|blockquote|pre|dd|dt|dl)\b[^>]*>", "\n", raw)
    raw = html.unescape(re.sub(r"(?s)<[^>]+>", "", raw))
    return "\n".join(l.strip() for l in raw.splitlines() if l.strip())

if __name__ == "__main__":
    root, loc = sys.argv[1], sys.argv[2]
    path, _, off = loc.rpartition("@")
    warc, status, headers, body = read_record(os.path.join(root, path), int(off))
    print(f"{warc.get('WARC-Target-URI', '')} | {status} | sha256 {hashlib.sha256(body).hexdigest()} | {len(body)} bytes",
          file=sys.stderr)
    text = body.decode(re.search(r"charset=([\w-]+)", headers.get("content-type", "")) and
                       re.search(r"charset=([\w-]+)", headers["content-type"]).group(1) or "utf-8", "replace")
    print(html_text(text) if "--text" in sys.argv[3:] else text)
