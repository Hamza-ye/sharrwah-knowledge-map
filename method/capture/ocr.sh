#!/bin/bash
# Page images and OCR text for scanned PDFs. Writes to EVIDENCE_ROOT/derived/<run>/<item>/.
# Usage: ocr.sh LIST EVIDENCE_ROOT TMP_DIR   (LIST lines: <run>/items/<item>|<pdf path>)
set -u
export OMP_THREAD_LIMIT=1
E=${2:?evidence root, e.g. evidence/yemen}
TMP=${3:?temporary directory}
TV=$(tesseract --version 2>&1 | head -1)
while IFS='|' read -r rel pdf; do
  run=${rel%%/items/*}; item=${rel##*/items/}
  out=$E/derived/$run/$item; tmp=$TMP/$run/$item
  mkdir -p "$out/pages" "$tmp"
  pdftoppm -r 110 -jpeg -jpegopt quality=75 "$pdf" "$out/pages/page"
  pdftoppm -r 200 -png "$pdf" "$tmp/p"
  ls "$tmp"/p-*.png | xargs -P 4 -I{} sh -c 'tesseract "{}" "${1%.png}" -l ara+eng --psm 3 >/dev/null 2>&1' _ {}
  {
    echo "OCR of $rel ($(basename "$pdf"), sha256 $(sha256sum "$pdf" | cut -d' ' -f1))"
    echo "Tool: $TV, languages ara+eng, 200 dpi, one thread per page. Machine reading of a scan: expect errors, check against the page images."
    echo
    for t in $(ls "$tmp"/p-*.txt | sort -V); do
      n=$(basename "$t" .txt); echo "=== page ${n#p-} ==="; cat "$t"; echo
    done
  } > "$out/ocr.txt"
  echo "$rel pages=$(ls "$out/pages" | wc -l) ocr_chars=$(wc -c < "$out/ocr.txt")"
  rm -rf "$tmp"
done < "${1:?list file}"
