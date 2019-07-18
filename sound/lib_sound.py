#!/usr/bin/python3
#
# Licence: GPL
# Created: 2019-06-28 15:54:12+02:00
# Main authors:
#     - Samy Carmouche <samy.carmouche@gmail.com>
#
# Description
# sample : ./lib_sound.py -f ../piano2.wav -d 9 -t 10

import sounddevice as sd
import soundfile as sf
import argparse
import time
from lib_logs import Log


def int_or_str(text):
    """Helper function for argument parsing."""
    try:
        return int(text)
    except ValueError:
        return text


def get_duration(filename):
    f = sf.SoundFile(filename)
    Log.debug('duration = {}'.format(len(f) / f.samplerate))
    return abs(len(f) / f.samplerate)


def play_s(filename, device, timer):
    Log.debug("start play " + str(timer))
    sd.default.device = device
    data, fs = sf.read(filename, dtype='float32')
    duration = int(get_duration(filename))

    # Calcule number of time to repeat
    if timer < duration:
        Log.debug("timer < duration => play during timer")
        last_repeat = timer
    else:
        last_repeat = timer % duration
        repeat = int(timer / duration)
        Log.debug("repeat  " + str(repeat) +
                  " last_repeat " + str(last_repeat) + "sec")
        for i in range(0, int(repeat)):
            sd.play(data, fs, blocking=True)

    # Play last occurence and stop after X sec
    sd.play(data, fs, blocking=False)
    while last_repeat > 0:
        last_repeat -= 1
        Log.debug("wait 1 sec , left :  " + str(last_repeat))
        time.sleep(1)
    sd.stop()


parser = argparse.ArgumentParser()
parser.add_argument(
    '-d', '--device', type=int_or_str,
    help='input device (numeric ID or substring)')
parser.add_argument(
    '-f', '--file', type=int_or_str,
    help='input device (numeric ID or substring)')
parser.add_argument(
    '-t', '--timeout', type=int,
    help='timeout of sound play')

args = parser.parse_args()

try:
    play_s(args.file, args.device, args.timeout)
except Exception as ex:
    Log.error("error " + str(ex))
