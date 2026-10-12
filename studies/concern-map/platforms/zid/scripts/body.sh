#!/bin/bash
# Print the article body of a rendered help page (from the date line to the end of the article).
f=$1
awk '/آخر تحديث/{on=1} on{print} /^سوف تتعلم|^التقييمات والمراجعات/{if(on) exit}' "$f" | grep -v '^\s*$'
