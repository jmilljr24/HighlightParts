import fitz
import re
from io import BytesIO
import random
import argparse

#Color list for highlights
cl = ['deeppink', 'pink3', 'magenta', 'darkorchid2', 'maroon',
      'slateblue', 'steelblue', 'deepskyblue', 'cyan', 'cyan3', 'aquamarine3',  'royalblue2',
      'green', 'limegreen', 'chartreuse1', 'yellowgreen', 
       'khaki4', 
      'gold2', 'darkgoldenrod3', 
      'orange', 'darkorange1', 'orangered','orangered3', 'salmon3',
      'red3', 'indianred3',
      'snow4']


input_file = "pdfs/06_10.pdf"
output_file = "test.pdf"
parts_re = re.compile(r"[A-Z]{1,2}-\d{3,5}[A-Z]?(-[LR])?")  # need to exclude "(" at beginning tried ^[^\(] but did not work on 07_10. 06_10 was was successfully

# Add key/value pair for unique parts
def colorize(part):
    if part not in color_dict:
        color_dict[part] = cl[uniq_parts]
        return 1
    return 0


#Setup for pdf scan
pdfDoc = fitz.open(input_file)
#Print page count of input PDF
num_pages = pdfDoc.page_count
print( str(num_pages) + " pages to process...")

# Iterate through pages
count = 0
output_buffer = BytesIO()

for pg in range(pdfDoc.page_count):
    # Select the page
    page = pdfDoc[pg]

    #Randomize color list
    random.shuffle(cl)

    #Process page for parts
    words = page.get_text("words")
    matches = [w for w in words if parts_re.findall(w[4])]

    for m in matches:
        print(m[4])
    print(len(matches))
    count += len(matches)

    color_dict = {}
    uniq_parts = 0
    for val in matches:
        part_num = val[4]
        uniq_parts += colorize(part_num)
        matching_val_area = page.search_for(part_num, quads=True)

        highlight = None
        highlight = page.add_highlight_annot(matching_val_area)
        highlight.set_colors(stroke= fitz.utils.getColor(color_dict[part_num]))
        highlight.update(opacity= 0.5)

print(count)
# Save to output
pdfDoc.save(output_buffer)
pdfDoc.close()
# Save the output buffer to the output file
with open(output_file, mode='wb') as f:
    f.write(output_buffer.getbuffer())