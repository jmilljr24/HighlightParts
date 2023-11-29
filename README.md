# HighlightParts


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
hightlight.py [-h] [-i INPUT] [-o OUTPUT]

options:

-h, --help show this help message and exit

-i INPUT, --input INPUT       

Input file path


-o OUTPUT, --output OUTPUT    

Output file path


## Example from command line:

```
python3 hightlight.py -i test.pdf -o test_output.pdf
```
