# Highlight Parts

### Requirements:

Ensure Python3 is installed on your system

Required Packages:

- PyMuPDF==1.23.6
- PyMuPDFb==1.23.6
- argparse==1.4.0

```
pip install pymupdf argparse
```

### Usage:

highlight.py [-h] input_path

positional arguments:

input_path Enter the path of the file or the folder to process

options:

-h, --help show this help message and exit

-o OUTPUT, --output OUTPUT

Output file path

## Example from command line:

```
python3 highlight.py test.pdf -o test_output.pdf
```

```
python3 highlight.py pdf_folder
```

## Testing

Test regex results with regex.py

Output is all results and highlighted in yellow
