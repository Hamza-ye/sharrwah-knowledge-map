#!/bin/bash
# Page images and OCR text for scanned PDFs, and OCR text for captured images (a photo of a document is its own
# page, so no page images are made for it). Writes to EVIDENCE_ROOT/derived/<run>/<item>/.
# Usage: ocr.sh LIST EVIDENCE_ROOT TMP_DIR   (LIST lines: <run>/items/<item>|<pdf or image path>)
set -u
export OMP_THREAD_LIMIT=1
E=${2:?evidence root, e.g. evidence/yemen}
TMP=${3:?temporary directory}
TV=$(tesseract --version 2>&1 | head -1)
while IFS='|' read -r rel pdf; do
  run=${rel%%/items/*}; item=${rel##*/items/}
  out=$E/derived/$run/$item; tmp=$TMP/$run/$item
  mkdir -p "$tmp"
  case "$pdf" in
    *.pdf)
      mkdir -p "$out/pages"
      pdftoppm -r 110 -jpeg -jpegopt quality=75 "$pdf" "$out/pages/page"
      pdftoppm -r 200 -png "$pdf" "$tmp/p"; how="200 dpi" ;;
    *)
      mkdir -p "$out"
      cp "$pdf" "$tmp/p-1.${pdf##*.}" && convert "$tmp/p-1.${pdf##*.}" "$tmp/p-1.png" 2>/dev/null \
        || cp "$pdf" "$tmp/p-1.png"; how="the image as captured" ;;
  esac
  ls "$tmp"/p-*.png | xargs -P 4 -I{} sh -c 'tesseract "{}" "${1%.png}" -l ara+eng --psm 3 >/dev/null 2>&1' _ {}
  {
    echo "OCR of $rel ($(basename "$pdf"), sha256 $(sha256sum "$pdf" | cut -d' ' -f1))"
    echo "Tool: $TV, languages ara+eng, $how, one thread per page. Machine reading of a scan: expect errors, check against the page images."
    echo
    for t in $(ls "$tmp"/p-*.txt | sort -V); do
      n=$(basename "$t" .txt); echo "=== page ${n#p-} ==="; cat "$t"; echo
    done
  } > "$out/ocr.txt"
  echo "$rel pages=$(ls "$tmp"/p-*.txt | wc -l) ocr_chars=$(wc -c < "$out/ocr.txt")"
  rm -rf "$tmp"
done < "${1:?list file}"
