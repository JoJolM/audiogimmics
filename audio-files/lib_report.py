import csv 
from logger_j import check
import os 
import argparse
import datetime


import csv

path_for_report = os.getcwd() + 'report.csv'
if not os.path.isfile(path_for_report):
	with open(path_for_report,'w') as f:
		f_writer = csv.writer(f)
		f_writer.writerow(['Date','Name','File played','Errors','Result'])

def report(name,filename):
	date = datetime.datetime.now()
	if name == 'test_1':
		print('here first')
		Result = 'Success' if check('Finished',False) else 'Failed'
		print('passes here')

		if check('ERROR',False):
			error = 'interrupted by user'
		else :
			error = 'N/A'
	

	print('gottem')


#if name == 'test_2':
#		Result = 'Success' if (check_1 and check_2) else 'Faled'
#
#		if check('ERROR'):
#			error = 'one or more error(s) occured'
#		else:
#			error = 'N/A'

#	with open(path_for_report,'a') as f:
#		f_writer = csv.writer(f)
#		f_writer.writerow([str(date),name,filename,error,Result])
