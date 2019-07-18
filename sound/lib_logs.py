#!/usr/bin/python3
#
# Licence: GPL
# Created: 2019-06-28 15:54:12+02:00
# Main authors:
#     - Samy Carmouche <samy.carmouche@gmail.com>
#
# Description


class Log:
    DEBUG = '\033[95m'
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    def warn(mess):
        print(Log.WARNING + str(mess) + Log.ENDC)

    def ok(mess):
        print(Log.OKGREEN + str(mess) + Log.ENDC)

    def fail(mess):
        print(Log.FAIL + str(mess) + Log.ENDC)

    def error(mess):
        print(Log.FAIL + str(mess) + Log.ENDC)

    def debug(mess):
        print(Log.DEBUG + str(mess) + Log.ENDC)
