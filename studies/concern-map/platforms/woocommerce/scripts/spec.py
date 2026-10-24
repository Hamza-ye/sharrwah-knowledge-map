# Small vocabulary for concern specs.
#   C(id, concern, terms, split_note, match=[(list_regex, entry_regex), ...], software=..., decides=..., legal=..., boundary=..., reason=...)
#   S(value, refs, note="")  a placement shown by the cited sources
#   N(note="")               a placement not shown
# refs: citation keys from out/cite_keys.json, cite ids "WC-S-nnnn", or I(list_regex, entry_regex) for inventory citations.
import json, os, re
HERE = os.path.dirname(os.path.abspath(__file__))
CONCERNS = []
_inv = None


def inventory():
    global _inv
    if _inv is None:
        rel = json.load(open(os.path.join(HERE, "out", "inv_release_cited.json")))
        live = json.load(open(os.path.join(HERE, "out", "inv_live.json")))
        _inv = rel + live
        for n, r in enumerate(_inv, 1):
            r["inv_id"] = f"WC-I-{n:04d}"
    return _inv


class I:
    """Citation(s) of inventory rows matching (list regex, entry regex)."""
    def __init__(self, lst, entry):
        self.lst, self.entry = lst, entry

    def ids(self):
        out = [r["cite_id"] for r in inventory() if re.search(self.lst, r["list"]) and re.search(self.entry, r["entry"])]
        if not out:
            raise LookupError(f"no inventory row for {self.lst} / {self.entry}")
        return out


def S(value, refs, note=""):
    if not refs:
        raise ValueError(f"shown placement without citations: {value}")
    return dict(value=value, status="shown", refs=refs if isinstance(refs, list) else [refs], note=note)


def N(note=""):
    return dict(value="", status="not shown", refs=[], note=note)


def C(cid, concern, terms, split_note="", match=None, software=None, decides=None, legal=None, boundary=None, reason=None):
    for name, p in [("software", software), ("decides", decides), ("legal", legal), ("boundary", boundary), ("reason", reason)]:
        if p is None:
            raise ValueError(f"{cid}: missing placement {name}")
    if any(c["id"] == cid for c in CONCERNS):
        raise ValueError(f"duplicate concern id {cid}")
    CONCERNS.append(dict(id=cid, concern=concern, terms=terms, split_note=split_note, match=match or [],
                         placements=dict(software=software, decides=decides, legal=legal, boundary=boundary, reason=reason)))
