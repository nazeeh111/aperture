**Yes, according to current documentation:** Recoll can recognize scanned body text and keep it in its own search index/OCR cache, without producing replacement PDFs. Crucially, `pdfocr` alone skips a PDF containing any extracted text, so the digital title page would defeat that default route. Set **`pdfforceocr = 1`**: the parameter reference explicitly says OCR runs despite existing text and concatenates OCR output with extracted PDF text. [PDF-handler parameters, entries `pdfocr` and `pdfforceocr`](https://www.recoll.org/usermanual/webhelp/docs/RCL.CONFIG.RECOLLCONF.PDF.html).

Proposed `recoll.conf` settings, scoped to the archive directory:

```ini
[/absolute/path/to/archive]
pdfocr = 1
pdfforceocr = 1
ocrprogs = tesseract
tesseractlang = eng
```

Recoll needs an available OCR engine and appropriate language data. Use Tesseract for the free route; configure `tesseractcmd` if its executable is not discoverable, particularly on Windows. Adjust `tesseractlang` for the archive, e.g. `eng+fra`. Ordinary PDF extraction requires Poppler’s `pdftotext`. [OCR setup](https://recoll.org/usermanual/webhelp/docs/RCL.INDEXING.OCR.html), [OCR configuration, `tesseractlang`/`tesseractcmd`](https://www.recoll.org/usermanual/webhelp/docs/RCL.CONFIG.RECOLLCONF.OCR.html), [features, PDF dependencies](https://www.recoll.org/pages/features.html#_file_types_indexed_with_external_helpers).

Operating limits:

- OCR is slow; budget initial processing time and disk space for both index and separate OCR cache. Unchanged files reuse cached output; content changes trigger OCR again. Cache defaults to `$RECOLL_CONFDIR/ocrcache`. [OCR operation](https://recoll.org/usermanual/webhelp/docs/RCL.INDEXING.OCR.html), [cache setting](https://www.recoll.org/usermanual/webhelp/docs/RCL.CONFIG.RECOLLCONF.OCR.html).
- Original scans remain without an embedded searchable layer. Finding body text through Recoll does not make the original PDF viewer’s search work; the manual identifies native searching and positioning as benefits of modifying PDFs with OCRmyPDF. [PDF OCR note](https://www.recoll.org/usermanual/webhelp/docs/ch02s07s03s01.html).
- Linux Recoll is free; Tesseract is free/open source. Windows binaries request a contribution, with a free download link available by emailing the maintainer. ABBYY is commercial. [Recoll licensing](https://www.recoll.org/), [Tesseract introduction](https://tesseract-ocr.github.io/tessdoc/#introduction), [Windows download terms](https://www.recoll.org/pages/recoll-windows.html).

**Evidence boundary:** documentation checked October 21, 2026; no installation or archive runtime test. OCR accuracy and processing time remain unmeasured for these scans.
