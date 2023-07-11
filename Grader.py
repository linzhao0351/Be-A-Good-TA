#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 15:29:07 2021

@author: root
"""

import os
import pandas as pd
import csv, codecs
import shutil
import math

class Grader():
    
    def __init__(self):
        pass

    def readcsv(self, csvfile):
        data = []
        with codecs.open(csvfile, 'r', 
                         encoding='utf-8', 
                         errors='ignore') as fdata:
            csv_f = csv.reader(fdata)
            for row in csv_f:
                data.append(row)
        
        return data   


    def read_roster(self, filename):
        roster = self.readcsv(filename)

        stu_info = {}
        stu_names = []
        for line in roster[1:]:
            fname = line[0]
            lname = line[1]
            sid = line[2]
            section = line[-2]

            full_name = lname + ", " + fname

            stu_info[full_name] = {"sid": sid, "section": section}
            stu_names.append(full_name)
               
        return stu_info, stu_names
 

    def write_graded_case(self, stu_info, stu_names):
        stu_names.sort()

        grading_path = os.path.join(os.getcwd(), "Latex")
        if os.path.exists(grading_path) == False:
            os.mkdir(grading_path)

        bashfilename = os.path.join(grading_path, "pdflatex_bash.sh")
        bashfile = open(bashfilename, 'w')

        for sname in stu_names:
            fmt_name = sname.replace(", ", "_")
            fmt_name = fmt_name.replace(" ", "_")
            fmt_name = fmt_name.replace("(", "_") 
            fmt_name = fmt_name.replace(")", "_")
            fmt_name = fmt_name.replace("\'", "_") 
            
            sid = stu_info[sname]["sid"]
            section = stu_info[sname]["section"]

            texfilename = os.path.join(grading_path, "Student_%s_sec_%s.tex" % (fmt_name, section))
            texfile = open(texfilename, 'w')
            
            # write title of latex file
            texfile.write(r"\documentclass{article}" + "\n")
            texfile.write(r"\usepackage{geometry}" + "\n")
            texfile.write(r"\usepackage{multirow}" + "\n")
            texfile.write(r"\usepackage{caption}" + "\n")
            texfile.write(r"\usepackage{makecell}" + "\n")
            texfile.write(r"\usepackage{float}" + "\n")
            texfile.write(r"\usepackage{tabularx}" + "\n")
            texfile.write(r"\usepackage{cellspace}" + "\n")
            texfile.write(r"\usepackage{array}" + "\n")
            texfile.write(r"\usepackage[absolute,overlay]{textpos}" + "\n")
            texfile.write(r"\usepackage{pdfpages}" + "\n")
            texfile.write(r"\usepackage[utf8]{inputenc}" + "\n")
            texfile.write(r"\newcolumntype{L}[1]{>{\raggedright\let\newline\\\arraybackslash\hspace{0pt}}m{#1}}" + "\n")
            texfile.write(r"\newcolumntype{C}[1]{>{\centering\let\newline\\\arraybackslash\hspace{0pt}}m{#1}}" + "\n")
            texfile.write(r"\newcolumntype{R}[1]{>{\raggedleft\let\newline\\\arraybackslash\hspace{0pt}}m{#1}}" + "\n")
            texfile.write(r"\geometry{left=1in, right=1in, top=1in, bottom=1in}" + "\n\n")            
            texfile.write(r"\setlength{\parindent}{0pt}" +  "\n")
            texfile.write(r"\setlength{\parskip}{12pt}" +  "\n")
            # texfile.write(r"\linespread{1.2}" + "\n")
            

            coursetitle = "Finance 645W: Financial Management"
       
            texfile.write(r"\title{\textbf{Fuqua School of Business \\ " + 
                          r"%s \\ " % coursetitle +
                          r"Final Exam}}" + "\n")
           
            texfile.write(r"\date{}" + "\n")
            
            texfile.write(r"\begin{document}" + "\n")
            texfile.write("\n")            
            
            texfile.write(r"\maketitle" + "\n")
            texfile.write(r"\Large{\textbf{Name: %s}}" % (sname) + "\n\n")
            texfile.write(r"\vspace{12pt}" + "\n")
            texfile.write(r"\Large{\textbf{SID: %s}}" % (sid) + "\n\n")
            texfile.write(r"\newpage" + "\n\n")    

            for q in range(7):
                # write grades and comments
                texfile.write(r"\Large{\textbf{Question %s}}" % (q+1) + "\n\n")
                texfile.write(r"\Large{\textbf{Name: %s}}" % (sname) + "\n\n")
                texfile.write(r"\Large{\textbf{SID: %s}}" % (sid) + "\n\n")
                texfile.write(r"\newpage" + "\n\n")
   
            # end texfile
            texfile.write(r"\end{document}" + "\n")
            texfile.close()
            
            # write bash file
            bashfile.write("pdflatex --no-shell-escape %s" % os.path.basename(texfilename) + "\n")
            bashfile.write("yes | rm %s.pdf" % fmt_name + "\n")
            bashfile.write("yes | rm %s" % "Student_%s_sec_%s.tex" % (fmt_name, section) + "\n") 
            bashfile.write("yes | rm %s" % "Student_%s_sec_%s.aux" % (fmt_name, section) + "\n")
            bashfile.write("yes | rm %s" % "Student_%s_sec_%s.log" % (fmt_name, section) + "\n\n") 
        
        bashfile.close()
        
        # os.system("sh %s" % bashfilename.replace(" ", r"\ "))
        
        return 0
        


if __name__ == '__main__':
    app = Grader()

    stu_info, stu_names = app.read_roster(os.path.join(os.getcwd(), 'Gradescope_101_Spring_2021_roster.csv'))
    
    app.write_graded_case(stu_info, stu_names)




    