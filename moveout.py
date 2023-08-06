# code by Mehrnoosh Behzadi
# Jan 2012
# Uni Hamburg
import numpy as np

def moveout(time):
    # Find the amount of move out per shot
    T = time.T
    jj = T.shape[1]
    n = time.shape[1]
    for ii in range(jj):
        Ti = T[:, ii]   # Ti is the traveltime table of the ith shot
        tm = np.max(Ti)  # Find the minimum traveltime
        Tm = tm * np.ones(n)
        o = Tm - Ti      # Compute MO of per receiver for per shot
        T[:, ii] = o    # Replace the NMO instead of traveltime

    Tnmo = T.T
    Tnmo = Tnmo / 0.025  # Sampling interval in homogeneous data is 5 (ms)
    SMO = np.round(Tnmo)  # Number of samples to be shifted in per seismogram of per receiver
    return SMO

