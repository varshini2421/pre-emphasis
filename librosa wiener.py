import numpy as np
import scipy as sp
from scipy.io.wavfile import read
from scipy.io.wavfile import write
from scipy import signal
from scipy.signal.signaltools import wiener
import matplotlib.pyplot as plt
import librosa
import soundfile as sf

(Frequency, array) = librosa.load('audio07.wav', sr=None)

# (Frequency, array) = read('10.wav')
len(Frequency)

plt.plot(Frequency)
plt.title('Original Signal Spectrum')
plt.xlabel('Frequency(Hz)')
plt.ylabel('Amplitude')
plt.show()


    # FourierTransformation = sp.fft(array)
    # # array = sp.fft(array)
    #
    # scale = sp.linspace(0, Frequency, len(array))
    #
    # plt.stem(scale[0:5000], np.abs(FourierTransformation[0:5000]), 'r')
    # # array = FourierTransformation
    # array = array.astype('float32')

filteredSignal = signal.wiener(Frequency)
plt.plot(filteredSignal) # plotting the signal.
plt.title('wiener filter plot')
plt.xlabel('Frequency(Hz)')
plt.ylabel('Amplitude')
plt.show()

    # c,d = signal.ellip(array,) # ButterWorth low-filter
# newfilteredSignal = signal.wiener(filteredSignal) # Applying the filter to the signal
# plt.plot(newfilteredSignal) # plotting the signal.
# plt.title('2')
# plt.xlabel('Frequency(Hz)')
# plt.ylabel('Amplitude')
# plt.show()
#     filename = "output-wiener" + myFiles[i]

sf.write('filename-wiener.wav',filteredSignal, array)

    # write("NewSound-wiener.wav", Frequency, newfilteredSignal)
