#
#Import de modules
#
import play_api
import argparse
import logging
import datetime
import sounddevice as sd
import soundfile as sf


parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("filename", help="audio file to be played back")
parser.add_argument("-d", "--device", type=int, help="device ID")
parser.add_argument("-t", "--time", type=int, help="duration of the sound")
parser.add_argument("-b", "--blockingmode", type=int, help="duration of the sound")
args = parser.parse_args()

t = args.time
blocking_mode = args.blockingmode
path = '/home/j.dittrick/Audio/audio-files/log.txt'
 
def check(s):
	f= open(path, 'r')
	f_read= f.read()
	f2_r= f_read.split()
	i = len(f2_r) -1 
	while True:
		print(f2_r[i])

		if f2_r[i] == s:
			f.close()
			return True
		elif f2_r[i] == "=======================================" and i != len(f2_r) -1:
			f.close()
			return False
		i-=1
	

def test_1():
	f= open(path, 'a')
	f.write('\n'+str(datetime.datetime.now())+' : > test_1 start <\r')
	play_api.play_and_log_file()
	print("does smthn")
	check_1 = check("Finished")
	print(str(check_1))
	if check_1:
		print("test_1 exit success")
		f.write('\n'+str(datetime.datetime.now())+' : > test_1 success <\r')
		return f.write('\n=======================================\r')
	else: 
		print("test_1 exit fail")
		f.write('\n> test_1 fail <\r')
		return  f.write('\n=======================================\r')

test_1()
parser.exit()