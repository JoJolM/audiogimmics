#! /usr/bin/python3

import argparse
import logging
import datetime
import sounddevice as sd
import soundfile as sf

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("filename", help="audio file to be played back")
parser.add_argument("-d", "--device", type=int, help="device ID")
parser.add_argument("-t", "--time", type=int, help="duration of the sound")
parser.add_argument("-b", "--blocking mode", type=int, help="duration of the sound")
args = parser.parse_args()
d= args.device
fn= args.filename
t = args.time



def play_and_log_file(d,fn,t,blocking_mode):
	time_start = datetime.datetime.now()

	try:			
		print("playing sound")		
		data, fs = sf.read(fn, dtype='float32')
		sd.play(data, fs, d, blocking=False)
		blocking= ("blocking=True" if blocking_mode==1 else "blocking=False")
		print("playing sound 2")
		
		while (datetime.datetime.now()).second - time_start.second < t:
			print("elapsed_time= "+str((datetime.datetime.now()).second - time_start.second))
			i=0
		print("music stop")
		sd.stop()
		print("elapsed_time= "+str((datetime.datetime.now()).second - time_start.second))
			
		status = sd.get_status()
		if status:
			logging.warning(str(status))
	except KeyboardInterrupt:
		parser.exit('\nInterrupted by user')
	except Exception as e:
			parser.exit(type(e).__name__ + ': ' + str(e))
	print("stop playing sound")
	print("write file ?")
	path = '/home/j.dittrick/Audio/audio-files/log.txt'

	f = open(path,'w')
	f.write('Hey Qwant')
	f.close()
	parser.exit()
	return

play_and_log_file(d,fn,t,blocking_mode)