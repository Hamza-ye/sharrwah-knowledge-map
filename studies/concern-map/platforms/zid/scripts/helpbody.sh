#!/bin/bash
# Print the article body of a rendered help page: from the title line before "آخر تحديث" to the first "تواصل معنا" after it.
f=$1
s=$(grep -n -m1 'آخر تحديث' "$f" | cut -d: -f1)
[ -z "$s" ] && s=20
e=$(awk -v s="$s" 'NR>s && /^(تواصل معنا|هل كانت هذه المقالة مفيدة|مقالات ذات صلة)/ {print NR; exit}' "$f")
[ -z "$e" ] && e=$(wc -l < "$f")
sed -n "$((s-3)),$((e-1))p" "$f" | grep -v '^\s*$'
