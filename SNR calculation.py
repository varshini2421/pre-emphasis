

import scipy.io.wavfile as wavfile
import numpy
import os.path
from scipy import stats

import numpy as np
def signaltonoise(a, axis=0, ddof=0):
    a = np.asanyarray(a)
    m = a.mean(axis)
    sd = a.std(axis=axis, ddof=ddof)
    return np.where(sd == 0, 0, m/sd)

def snr(file):
    if (os.path.isfile(file)):
        data = wavfile.read(file)[1]
        singleChannel = data
        try:
            singleChannel = numpy.sum(data, axis=1)
        except:
            # was mono after all
            pass

        norm = singleChannel / (max(numpy.amax(singleChannel), -1 * numpy.amin(singleChannel)))
        # k =signaltonoise(norm)
    return signaltonoise(norm)
file="dummy.wav"
ratio = snr(file)
print(ratio)