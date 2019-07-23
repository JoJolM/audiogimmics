#
#Import de modules
#
import os
import play_api
import argparse
import logging
import datetime
import lib_report
from logger_j import j_log, check
import sounddevice as sd
import soundfile as sf

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
			path = b_path+'audio.log'
		else:
			f=open('audio.log','+w')
			f.close()
			path = b_path+'audio.log'
			# et sinon un nouveau fichier est créé et le path est paramétré 
		active = True

	elif os.path.isfile(b_path):
		#si il existe il paramettre le path à utiliser pour lire le fichier
		active = True
		path = b_path
	else:
		logging.error('Input invalid')
		quit()
		
	logging.basicConfig(level=logging.DEBUG,filename= path,
						format= '%(asctime)s %(levelname)s : %(message)s')
	print(path)
else: 
	active = False

#stockage de si l'utilisateur a niput un dir	
cwd = os.getcwd()
if os.path.isfile(cwd+'active.value'):	
	f= open('active.value','w+')
	f.write(str(active)+'\r')
	f.write('\n'+str(path))
else:
	f= open('active.value','w')
	f.write(str(active)+'\r')
	f.write('\n'+str(path))
print('active_1= '+str(active))
f.close()
#logging.basicConfig(level=logging.DEBUG,filename= path,format= '%(asctime)s %(levelname)s : %(message)s')


def test_1():
	j_log('info','test_1 started')
	play_api._play_()
	print("does smthn")
	check_1 = check("Finished")
	lib_report.report('test_1',args.filename)
	print("check_1: "+str(check_1))
	if check_1:
		print("test_1 exit success")
		j_log('info','test_1 success exit')
		print('active : '+ str(active))
		return j_log('info','=======================================')
	else: 
		print("test_1 exit fail")
		j_log('info','test_1 fail exit')
		print('active : '+ str(active))
		return  j_log('info','=======================================')

def test_log():
	j_log('info',f'info {t} success')
	j_log('error','error success')
	j_log('warning','warning success')
	j_log('info','info')



test_1()

parser.exit()