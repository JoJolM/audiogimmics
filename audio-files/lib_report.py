import csv 
from logger_j import check
import os 
import argparse
import datetime


import csv
with open('experiment.csv', 'a') as newFile:
    newFileWriter = csv.writer(newFile)
    newFileWriter.writerow([3, 'xxx'])
    newFileWriter.writerow([4,2, 'yyy'])
    newFileWriter.writerow([5, 'zzz'])


with open('experiment.csv','r') as userFile:
	userFileReader = csv.reader(userFile)
	for row in userFileReader:
		print (row)

path_for_report = os.getcwd() + 'report.csv'
if not os.path.isfile(path_for_report):
	with open(path_for_report,'w') as f:
		f_writer = csv.writer(f)
		f_writer.writerow(['Date','Name','File played','Errors','Result','Comments'])

def report(name,filename):
	if name == 'test_1':
		Result = 'success' if check('Finished') else 'Failed'
		if check('ERROR'):
			error = 'interrupted by user'
		else :
			error = 'N/A'
		filename = filename
		date = datetime.datetime.now()
		Comments='None'
	

	with open(path_for_report,'a') as f:
		f_writer = csv.writer(f)
		f_writer.writerow([str(date),name,filename,error,Result,Comments])


	print('gottem')
