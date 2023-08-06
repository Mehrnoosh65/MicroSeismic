# code by Mehrnoosh Behzadi
# Jan 2012
# Uni Hamburg
def shifttr(seismogram, L, NS):
    ii = seismogram.shape[1]
    data = np.zeros((NS, ii))  # Initialize the shifted data matrix

    for i in range(ii):
        seism = seismogram[:, i]
        n = int(L[i])
        sh = np.concatenate((np.zeros(n), seism))
        b = sh.shape[0]
        
        if b < NS + 1:
            c = NS - b
            e = np.zeros(c)
            shi = np.concatenate((sh, e))  # Final shifted seismogram
        else:
            shi = sh

        data[:, i] = shi  # M is NMO-corrected matrix

    return data
