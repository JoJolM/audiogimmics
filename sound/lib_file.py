#!/usr/bin/python3
#
# Licence: GPL
# Created: 2019-06-28 15:54:12+02:00
# Main authors:
#     - Samy Carmouche <samy.carmouche@gmail.com>
#
# Description
# sample : ./lib_file.py "heartbeat succeessfu" 5 /var/log/syslog

import random
from datetime import datetime
import os
import time
import re
import sys
from lib_logs import Log


def parse_file(log, filename="test_file.txt", timeout=20, backline=0):

    start = int(datetime.now().strftime("%s"))
    file = open(filename, 'r')

    # Find the size of the file and move to the end
    st_size = os.stat(filename)[6] - backline
    # Go back some line
    file.seek(st_size)

    delta_time = 0

    while 1:
        now = int(datetime.now().strftime("%s"))
        delta = now - start
        left = timeout - delta
        # If timeout is reached
        if int(delta) > timeout:
            Log.fail("PATTERN NOT FOUND, TRY AGAIN")
            file.close()
            return False

        if int(delta) % 1 == 0 and delta_time != delta:
            Log.warn("[LOOKING FOR " + str(log) +
                     " time left : " + str(left) + "  sec ]")
            delta_time = delta

        where = file.tell()
        line = file.readline()

        # In case no line is reached
        if not line:
            time.sleep(0.1)
            file.seek(where)
        # Seek for the log in the line
        else:
            Log.debug(line.rsplit("\n"))
            searchObj = re.search(r'' + log + '', line, re.M | re.I)
            if searchObj:
                Log.ok("PATTERN FOUND IN :  " + line)
                file.close()
                return True


def random_write(input, output, inter):
    inp = open(input, 'r')
    out = open(output, 'w')

    seed = inp.readlines()
    nb_line = int(os.popen('wc -l '+input).read().split()[0])

    while 1:
        rline = random.randint(0, int(nb_line))
        print(str(rline) + " / " + str(nb_line))
        out.write(seed[rline-1])
        out.flush()
        time.sleep(float(inter))


if __name__ == "__main__":
    print("MAIN")
    if sys.argv[1] == "random":
        random_write(sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        parse_file(log=sys.argv[1], timeout=int(
            sys.argv[2]), filename=sys.argv[3])
