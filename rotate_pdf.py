#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 20:32:12 2021

@author: root
"""

import os
import PyPDF2


def rotatePDF(pdfFile):
    pdfFileObj = open(pdfFile, 'rb')     
    reader = PyPDF2.PdfFileReader(pdfFileObj, strict=False)   
    numPages = reader.numPages
    
    writer = PyPDF2.PdfFileWriter()
    for k in range(0, numPages):
        page = reader.getPage(k)
        writer.addPage(page.rotateClockwise(180))
    
    path, basename = os.path.split(pdfFile)
    outputfilename = os.path.join(path, "rotate_" + basename)
    with open(outputfilename, 'wb') as out:
        writer.write(out)
    
    return outputfilename 
    

if __name__ == '__main__':
    folder = '/Users/linzhao/Desktop/Scanned Exams'
    files = os.listdir(folder)
    for f in files:
        if ".pdf" in f:
            rotatePDF(os.path.join(folder, f))