import sys 
import threading
import argparse 
import queue
import soundfile as sf
import sounddevice as sd 
import datetime 

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


if args.blocksize == 0:
    parser.error('blocksize must not be zero')
if args.buffersize < 1:
    parser.error('buffersize must be at least 1')

q = queue.Queue(maxsize=args.buffersize)
event = threading.Event()
t= args.time
t_start = datetime.datetime.now()
def callback(outdata, frames, time, status):
    assert frames == args.blocksize
    print('activated callback')
    if status.output_underflow:
        print('Output underflow: increase blocksize?', file=sys.stderr)
        raise sd.CallbackAbort
    assert not status
    try:
        data = q.get_nowait()
    except queue.Empty:
        print('Buffer is empty: increase buffersize?', file=sys.stderr)
        raise sd.CallbackAbort
    if len(data) < len(outdata):
        outdata[:len(data)] = data
        outdata[len(data):] = b'\x00' * (len(outdata) - len(data))
        raise sd.CallbackStop
    else:
        outdata[:] = data


def _stream_():
	try:
		with sf.SoundFile(args.filename) as f:
			for _ in range(args.buffersize):
				print('5674')
				data = f.buffer_read(args.blocksize,dtype = 'float32')
				print('5674')
				if not data :
					print('eds')

					break 
				q.put_nowait(data)
				print('here')
			stream = sd.RawOutputStream( samplerate = f.samplerate, blocksize = args.blocksize,
				device = args.device, channels=f.channels, dtype= 'float32', callback = callback,
				finished_callback = event.set)
			print('abc')
			with stream:
		            timeout = args.blocksize * args.buffersize / f.samplerate
		            while data:
		            	print("elapsed_time= "+str((datetime.datetime.now()- t_start).total_seconds()))
		            	if t != None:
		            		print('t != None')
		            		if (datetime.datetime.now()-t_start).total_seconds() >= t:
		            			sd.RawOutputStream.stop()
		            		else:
		            			data = f.buffer_read(args.blocksize, dtype='float32')
		            			q.put(data, timeout=timeout)
		            			print('data exists')
		            	else:
		            		print('raté')
		            		data = f.buffer_read(args.blocksize, dtype='float32')
		            		q.put(data, timeout=timeout)
		            		print('data exists')
		            		#event.wait()  # Wait until playback is finished
			
	except KeyboardInterrupt:
	    parser.exit('\nInterrupted by user')
	except queue.Full:
	    # A timeout occured, i.e. there was an error in the callback
	    parser.exit(1)
	    print ('exit _stream_')
	except Exception as e:
	    parser.exit(type(e).__name__ + ': ' + str(e))
	


_stream_()
print('nosz')
