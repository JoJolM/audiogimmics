import logging
import datetime as dt
import os 
import argparse
import re 
import soundfile as sf 
import time

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("filename", help="audio file to be played back")
parser.add_argument("-d", "--device", type=int, help="device ID")
parser.add_argument("-t", "--time", type=int, help="duration of the sound")
parser.add_argument("-path","--fpath",help = "path to log file")
args = parser.parse_args()

filename = args.filename
value_file = open('active.value','r')
v_f_read = value_file.read()
value  = v_f_read.split()
path =  value[1]
t= args.time
f_sound = sf.SoundFile(args.filename)
t_file_s = format(len(f_sound) / f_sound.samplerate)
t_file_f = float(t_file_s)	
t_file = int(t_file_f)
backline = 0

def j_log(typ,s):
	if value[0] == 'True':
		active = True
	else :
		active = False
	print('active_2= '+str(active))
	if active :
		if typ == 'info':
			return logging.info(s)
		if typ == 'error':
			return logging.error(s)
		if typ == 'warning':
			return logging.warning(s)
	else:
		return	

def check(s):
	if value[0] == 'True':
		start = int(dt.datetime.now().strftime("%s")) # gets the current time in seconds 
		f= open(path, 'r')
		
		# get file size and moves to backline
		f_size = os.stat(filename)[6] - backline
		# set current position to said backline
		f.seek(f_size)

		delta_time = 0
		timeout = (t if type(t)==int else t_file)
		while 1:
			print("bonjour")
			now = int(dt.datetime.now().strftime("%s"))
			delta = now - start
			left = timeout - delta
			# if timeout
			if int(delta) > timeout:
				print('PATTER NOT FOUND, TRY AGAIN')
				f.close()
				return False

			if int(delta)%1 == 0 and delta_time != delta:
				print("[LOOKING FOR "+ s +" time left : "+ str(left) + " sec ]")
				delta_time = delta

			where = f.tell()
			line = f.readline()

			# In case no line is reached 
			if not line:
				print("line not found")
				time.sleep(0.1)
				f.seek(where)

		# Seek for the log in the line
		else:
			print("looking for ")
			logging.debug(line.rsplit("\n"))
			searchObj = re.search(r'' + log + '', line, re.M | re.I)
			if searchObj:
				print("PATTERN FOUND IN : " + line)
				f.close()
				return True
