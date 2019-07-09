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
args = parser.parse_args()

def test_1(d=args.device, t=args.time, filename=args.filename):
