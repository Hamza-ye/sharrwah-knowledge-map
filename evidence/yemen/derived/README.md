# Derived renderings

Machine-made renderings of captured files that can't be read as text. They are kept apart so that capture runs stay unedited.

Each folder mirrors a run and an item: `derived/<run>/<item>/` belongs to `runs/<run>/items/<item>/`.

- **`pages/page-NN.jpg`** is every page of the PDF, rendered at 110 dpi (JPEG, quality 75) by `pdftoppm`.
- **`ocr.txt`** is text recognised by Tesseract 5 (Arabic and English) from pages rendered at 200 dpi. Its header names the source file and the source's fingerprint. OCR of a scan makes mistakes, so check any quoted wording against the page images.

These were made for PDFs whose text layer is empty or nearly so: scans and designed artwork. They include several Aden central bank instructions cited in the Yemen report, and Sana'a ministry and Tax Authority guides.

**Added on 12 October 2026**, for six items of the Sana'a rules run that Stage 1's pass 1 couldn't read:
- **Three photographs of documents** (items 016, 026 and 030, from yemeneco.org). Each image is OCR'd as captured, so it has no `pages/` folder: the captured `raw.jpeg` is the page.
- **Three PDFs whose text layer uses a shifted font encoding** (items 041, 047 and 066). Their `text.txt` is unreadable in whole or in part.
