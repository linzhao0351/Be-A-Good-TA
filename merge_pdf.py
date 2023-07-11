#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 23:28:17 2020

@author: linzhao
"""

import PyPDF2
import os

def readPDF(pdfFile):
    pdfFileObj = open(pdfFile, 'rb')     
    reader = PyPDF2.PdfFileReader(pdfFileObj, strict=False)   
    return reader
    
    
def merge_PDFs(pdf_filename_list, outputfilename):
    writer = PyPDF2.PdfFileWriter()
    for f in pdf_filename_list:
        reader = readPDF(f)
        numPages = reader.numPages
        for k in range(0, numPages):
            page = reader.getPage(k)
            writer.addPage(page)
    
    with open(outputfilename, 'wb') as out:
        writer.write(out)    
    
    return outputfilename

    
if __name__ == '__main__':
    files = os.listdir(os.path.join(os.getcwd(), 'Latex'))
    
    files = [os.path.join(os.getcwd(), 'Latex', f) for f in files if ".pdf" in f]
    files.sort()

    for i in range(0,1):
        subfiles = files[30*i: 30*(i+1)]
        merge_PDFs(subfiles, os.path.join(os.getcwd(), 'submissions_%s.pdf' % i))
    






