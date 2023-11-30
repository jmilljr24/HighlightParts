import fitz
import re
from io import BytesIO
import random
import argparse


input_file = "pdfs/50_10-ocr.pdf"
output_file = "test.pdf"

parts_re = re.compile(r"[A-Z]{1,2}-\d{3,5}[A-Z]?(-[LR])?")

#Setup for pdf scan
pdfDoc = fitz.open(input_file)
# Iterate through pages
count = 0
for pg in range(pdfDoc.page_count):
    # print("Page: " + str(pg + 1))
        # Select the page
    page = pdfDoc[pg]
    words = page.get_text("words")
    # parts = page.search_for(parts_re, quads=True)
    matches = [w for w in words if parts_re.findall(w[4])]
    for m in matches:
        print(m[4])
    
    count += len(matches)

    for val in matches:
        matching_val_area = page.search_for(val[4], quads=True)
        highlight = None
        highlight = page.add_highlight_annot(matching_val_area)
        highlight.set_colors(stroke= fitz.utils.getColor("yellow"))
        highlight.update(opacity= 0.5)

# print(count)