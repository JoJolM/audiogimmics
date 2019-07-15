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
#parser.add_argument("-b", "--blockingmode", type=int, help="duration of the sound")
args = parser.parse_args()
#d= args.device
#fn= args.filename
t = args.time
#blocking_mode = args.blockingmode
#print("blocking_mode= "str(blocking_mode))

def play_and_log_file():
	time_start = datetime.datetime.now()
	path = '/home/j.dittrick/Audio/audio-files/log.txt'
	f_sound = sf.SoundFile(args.filename)
	t_file_s = format(len(f_sound) / f_sound.samplerate)
	t_file_f = float(t_file_s)	
	t_file = int(t_file_f)

	f = open(path,'a')
	#f_r = open(path,'r')
	f.write('\n' + str(datetime.datetime.now())+' LOG: '+ 'Request to play '+ args.filename +'\r')
	try:			
		print("playing sound")		
		data, fs = sf.read(args.filename, dtype='float32')
		f.write('\n' + str(datetime.datetime.now())+' LOG: '+ 'data from '+args.filename+' loaded\r')
		print("goes here")
		blocking= (False if type(t) == int else True)
		print(blocking)
		#sd.play(data, fs, device= args.device, blocking= blocking)
		print("playing sound 2")
		f.write('\n' + str(datetime.datetime.now())+' LOG: '+ 'playing '+ args.filename)

		if blocking == False:
			if t > t_file:
				f.write('\n' + str(datetime.datetime.now())+' LOG: user requested a '+ str(t) +' second(s) timer requested \r')
				#si temps demandé > temps du fichier calcule le nombre de fois que le fichier doit être joué
				print("lqsfnq")
				number_of_plays = t // t_file
				f.write('\n' + str(datetime.datetime.now())+' LOG: '+ 'playing '+ str(number_of_plays)+'for '+args.filename)
				while number_of_plays > 0:
					sd.play(data, fs, device= args.device, blocking= True)
					sd.stop()
					number_of_plays -= 1
				#sortie de boucle cacule le temps restant
				t_2 = t%t_file
				print("t_2= "+str(t_2))
			else:
				t_2 = t
			sd.play(data, fs, device= args.device, blocking= blocking)	
			t_start_2 = datetime.datetime.now()	
			
			while (datetime.datetime.now() - t_start_2).total_seconds() < t_2:
				print("elapsed_time= "+str((datetime.datetime.now()- t_start_2).total_seconds()))
				i=0
		else:
			sd.play(data, fs, device= args.device, blocking= blocking)
			f.write('\n' + str(datetime.datetime.now())+' LOG: blocking == True\r')

		print("music stop")
		sd.stop()
		elapsed_time= (datetime.datetime.now() - time_start).total_seconds()

		print("elapsed_time= "+str(int(elapsed_time//60))+':'+str(int(elapsed_time%60))+'\r')
		if blocking:
			f.write('\n'+ str(datetime.datetime.now()) +' LOG: No timer requested, time elapsed = '+str(int(elapsed_time//60))+':'+str(int(elapsed_time%60))+'\r')
		else:
			f.write('\n'+"elapsed_time= "+str(int(elapsed_time//60))+':'+str(int(elapsed_time%60))+'\r')

		status = sd.get_status()
		if status:
			logging.warning(str(status))
	except KeyboardInterrupt:
		f.write('\n' + str(datetime.datetime.now())+' LOG: user quit \r')
		f.write('\n=======================================\r')
		parser.exit('\nInterrupted by user')
	except Exception as e:
		f.write('\n' + str(datetime.datetime.now())+' ERROR: something went wrong\r')
		parser.exit(type(e).__name__ + ': ' + str(e))
	print("stop playing sound")
	print("write file ?")
	
	f.write('\n' + str(datetime.datetime.now())+' LOG: Finished playing '+ args.filename+'\r')
	f.write('\n=======================================\r')
	f.close()
	return 

