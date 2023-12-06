import fitz
import re
from io import BytesIO
import random
import argparse
import math
import os
from pathlib import Path

#Color list for highlights
cl = ['deeppink', 'pink3', 'magenta', 'darkorchid2', 'maroon',
      'slateblue', 'steelblue', 'deepskyblue', 'cyan', 'cyan3', 'aquamarine3',  'royalblue2',
      'green', 'limegreen', 'chartreuse1', 'yellowgreen', 
       'khaki4', 
      'gold2', 'darkgoldenrod3', 
      'orange', 'darkorange1', 'orangered','orangered3', 'salmon3',
      'red3', 'indianred3',
      'snow4']


# input_file = "pdfs/09_10.pdf"
# output_file = "test.pdf"
parts_re = re.compile(r"[A-Z]{1,2}-\d{3,5}[A-Z]?(-[L|R])?")  # need to exclude "(" at beginning tried ^[^\(] but did not work on 07_10. 06_10 was was successfully
#Command line arguments
# argParser = argparse.ArgumentParser()
# argParser.add_argument("-i", "--input", help="Input file path")
# argParser.add_argument("-o", "--output", help="Output file path")
# args = argParser.parse_args()
# input_file = args.input
# output_file = args.output

def extract_info(input_file: str):
    """
    Extracts file info
    """
    # Open the PDF
    pdfDoc = fitz.open(input_file)
    output = {
        "File": input_file, "Encrypted": ("True" if pdfDoc.isEncrypted else "False")
    }
    # If PDF is encrypted the file metadata cannot be extracted
    if not pdfDoc.isEncrypted:
        for key, value in pdfDoc.metadata.items():
            output[key] = value
    # To Display File Info
    print("## File Information ##################################################")
    print("\n".join("{}:{}".format(i, j) for i, j in output.items()))
    print("######################################################################")
    return True, output

# Add key/value pair for unique parts
def colorize(part, color_dict, uniq_parts):
    if part not in color_dict:
        color_dict[part] = cl[uniq_parts] if len(color_dict) < len(cl) else 'yellow'
        return 1
    return 0

def lr_highlight(matched_values, border_color, page):
    for val in matched_values:
        shape = page.new_shape()
        matching_val_area = page.search_for(val, quads=True)
        for quad in matching_val_area:
            #Adjust border position/size
            ul = quad.ul
            ul_big = fitz.Point(ul[0] + 2, ul[1])
            ll_big = fitz.Point(ul[0] + 2, ul[1] + 13)
            lr_big = fitz.Point(ul[0] + 13, ul[1] + 13)
            ur_big = fitz.Point(ul[0] + 13, ul[1])
            big_quad = fitz.Quad(ul_big, ll_big, ur_big, lr_big)
            #Draw colored border around '-L' and '-R'
            page.draw_quad(big_quad, color= fitz.utils.getColor(border_color))
            shape.commit()


def highlight_left(left_parts, page):
    lr_highlight(left_parts, 'darkred', page)
    
def highlight_right(right_parts, page):
    lr_highlight(right_parts, 'chartreuse4', page)

def uniq_page_parts(matches):
    clean_parts = set()
    left_right_parts = set()
    for val in matches:
        #remove unnecessary beginning and trailing characters
        string = val[4].strip("(,")
        part =  re.findall(r"[A-Z]{1,2}-\d{3,5}[A-Z]?", string)
        clean_parts.add(part[0])
        #find left/right parts
        lr = re.search(r"-[R|L]", string)
        if lr:
            left_right_parts.add(lr.string)
    return [clean_parts, left_right_parts]

def process_file(**kwargs):
    """
    To process one single file
    Highlight one PDF File

    """
    input_file = kwargs.get('input_file')
    output_file = kwargs.get('output_file')
    if output_file is None:
        output_file = Path(input_file).stem + '_colored.pdf'

    #highlight
    process_data(input_file=input_file, output_file=output_file)

def process_folder(**kwargs):
    """
    Highlight all PDF Files within a specified path
    """
    input_folder = kwargs.get('input_folder')

    #Highlight
    # Loop though the files within the input folder.
    for foldername, dirs, filenames in os.walk(input_folder):
        for filename in filenames:
            # Check if pdf file
            if not filename.endswith('.pdf'):
                continue
             # PDF File found
            inp_pdf_file = os.path.join(foldername, filename)
            print("Processing file =", inp_pdf_file)
            process_file(input_file=inp_pdf_file, output_file=None)

def is_valid_path(path):
    """
    Validates the path inputted and checks whether it is a file path or a folder path
    """
    if not path:
        raise ValueError(f"Invalid Path")
    if os.path.isfile(path):
        return path
    elif os.path.isdir(path):
        return path
    else:
        raise ValueError(f"Invalid Path {path}")
    
def is_valid_path(path):
    """
    Validates the path inputted and checks whether it is a file path or a folder path
    """
    if not path:
        raise ValueError(f"Invalid Path")
    if os.path.isfile(path):
        return path
    elif os.path.isdir(path):
        return path
    else:
        raise ValueError(f"Invalid Path {path}")


def parse_args():
    """Get user command line parameters"""
    parser = argparse.ArgumentParser(description="Available Options")
    parser.add_argument('input_path', type=is_valid_path,
                        help="Enter the path of the file or the folder to process")
    path = parser.parse_known_args()[0].input_path
    if os.path.isfile(path):
        parser.add_argument('-o', '--output_file', dest='output_file', type=str  # lambda x: os.path.has_valid_dir_syntax(x)
                            , help="Enter a valid output file")
    if os.path.isdir(path):
        parser.add_argument('-r', '--recursive', dest='recursive', default=False, type=lambda x: (
            str(x).lower() in ['true', '1', 'yes']), help="Process Recursively or Non-Recursively")
    args = vars(parser.parse_args())
    # To Display The Command Line Arguments
    print("## Command Arguments #################################################")
    print("\n".join("{}:{}".format(i, j) for i, j in args.items()))
    print("######################################################################")
    return args





def last_letter(word):
    return word[::-1]

#Setup for pdf scan
# pdfDoc = fitz.open(input_file)
#Print page count of input PDF
# num_pages = pdfDoc.page_count
# print( str(num_pages) + " pages to process...")

# Iterate through pages
# count = 0
# output_buffer = BytesIO()

def process_data(input_file: str, output_file: str):
    pdfDoc = fitz.open(input_file)
    count = 0
    output_buffer = BytesIO()
    for pg in range(pdfDoc.page_count):
        print('Page: ' + str(pg + 1))
        # Select the page

        page = pdfDoc[pg]

        page_lines = page.get_text("text").split('\n')
        for line in page_lines:
            left_result = re.findall("-L", line)
            highlight_left(left_result, page)
            right_result = re.findall("-R", line)
            highlight_right(right_result, page)
        #Randomize color list
        random.shuffle(cl)

        #Process page for parts
        words = page.get_text("words")
        matches = [w for w in words if parts_re.findall(w[4])]
        uniq = uniq_page_parts(matches)
        # for m in matches:
        #     print(m[4])
        
        count += len(matches)

        color_dict = {}
        uniq_parts = 0
        base_set = uniq[0]
        s = sorted(base_set)

        contains_highlight = set()
        contains_highlight.clear()
        for part_num in reversed(s):
    
            uniq_parts += colorize(part_num, color_dict, uniq_parts)
            matching_val_area = page.search_for(part_num, quads=True)
            point = None
            set_positions = list()
            for quad in range(len(matching_val_area)):
                llx = math.trunc(matching_val_area[quad].ll[0])
                lly = math.trunc(matching_val_area[quad].ll[1])
                point = frozenset([llx, lly])
                if point not in contains_highlight:
                    position = fitz.Quad(matching_val_area[quad])
                    set_positions.append(position)
                    contains_highlight.add(point)

            highlight = None
            highlight = page.add_highlight_annot(set_positions)
            highlight.set_colors(stroke= fitz.utils.getColor(color_dict[part_num]))
            highlight.update(opacity= 0.5)

    print(str(count) + ' Matches found')
    # Save to output
    pdfDoc.save(output_buffer)
    pdfDoc.close()
# Save the output buffer to the output file
    with open(output_file, mode='wb') as f:
        f.write(output_buffer.getbuffer())


if __name__ == '__main__':
    # Parsing command line arguments entered by user
    args = parse_args()
    # If File Path
    if os.path.isfile(args['input_path']):
        # Extracting File Info
        extract_info(input_file=args['input_path'])
        # Process a file
        process_file(
            input_file=args['input_path'], output_file=args['output_file']
        )
    # If Folder Path
    elif os.path.isdir(args['input_path']):
        # Process a folder
        process_folder(
            input_folder=args['input_path']
        )