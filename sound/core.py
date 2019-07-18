#!/usr/bin/python3
#
# Licence: GPL
# Created: 2019-06-28 15:54:12+02:00
# Main authors:
#     - Samy Carmouche <samy.carmouche@gmail.com>
#
# Description
# sample : ./core.py -f /var/log/syslog -t 5 "heartbeat succeessfu" 

import lib_file
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    'text', help='text to search')
parser.add_argument(
    '-t', '--timeout', type=int, default=10,
    help='search timeout ( return false after timeout second')
parser.add_argument(
    '-f', '--file', type=str, 
    help='file to parse')

args = parser.parse_args()


lib_file.parse_file(log=args.text, timeout=args.timeout, filename=args.file)



