#!/bin/bash
# Body of a raw help article (checker-style text): from "آخر تحديث" to "سوف تتعلم".
f=$1
python3 -I /tmp/claude-0/-home-user/9f45def8-b710-5f9c-84f3-6a0fa7e617c8/scratchpad/q1n/zid/scripts/htmltext.py "$f" | awk '/آخر تحديث/{p=1} /سوف تتعلم/{p=0} p'
