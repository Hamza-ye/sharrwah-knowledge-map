"""Print the decoded body of one response in a WARC to stdout; its metadata to stderr as JSON.

    .venv/bin/python capture/warcbody.py <warc.gz> <target-uri>

A run's fetch.warc.gz may be held as the parts capture/warc_split.py cut it into (fetch-00000.warc.gz, ...):
warc_files() names the files that hold it, open_warc() reads them in order as the one WARC.
"""
import hashlib
import io
import json
import sys
from pathlib import Path

from warcio.archiveiterator import ArchiveIterator


def warc_files(warc):
    """The files holding a WARC: the file itself, or the parts cut from it, in order."""
    p = Path(warc)
    if p.exists():
        return [p]
    parts = sorted(p.parent.glob(p.name.replace('.warc.gz', '-[0-9][0-9][0-9][0-9][0-9].warc.gz')))
    if not parts:
        raise FileNotFoundError(warc)
    return parts


class _Parts(io.RawIOBase):
    """The parts read one after the other: their bytes in order are the WARC as fetched."""

    def __init__(self, paths):
        self._files, self._i, self._pos = [open(p, 'rb') for p in paths], 0, 0

    def readable(self):
        return True

    def readinto(self, b):
        while self._i < len(self._files):
            n = self._files[self._i].readinto(b)
            if n:
                self._pos += n
                return n
            self._i += 1
        return 0

    def tell(self):
        return self._pos

    def close(self):
        for f in self._files:
            f.close()
        super().close()


def open_warc(warc):
    files = warc_files(warc)
    return open(files[0], 'rb') if len(files) == 1 else _Parts(files)


def find(warc, uri):
    """The first response for uri; meta's warc is the file that holds it (a part, when the WARC is cut)."""
    for part in warc_files(warc):
        with open(part, 'rb') as f:
            for r in ArchiveIterator(f):
                if r.rec_type == 'response' and r.rec_headers.get_header('WARC-Target-URI') == uri:
                    body = r.content_stream().read()
                    meta = {
                        'warc': warc if Path(warc) == part else str(part), 'uri': uri,
                        'record_id': r.rec_headers.get_header('WARC-Record-ID'),
                        'date': r.rec_headers.get_header('WARC-Date'), 'status': r.http_headers.get_statuscode(),
                        'content_type': r.http_headers.get_header('Content-Type'), 'bytes': len(body),
                        'sha256': hashlib.sha256(body).hexdigest(),
                    }
                    return body, meta
    return None, None


if __name__ == '__main__':
    body, meta = find(sys.argv[1], sys.argv[2])
    if body is None:
        sys.exit(f'not found: {sys.argv[2]}')
    sys.stderr.write(json.dumps(meta) + '\n')
    sys.stdout.buffer.write(body)
