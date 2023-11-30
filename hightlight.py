
import fitz
import re
from io import BytesIO
import random
import argparse





parts = ["VENT SV-10", "E-1001A", "E-1001B", "E-1002", "E-1007", "E-1008", "E-1015", "E-1017", "E-1018", "E-1019", "E-1020", "E-1022", "E-614", "E-615PP", "E-616PP", "E-903", "E-904", "E-905", "E-910", "E-912", "E-913", "E-917", "E-918", "E-919", "E-920", "E-921", "E-DRILL BUSHING", "ES MSTS-8A", "F-1002", "F-1006", "F-1006A", "F-1006B", "F-1006C", "F-1006D", "F-1006E", "F-1006F", "F-1007", "F-1008", "F-1009", "F-1010A", "F-1010B", "F-1010C", "F-10103A", "F-10103B", "F-1011", "F-1011A", "F-1011C", "F-1011E", "F-1012", "F-1012A", "F-1012B", "F-1012E", "F-1014", "F-1015A", "F-1015B", "F-1028", "F-1029", "F-1032", "F-1035", "F-1036", "F-1037A", "F-1037B", "F-1037C", "F-1047", "F-1055", "F-1056", "F-1074", "F-1073", "F-1075", "F-1078", "F-1079", "F-1085", "F-1089", "F-1090", "F-1091", "F-1094A", "F-1095", "F-1095A", "F-1095B", "F-1095D", "F-1095E", "F-1095F", "F-1098", "F-635", "F-636", "F-824B", "F-8105", "FOAM,PVC-750X2X5.25", "HS-1001", "HS-1002", "HS-1003", "HS-1004", "HS-1007", "HS-1008", "HS-1013", "HS-1014", "HS-1015", "HS-1016", "HS-904", "HS-905", "HS-906", "HS-910", "HS-911", "HS-912", "J-CHANNELX6'", "J-CHANNELX8'", "K1000-08", "K1000-3", "K1100-06", "K1100-08", "PS UHMW-125X1/2X2", "PS UHMW-125X1X2", "R-01007A-1", "R-01007B-1", "R-1001", "R-1002", "R-1003", "R-1004A", "R-1004B", "R-1005", "R-1006", "R-1009", "R-1010", "R-1011", "R-1012", "R-1014", "R-1015", "R-607PP", "R-608PP", "RIVET AD-41-ABS", "RIVET CCR-264SS-3-2", "RIVET CS4-4", "RIVET LP4-3", "RIVET MK-319-BS", "RIVET MSP-42", "TRIM BUNDLE, EMP", "VA-101", "VA-111", "VA-137", "VA-140", "VA-146", "VA-169", "VS-01010-1", "VS-1001", "VS-1002", "VS-1003", "VS-1004", "VS-1005", "VS-1006", "VS-1007", "VS-1008", "VS-1009", "VS-1011", "VS-1012", "VS-1013", "VS-1014", "VS-1015", "VS-1016", "VS-1017", "WASHER 5702-475-48 Z3", "WASHER 5702-95-30", "WD-415-1", "WD-605", "A-1001A-1L", "A-1001A-1R", "A-1001B-1", "A-1002-1", "A-1003-1", "A-1004-1R", "A-1004-1L", "A-1005-1", "A-1005A-1L", "A-1005A-1R", "A-1006-1A", "A-1006-1B", "A-1007-1A", "A-1007-1B", "A-1007-1C", "A-1008-1", "A-1011", "A-1015-1L", "A-1015-1R", "A-710", "AA6-063X3/4X3/4X12", "AS3-016", "AS3-020", "AS3-025", "AS3-032", "AS3-040", "AS3-063", "AS3-063X5/8X13 1/2", "AT0-032X1/4X19", "AT6-049X1.25X8", "AT6-058X5/16X4", "BEARING CM-4M", "BEARING COM-3-5", "CAV-110", "DOC W/TIP LENS 7/9", "ES AUDIO WARN", "ES E22-50K MICRO SW", "FL-1001A", "FL-1001B", "FL-1001C", "FL-1002", "FL-1003", "FL-1004", "FL-1005", "FL-1006", "FL-1007", "FL-1008", "FL-1009A", "J-CHANNELX6", "J-CHANNELX8", "ST304-065X1.375X34.62", "ST4130-035X1/2X48-PC", "ST4130-035X7/8X22", "T-00007-1", "T-1001", "T-1002", "T-1003", "T-1003B", "T-1003C", "T-1004", "T-1005", "T-1005BC", "T-1010", "T-1011", "T-1012", "VA-141", "VA-193", "VA-195A", "VA-195B", "VA-195C", "VA-195D", "VA-196", "VA-256", "VA-261", "VA-4908P", "W-00007CD", "W-1001", "W-1002", "W-1003", "W-1004", "W-1005", "W-1006", "W-1006E", "W-1006F", "W-1007A", "W-1007B", "W-1007C", "W-1007D", "W-1007E", "W-1008", "W-1009", "W-1010", "W-1011", "W-1012", "W-1013", "W-1013A", "W-1013C", "W-1013C-LX", "W-1013CX", "W-1013D", "W-1013E", "W-1013F", "W-1013G", "W-1014", "W-1015", "W-1016", "W-1017", " W-1018A", "W-1019", "W-1020", "W-1021", "W-1021B", "W-1024", "W-1025A", "W-1025B", "W-1026", "W-1027A", "W-1027B", "W-1029A", "W-1029B", "W-1029D", "W-1029E", "W-730", "W-822PP", "W-823PP-PC", "WD-1014-PC", "WD-1014", "WD-1014C", "WD-1030", "WD-1031", "WD-421", "W-SPAR ASSY", "W-1028A", "W-1028B", "J-STIFFENER", "W-823PP", "ES E22-50k", "ES DV18-188M", "WH-F1001", "C-1001", "C-1002", "C-1004", "C-1005", "ES-FA-PA-270-12-5", "F-01002", "F-01004A", "F-01004C", "F-01004K", "F-01004P", "F-01004T", "F-01042", "F-01042BCD-1", "F-01043B", "F-01043D", "F-01043G", "F-01049C", "F-01050", "F-01057", "F-01067A-1", "F-01067C-1", "F-01067D-1", "F-01069", "F-01072-1", "F-01088", "F-1001", "F-1001A", "F-1001B", "F-1001C", "F-1001D", "F-1001E", "F-1001F", "F-1001G", "F-1001J", "F-1001K", "F-1001M", "F-1003A", "F-1003B", "F-1003C", "F-1003D", "F-1003E", "F-1004-SPACR-063", "F-1004-SPACR-125", "F-1004A", "F-1004F", "F-1004H", "F-1004T", "F-1004B", "F-1004D", "F-1004J", "F-1004L", "F-1004R", "F-1004S", "F-1004N", "F-1004M", "F-1005A", "F-1005B", "F-1005C", "F-1005D", "F-1005E", "F-1013", "F-10100A", "F-10100B", "F-10102A", "F-10102B", "F-10101", "F-10104", "F-10105", "F-10107", "F-1015C", "F-1015D", "F-1015E", "F-1015F", "F-1015EF", "F-1016B", "F-1016C", "F-1016D", "F-1016D-1", "F-1016E", "F-1016F", "F-1016G", "F-1016H", "F-1017A", "F-1017B", "F-1017C", "F-1018", "F-1019", "F-1020", "F-1021", "F-1022", "F-1022A", "F-1023", "F-1023B", "F-1024", "F-1025", "F-1026", "F-1027", "F-1030", "F-1031", "F-1033", "F-1034A", "F-1034B", "F-1034C", "F-1034D", "F-1034E", "F-1034F", "F-1038", "F-1039A", "F-1039B", "F-1039D", "F-1039J", "F-1040", "F-1041", "F-1042E", "F-1042F", "F-1042G", "F-1043A", "F-1043C", "F-1043E", "F-1043F", "F-1044A", "F-1044B", "F-1044C", "F-1044D", "F-1044E", "F-1044F", "F-1045", "F-1046", "F-1046B", "F-1048", "F-1048C", "F-1048D", "F-1048F", "F-1048G", "F-1049A", "F-1049B", "F-1049D", "F-1050B", "F-1051A", "F-1051C", "F-1051E", "F-1051F", "F-1051G", "F-1051J", "F-1052", "F-1052A", "F-1052B", "F-1052C", "F-1053", "F-1058", "F-1059A", "F-1059B", "F-1059C", "F-1059D", "F-1059E", "F-1059F", "F-1060", "F-1061", "F-1062", "F-1063A", "F-1063B", "F-1063C", "F-1064", "F-1065", "F-1066A-1", "F-1066B-2", "F-1066C-2", "F-1067B", "F-1068A", "F-1068B", "F-1070", "F-1071", "F-1071B", "F-1076", "F-1077", "F-1080", "F-1081", "F-1083", "F-1084", "F-1086", "F-1087", "F-1092", "F-1093", "F-1094B", "F-1096", "F-1099A", "F-1099B", "F-1099C", "F-1099D", "F-1099E", "F-1099F", "F-1099G", "F-1099H", "F-6114", "F-6114A", "F-6115", "F-6122-1", "F-637A", "F-814HPP", "F-DRILL BUSHING", "FUEL VALVE", "HINGE PIANO 1/8X6'", "HINGE PIANO 1/8X9' ML", "PS UHMW-125X1/2X5", "PT 1/2ODX2 CLEAR", "RUBBER CHANNEL X 4'", "SS4130-050X1/2X4", "VA-00272", "VA-00273", "VA-00274", "VA-00275", "VA-00277", "VA-00278", "VA-107", "VA-175", "VA-178A", "VA-178B", "VA-178G", "VA-188", "VENT DL-03", "VENT DL-10", "VENT TG-10", "VENT TG-1010", "VENT-00004", "WD-01001-D1-1", "WD-01021", "WD-1002", "WD-1003", "WD-1004", "WD-1006", "WD-1007", "WD-1008", "WD-1010", "WD-1011", "WD-1012", "WD-1013A", "WD-1013B", "WD-1013C", "WD-1016-1", "WD-1017-1", "WD-1043", "AN SPACER", "AN816-6D", "AN818-6D", "AN818-4D", "AN819-4D", "AN819-6D", "AN822-4D", "AN822-6D", "AN826-6D", "AN833-4D", "AN833-6D", "AN837-4D", "AN837-6D", "AN960-716", "AN924-4D", "AN924-6D", "MS21919DG4", "FLO-SCAN", "ES 40108", "GMM-4M-675", "BUSH-BS", "U-00024", "U-00711", "U-00712", "U-01004", "U-01407", "U-1001", "U-1003", "U-1004A", "U-1005", "U-1008-1", "U-1010", "F-1084A", "F-1048", "F-1048C-1", "ATO-035X3/8", "F-1084A", "F-1084B", "F-1048", "F-1004K", "F-1069", "F-1048E", "F-1072", "VA-178C", "VA-178D", "F-1052A", "F-1052A", "F-1097", "F-1052", "WD-1006", "WD-1006", "F-1052", "F-1013", "F-1013", "PT-062X1/4", "F-1073", "F-1034", "F-1005", "F-1004", "WD-1011", "WD-1011", "F-1063", "WD-605/R-1", "ES-FA-PA-450-12-5", "F-1063B", "F-1063B", "F-1063B/R", "F-1033", "F-1033", "F-1043D/R", "F-1066B-2", "F-1016F", "F-1016", "F-1016F", "F-1016", "F-1066B-2", "F-10966B-2", "F-1066C-2", "F-1066C-2", "F-1070", "F-1045", "F-1001N-FWD", "F-1068B", "F-1003C", "F-1003C", "F-1001P-FWD", "F-1003", "F-1068", "F-1044", "F-1045/R", "F-1068B/R", "F-1045", "F-1068B", "F-1003C/R", "F-1002", "F-1001P", "F-1001P-AFT", "F-1001P-SHIM", "F-1001N-SHIM-INBD", "F-1001N-SHIM-OUTBD", "F-1001Q-SHIM", "F-1001P-AFT", "F-1001N", "F-1001N-AFT", "F-1001N-FWD", "F-1001Q", "F-1001Q-AFT", "F-1001Q-FWD", "F-1001Q-AFT", "F-1001Q-FWD", "F-1001P-FWD", "F-1001N-AFT", "F-10038", "F-637B", "F-637B", "F-637C", "F-637B", "F-10103B", "F-10103B", "F-1099G", "F-1099F", "F-1099H", "F-1099E", "T-1001", "F-1099E/F/G", "F-1069", "F-1099EFG", "pushrod/WD-1013B", "T-1005B", "F-01069-1", "W-1004", "T-1005", "W-1002", "T-1005/T-1005B", "F-1054", "C-1002B", "C-1002A", "C-1002A", "C-1002B", "F-1005C", "C-1002C", "C-1002", "C-1002", "WD-1018", "WD-1019", "WD-1018", "WD-1019", "WD-1018", "WD-1019", "WD-1019/R", "C-1003", "C-1003", "C-1003/R", "C-1002/R", "C-656", "WD-1022", "C-1006A", "C-1006B", "C-1006C", "C-1006D", "C-1014", "C-1008", "C-1007", "C-1009", "C-1017", "VA-197", "C-1011/R", "C-1012/R", "C-1012", "C-1011", "C-1014", "C-1010", "F-1042", "WD-1023", "C-1016", "C-1013", "C-1016B", "VA-198", "C-1004/R", "C-1004", "C-1004", "U-1010", "J-11968-14", "K2750-O-219", "U-1001", "U-1010", "U-1001", "WASHER-00017", "WD-01021-1", "U-1021", "SPRING-00003", "U-01420", "VA-143", "U-00022", "LM-67000L-A", "IO-540", "S-601-1", "S-602-1", "S-602B", "S-603", "S-1001", "S-1002", "F-1001Q", "F-1001Q", "F-1001N", "F-1001P", "F-1001N", "F-1001S", "SSP-090", "F-1001Y", "F-1001Z", "F-1001T", "SSP-120", "F-10012", "F-1001U", "F-1001V", "F-1069", "F-10109", "F-10108B", "F-10108A", "F-10109", "F-10108C", "F-10109", "U-1057B", "U-1057A", "U-1020", "U-1017A", "U-1020", "U-1019", "U-1013A", "U-1013B", "U-1018A", "U-1057-A", "U-1057B", "U-1057A", "U-1057A/B", "U-10044", "U-1017A", "U-1057", "U-1017B", "U-1017A", "U-1017", "F-1015C/R", "WD-1007/R", "U-1017", "F-1015C", "WD-1007", "U-1019", "F-1099B", "U-1019", "WD-1017", "U-1024", "U-1013C/R", "U-1013C", "U-1013C", "U-1013", "U-1018C", "F-01057", "F-1016E", "F-1051H"]

#Color list for highlights
cl = ['deeppink', 'pink3', 'magenta', 'darkorchid2', 'maroon',
      'slateblue', 'steelblue', 'deepskyblue', 'cyan', 'cyan3', 'aquamarine3',  'royalblue2',
      'green', 'limegreen', 'chartreuse1', 'yellowgreen', 
       'khaki4', 
      'gold2', 'darkgoldenrod3', 
      'orange', 'darkorange1', 'orangered','orangered3', 'salmon3',
      'red3', 'indianred3',
      'snow4']

#Command line arguments
argParser = argparse.ArgumentParser()
argParser.add_argument("-i", "--input", help="Input file path")
argParser.add_argument("-o", "--output", help="Output file path")
args = argParser.parse_args()
# input_file = args.input
input_file = "pdfs/50_10-ocr.pdf"
# output_file = args.output
output_file = "test.pdf"

#Setup for pdf scan
pdfDoc = fitz.open(input_file)

#Print page count of input PDF
num_pages = pdfDoc.page_count
print( str(num_pages) + " pages to process...")

def search_for_text(lines, search_str):
    """
    Search for the search string within the document lines
    """
    for line in lines:
        # Find all matches within one line


        search_regex = re.escape(search_str) + r'(?:\s+|\-|\,)' # Reduces duplicates. regex for space, - or endof line
        results = re.findall(search_regex, line, re.IGNORECASE)
        # In case multiple matches within one line
        for result in results:
            yield result

def lr_highlight(matched_values, border_color):
    for val in matched_values:
        shape = page.new_shape()
        matching_val_area = page.search_for(val, quads=True)
        for quad in matching_val_area:
            #Adjust border position/size due to OCR alignment inaccuracy
            ul = quad.ul
            ul_big = fitz.Point(ul[0] + 1, ul[1] - 1)
            ll = quad.ll
            ll_big = fitz.Point(ll[0] + 1, ll[1] + 1)
            lr = quad.lr
            lr_big = fitz.Point(lr[0] + 4, lr[1] + 1)
            ur = quad.ur
            ur_big = fitz.Point(ur[0] + 4, ur[1] - 1)
            big_quad = fitz.Quad(ul_big, ll_big, ur_big, lr_big)
            #Draw colored border around '-L' and '-R'
            page.draw_quad(big_quad, color= fitz.utils.getColor(border_color))
            shape.commit()


def highlight_left(left_parts):
    lr_highlight(left_parts, 'darkred')
    
def highlight_right(right_parts):
    lr_highlight(right_parts, 'chartreuse4')

def highlight_matching_data(page, matched_values, highlight_color):
    """
    Highlight matching values
    """
    matches_found = 0
    # Loop throughout matching values
    for val in matched_values:
        matches_found += 1
        matching_val_area = page.search_for(val, quads=True)
        # print("matching_val_area",matching_val_area)
        highlight = None
        highlight = page.add_highlight_annot(matching_val_area)
        highlight.set_colors(stroke= fitz.utils.getColor(highlight_color))
        highlight.update(opacity= 0.2)
        
    return matches_found



# Save the generated PDF to memory buffer
output_buffer = BytesIO()
total_matches = 0

# Iterate through pages
for pg in range(pdfDoc.page_count):
    
    # Select the page
    page = pdfDoc[pg]
    random.shuffle(cl)
        # Get Matching Data
        # Split page by lines
    page_lines = page.get_text("text").split('\n')
    for line in page_lines:
        left_result = re.findall("-L", line)
        highlight_left(left_result)
        right_result = re.findall("-R", line)
        highlight_right(right_result)
    color_count = 0
    for x in parts:
        matched_values = search_for_text(page_lines, x)
        if matched_values:
            h_color = cl[color_count] if color_count < len(cl) else 'yellow'
            matches_found = highlight_matching_data(
                page, matched_values, h_color)
            if matches_found > 0:
                color_count += 1
            total_matches += matches_found
        
print(f"{total_matches} Match(es) Found of Parts List In Input File: {input_file} -- Saved to: {output_file}")
# Save to output
pdfDoc.save(output_buffer)
pdfDoc.close()
# Save the output buffer to the output file
with open(output_file, mode='wb') as f:
    f.write(output_buffer.getbuffer())