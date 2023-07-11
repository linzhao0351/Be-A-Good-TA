

import os
import shutil
import csv
import re

def mkdir(path):
	if os.path.exists(path):
		pass
	else:
		os.mkdir(path)

	return path

def writecsv(data, filename):
    output = open(filename,'w', newline='')
    csv_writer = csv.writer(output)
    for item in data:
        csv_writer.writerow(item)
    output.close()
        
    return filename


submissions_folder = os.path.join(os.getcwd(), 'submissions_35304')

files = os.listdir(submissions_folder)

check_list = []
for f in files:
	if os.path.isdir(os.path.join(submissions_folder, f)):
		continue

	fname_list = f.split('_')
	
	sname = fname_list[0]

	spath = os.path.join(submissions_folder, sname)
	mkdir(spath)

	shutil.move(os.path.join(submissions_folder, f), os.path.join(spath, f))

sname_list = []
files = os.listdir(submissions_folder)
for f in files:
	if os.path.isdir(os.path.join(submissions_folder, f)):

		pass
	else:
		continue

	sname_list.append(f)

sname_list.sort()
sname_list = [[elem] for elem in sname_list]
writecsv(sname_list, os.path.join(os.getcwd(), 'submissions.csv'))








