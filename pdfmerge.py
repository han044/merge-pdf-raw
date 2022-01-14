'''
Remove blank.pdf given in the input to remove the blank file
'''

import PyPDF2
import os
direc = "./input_pdf"
files = os.listdir(direc)


def mergePdfGiven(pdf_list):
    '''Arguments: List
     merges the list of pdf file names given in input file'''
    if not files:
        print("No files Given! try again with pdf Files")
        return

    merger = PyPDF2.PdfFileMerger()
    for i in pdf_list:
        merger.append(f'{direc}/{i}')

    merger.write("./merged/merged.pdf")


mergePdfGiven(files)
