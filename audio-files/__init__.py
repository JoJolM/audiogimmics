#! /usr/bin/python3

import argparse
import logging
import time
import sounddevice as sd
import soundfile as sf

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("filename", help="audio file to be played back")
parser.add_argument("-d", "--device", type=int, help="device ID")
parser.add_argument("-t", "--time", type=int, help="duration of the sound")
args = parser.parse_args()

t = args.time
ok = True
def timer(t):
	print("timer activated")
	while t > 0:
		time.sleep(1)
		t-=1
		print(t)
		return True
	print("timer deactivated")
	return False


try:
	
	#t-=1
	print("playing sound")		
	data, fs = sf.read(args.filename, dtype='float32')
	sd.play(data, fs, device=args.device, blocking=True)
	status = sd.get_status()
	if status:
		logging.warning(str(status))
except KeyboardInterrupt:
	parser.exit('\nInterrupted by user')
except Exception as e:
	parser.exit(type(e).__name__ + ': ' + str(e))
print("stop playing sound")
parser.exit()