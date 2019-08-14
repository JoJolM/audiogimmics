import csv 
from logger_j import check
import os 
import argparse
import datetime

path_for_report = os.getcwd() + '/resources/report/report.csv'
if not os.path.isfile(path_for_report):
	with open(path_for_report,'w') as f:
		f_writer = csv.writer(f)
		f_writer.writerow(['Date','Name','File played','Errors','Result'])

value_file = open('active.value','r')
v_f_read = value_file.read()
value  = v_f_read.split()
active = value[0]

def report(name,filename):
	date = datetime.datetime.now()
	if name == 'test_1':
		if active:
			Result = 'Success' if check('success',False) else 'Failed'
		else:
			Result = 'No log'

		if check('ERROR',False):
			error = 'interrupted by user'
		else :
			error = 'N/A'
	with open(path_for_report,'a') as f:
		f_writer = csv.writer(f)
		f_writer.writerow([str(date),name,filename,error,Result])


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
