import fitz
import re
from io import BytesIO
import random
import argparse

input_file = "06_10.pdf"
output_file = "test.pdf"

parts_re = re.compile(r"[A-Z]{1,2}-\d{3,5}[A-Z]?(-[LR])?")

#Setup for pdf scan
pdfDoc = fitz.open(input_file)
# Iterate through pages
for pg in range(pdfDoc.page_count):
        # Select the page
    page = pdfDoc[pg]
    words = page.get_text("words")
    # parts = page.search_for(parts_re, quads=True)
    matches = [w for w in words if parts_re.findall(w[4])]
    for m in matches:
        print(m)