#
#Import de modules
#
import os
import play_api
import argparse
import logging
import datetime
import lib_report
from logger_j import j_log, check, inspector__
import sounddevice as sd
import soundfile as sf

# définition des arguments qui devront être parsé ie: le temps, les device,
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("filename", help="audio file to be played back")
parser.add_argument("-d", "--device", type=int or list, help="device ID")
parser.add_argument("-t", "--time", type=int, help="duration of the sound")
parser.add_argument('-b', '--blocksize', type=int, default=2048,
                    help='block size (default: %(default)s)')
parser.add_argument(
    '-q', '--buffersize', type=int, default=20,
    help='number of blocks used for buffering (default: %(default)s)')
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
	name = str(inspector__())
	j_log('info','test_1 started')
	play_api._play_(args.device,name)
	print("does smthn")
	check_1 = check("Finished",True)
	lib_report.report(name,args.filename)
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

def test_2():
	name = str(inspector__())
	j_log('info',f'{name} started')

	play_api.__play_mult__()
	play_api._play_(8)
	#play_api._play_(8,name)
	check_1 = check(f'device {args.device}',False)
	print('check_1 = '+ str(check_1))
	check_2 = check('device 8',False)
	print('check_2 = '+ str(check_2))
	if check_1 and check_2 :
		j_log('info','sound successfully played to both devices')
		j_log('info','test_2 success')
		return lib_report.report(name,args.filename)
	elif check_2 or check_1:
		j_log('error','sound only played on one device')
		j_log('error','test_2 failed')
		j_log('info','=======================================')
		return lib_report.report(name,args.filename)
	else:
		j_log('error','sound not played at all,change method')
		j_log('error','test_2 failed')
		j_log('info','=======================================')
		return lib_report.report(name,args.filename)

test_2()

parser.exit()