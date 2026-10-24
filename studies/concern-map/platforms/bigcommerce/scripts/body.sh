#!/bin/bash
# Print a rendered commerce.com page without blank lines, cookie banner, header nav and footer.
grep -v '^\s*$' "$1" | grep -v '^﻿$' | awk 'f==0 && /^Contact Us$/ {c++; if(c==2){f=1; next}} f==1 && /^Company$/ {exit} f==1 {print}'
