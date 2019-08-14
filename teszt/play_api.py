#! /usr/bin/python3

import argparse
import datetime
from logger_j import j_log 
import sounddevice as sd
import soundfile as sf


parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("filename", help="audio file to be played back")
parser.add_argument("-d", "--device", type=int, help="device ID")
parser.add_argument("-t", "--time", type=int, help="duration of the sound")
parser.add_argument("-path","--fpath",help = "path to log file")
#parser.add_argument("-b", "--blockingmode", type=int, help="duration of the sound")
args = parser.parse_args()
#d= args.device
#fn= args.filename
t = args.time
#blocking_mode = args.blockingmode
#print("blocking_mode= "str(blocking_mode))
value_file = open('active.value','r')
v_f_read = value_file.read()
value  = v_f_read.split()
filename = value[2]


def _play_(d):

	time_start = datetime.datetime.now()
	f_sound = sf.SoundFile(filename)
	t_file_s = format(len(f_sound) / f_sound.samplerate)
	t_file_f = float(t_file_s)	
	t_file = int(t_file_f)
	j_log('info',f'Request to play {args.filename}')
	try:					
		data, fs = sf.read(filename, dtype='float32')
		j_log('info',f'data from {args.filename} loaded')
		blocking= (False if type(t) == int else True)
		#sd.play(data, fs, device= args.device, blocking= blocking)
		j_log('info',f'playing {args.filename} to device {d}')
		if blocking == False:
			if t > t_file:
				j_log(info,f'user requested {t} second timer')
				#si temps demandé > temps du fichier calcule le nombre de fois que le fichier doit être joué
				number_of_plays = t // t_file
				j_log('info',f'playing {args.filename} {number_of_plays} times')
				while number_of_plays > 0:
					sd.play(data, fs, device= d, blocking= True)
					sd.stop()
					number_of_plays -= 1
				#sortie de boucle cacule le temps restant
				t_2 = t%t_file
			
			else:
				#sinon set un timer normal 
				t_2 = t
				if type(d) == list:
					for i in d:
						sd.play(data, fs, device= i, blocking= blocking)
				else:
					sd.play(data, fs, device= d, blocking= blocking)	
			t_start_2 = datetime.datetime.now()	
			
			while (datetime.datetime.now() - t_start_2).total_seconds() < t_2:
				i=0
		else:
			sd.play(data, fs, device= d, blocking= blocking)
			j_log('info','blocking == True')
		sd.stop()
		elapsed_time= (datetime.datetime.now() - time_start).total_seconds()

		print("elapsed_time= "+str(int(elapsed_time//60))+':'+str(int(elapsed_time%60))+'\r')
		if blocking:
			j_log('info','no timer requested, time elapsed = ' + str(int(elapsed_time//60))+':'+str(int(elapsed_time%60)))
		else:
			j_log('info','elapsed time= '+ str(int(elapsed_time//60))+':'+str(int(elapsed_time%60)))
		status = sd.get_status()
		if status:
			j_log('info',warning(str(status)))
	except KeyboardInterrupt:
		j_log('error','user quit')
		j_log('info','=======================================')
		return 
		#parser.exit('\nInterrupted by user')
	except Exception as e:
		parser.exit(type(e).__name__ + ': ' + str(e))
		return
	j_log('info',f'Finished playing {args.filename}')
	j_log('info','=======================================')
	return 
