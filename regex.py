import fitz
import re
from io import BytesIO

################################################################
# This file can be use to test the regex. The output of every match is printed 
# and the output file has all matches highlighted in yellow.
################################################################

input_file = "pdfs/25_10.pdf"
output_file = "test.pdf"

parts_re = re.compile(r"[A-Z]{1,2}-\d{3,5}[A-Z]?(-[LR])?")

#Setup for pdf scan
pdfDoc = fitz.open(input_file)
output_buffer = BytesIO()
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

print(str(count) + ' Matches found')
# Save to output
pdfDoc.save(output_buffer)
pdfDoc.close()
# Save the output buffer to the output file
with open(output_file, mode='wb') as f:
    f.write(output_buffer.getbuffer())