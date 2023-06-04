from spiceypy import spiceypy

import time  # for epoch time
import datetime

from log import log

J2000_EPOCH = 946684800  # SPICE uses the turn of the millennium as its epoch

UNIX_TIMESTAMP = time.time()

SPICE_TIMESTAMP = UNIX_TIMESTAMP - J2000_EPOCH

spiceypy.furnsh("de432s.bsp")  # load the SPK


def angle():
    target = "MOON"
    illuminator = "SUN"
    observer = "EARTH"
    aberration_corrections = "NONE"  # https://naif.jpl.nasa.gov/pub/naif/toolkit_docs/C/req/abcorr.html

    return spiceypy.phaseq(SPICE_TIMESTAMP,
                           target,
                           illuminator,
                           observer,
                           aberration_corrections)


def phase():
    date = datetime.datetime.fromtimestamp(UNIX_TIMESTAMP)
    p = ''

    t = angle()

    last: str
    with open('last.txt', 'r') as lastfile:
        last = lastfile.read()

    if t > 3.0:
        p = 'new'
    elif t < .15:
        p = 'full'
    else:
        if last == 'full' and t >= 1.5:
            p = 'last quarter'
        elif last == 'new' and t <= 1.5:
            p = 'first quarter'
    if p == last:
        p = ''

    if p != '':
        log('phase ' + p + ' from angle ' + str(t))
        if p == 'new':
            print('\n')
        with open('last.txt', 'w') as lastfile:
            lastfile.write(p)
    else:
        log('no phase, angle ' + str(t))

    return p