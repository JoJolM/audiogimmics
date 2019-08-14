import logging
import datetime as dt
import os 
import argparse
import re 
import soundfile as sf 
import time
import inspect

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
filename = value[2]
t= args.time
f_sound = sf.SoundFile(filename)
t_file_s = format(len(f_sound) / f_sound.samplerate)
t_file_f = float(t_file_s)	
t_file = int(t_file_f)
backline = 0

def inspector__():
	curframe = inspect.currentframe()
	calframe = inspect.getouterframes(curframe, 2)
	return calframe[1][3]

def j_log(typ,s):
	if value[0] == 'True':
		active = True
	else :
		active = False
	if active :
		if typ == 'info':
			return logging.info(s)
		if typ == 'error':
			return logging.error(s)
		if typ == 'warning':
			return logging.warning(s)
	else:
		return	

def check(s,need_timer):
	if value[0] == 'True':
		if need_timer:
			print("path = " + path)
			start = int(dt.datetime.now().strftime("%s")) # gets the current time in seconds 
			
			f = open(path, 'r')
			
			
			# get file size and moves to backline
			f_size = os.stat(path)[6] - 500
			print (str(os.stat(path)))
			print("f_size = "+str(f_size))

			# set current position to said backline
			f.seek(f_size)
			delta_time = 0
			timeout = 20
			while 1:
			
				now = int(dt.datetime.now().strftime("%s"))
				delta = now - start
				left = timeout - delta
				# if timeout
				if int(delta) > timeout:
					print('PATTERN NOT FOUND, TRY AGAIN')
					f.close()
					return False

				if int(delta)%1 == 0 and delta_time != delta:
					print("[LOOKING FOR "+ s +" time left : "+ str(left) + " sec ]")
					delta_time = delta

				where = f.tell()
				#print("where : "+str(where))
				line = f.readline()
				print("line : "+str(line))
				

				# In case no line is reached 
				if not line:
					print("line not found")
					time.sleep(0.1)
					f.seek(where)

				# Seek for the log in the line
				else:
					print("looking for " + str(line))
					print(line.rsplit("\n"))
					searchObj = re.search(r'' + s + '', line, re.M | re.I)
					if searchObj:
						print("PATTERN FOUND IN : " + line)
						f.close()
						return True

		else:
			f= open(path, 'r')
			f_read= f.read()
			f2_r= f_read.split()
			i = len(f2_r) -1 
			while True:

				if f2_r[i] == s:
					f.close()
					return True
				elif f2_r[i] == "=======================================" and i != len(f2_r) -1:
					f.close()
					return False
				i-=1
	else:
		return 
	print ("END FUNCT")


if __name__ == "__main__":
    print("MAIN")
    print(str(sys.argv))
    if sys.argv[1] == "random":
        random_write(sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        parse_file(log=sys.argv[1], timeout=int(
            sys.argv[2]), filename=sys.argv[3])
        
