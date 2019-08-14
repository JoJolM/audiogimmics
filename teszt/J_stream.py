import sys 
import threading
import argparse 
import soundfile as sf
import sounddevice as sd 
import datetime 

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("filename", help="audio file to be played back")
parser.add_argument("-d", "--device", type=int or list, help="device ID")
parser.add_argument("-t", "--time", type=int, help="duration of the sound")
parser.add_argument("-path","--fpath",help = "path to log file")
arg = parser.parse_args()
DATA_TYPE = 'float32'

class myThread(threading.Thread):
	def init(self, args):
		threading.Thread.init(self)
		self.args = args
	def run(self):
		playmp3(self.args)

def streamData(index):
	outstream = create_running_output_stream(index)

def  musicData(path):
 	music = load_sound_file(path)

def load_sound_file(path):

	audio_data,_  = sf.read(path, dtype = 'float32')
	return audio_data

def get_device_number_if_usb_soundcard(index_info):
	index, info = index_info 

	if "USB" in info["name"]:
		return index 
	return False 

def play_wav_on_index(audio_data, stream_object):
	stream_object.write(audio_data)

def create_running_output_stream(index):

	output = sd.OutputStream(
		device = index,
		dtype = DATA_TYPE)

	output.start()
	return output

sound_card_indices = list(filter(lambda x: x is not False, 
										map(get_device_number_if_usb_soundcard,[index_info for index_info in enumerate(sd.query_devices())])))
print('sound_card_indices = '+str(sound_card_indices))
song1 = musicData("/home/j.dittrick/A-test/audio-files/ocean-wave-1.wav")
song2 = musicData("/home/j.dittrick/A-test/audio-files/ocean-waves-2.wav")
stream1 = streamData(sound_card_indices[0])
stream2 = streamData(sound_card_indices[1])

def playmp3(args):
	if args == 1:
		stream1.outstream.write(song1.music)
	else:
		stream1.outstream.write(song2.music)

def play1():
	global thread1
	thread1 = myThread(1)
	stream1.outstream.start()
	thread1.start()

def play2():
	global thread2
	thread2 = myThread(2)
	stream2.outstream.start()
	thread2.start()

def stop1():
	stream1.outstream.stop()
	print(thread1.isAlive())

def stop2():
	stream2.outstream.stop()
	print(thread2.isAlive())

play1()
play2()