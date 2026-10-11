# Preview: python3 -I scripts/sent.py URL FRAGMENT [N_SENT]
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from weblib import *
s = sentence(sys.argv[1], sys.argv[2], int(sys.argv[3]) if len(sys.argv) > 3 else 1)
print(repr(s)); print(check_quote(s, sys.argv[1]))
