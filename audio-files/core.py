#
#Import de modules
#
import os
import play_api
import argparse
import logging
import datetime
import sounddevice as sd
import soundfile as sf
import Process

# définition des arguments qui devront être parsé ie: le temps, les device,
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("filename", help="audio file to be played back")
parser.add_argument("-d", "--device", type=int, help="device ID")
parser.add_argument("-t", "--time", type=int, help="duration of the sound")
parser.add_argument("-b", "--blockingmode", type=int, help="duration of the sound")
parser.add_argument("-path","--fpath",help = "path to log file")
args = parser.parse_args()

t = args.time
blocking_mode = args.blockingmode
b_path = args.fpath

# commence par regarder si le path spécifié n'est pas vide
if b_path != None:
	if os.path.isdir(b_path):
		# si le path existe regarde si un fichier log existe 
		if os.path.isfile(b_path+'audio.log'):
			#si il existe il paramettre le path à utiliser pour lire le fichier
			path = b_path+'audio.log'
		else:
			# et sinon un nouveau fichier est créé et le path est paramétré 
			f=open('audio.log','+w')
			f.close()
			path = b_path+'audio.log'

	else :
		# si l'input n'est pas un path alors retourne une erreur et quitte le programme
		logging.error('Input is not dir')
		quit()
else: 
	# si l'input path est vide alors   
	if os.path.isfile('/home/j.dittrick/log/audio.log'):
		#si un log existe paramettre le path par défaut
		path = '/home/j.dittrick/log/audio.log'
	else:
		# et sinon créé le log et paramettre le path par défaut 
		f = open('audio.log','+w')
		f.close()
		path = '/home/j.dittrick/log/audio.log'
print(path)

logging.basicConfig(level=logging.DEBUG,filename= path,format= '%(asctime)s %(levelname)s : %(message)s')
def check(s):	
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
	

def test_1():
	logging.info('test_1 started')
	play_api.play_and_log_file()
	print("does smthn")
	check_1 = check("Finished")
	print(str(check_1))
	if check_1:
		print("test_1 exit success")
		logging.info('test_1 success exit')
		return logging.info('=======================================')
	else: 
		print("test_1 exit fail")
		logging.info('test_1 fail exit')
		return  logging.info('=======================================')

test_1()
parser.exit()