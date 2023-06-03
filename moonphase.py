from spiceypy import spiceypy
print('\t' + spiceypy.tkvrsn('TOOLKIT'))

import time # for epoch time

J2000_EPOCH = 946684800 # SPICE uses the turn of the millenium as its

spiceypy.furnsh("de432s.bsp") # load the SPK

def angle():
    ephemeris_time = time.time() - J2000_EPOCH # time since epoch
    target = "MOON"
    illuminator  = "SUN"
    observer = "EARTH"
    aberration_corrections = "NONE" # https://naif.jpl.nasa.gov/pub/naif/toolkit_docs/C/req/abcorr.html

    return spiceypy.phaseq(ephemeris_time,
                           target,
                           illuminator,
                           observer,
                           aberration_corrections)

def phase():
    # determine phase from angle ranges
    return str(angle())