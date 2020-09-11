import numpy as np
import scipy as sp
from scipy.io.wavfile import read
from scipy.io.wavfile import write
from scipy import signal
import matplotlib.pyplot as plt
import librosa
import soundfile as sf

(Frequency, array) = librosa.load('audio10.wav', sr= None)

len(Frequency)

plt.plot(Frequency)
plt.title('Original Signal Spectrum')
plt.xlabel('Frequency(Hz)')
plt.ylabel('Amplitude')
# plt.show()


    # FourierTransformation = sp.fft(array)
    #
    # scale = sp.linspace(0, Frequency, len(array))
    #
    # plt.stem(scale[0:5000], np.abs(FourierTransformation[0:5000]), 'r')
    # plt.title('Signal spectrum after FFT')
    # plt.xlabel('Frequency(Hz)')
    # plt.ylabel('Amplitude')
    # # plt.show()



b,a = signal.ellip(6, 3, 50, 1000/(0.5*array), btype='highpass')

filteredSignal = signal.lfilter(b,a,Frequency)
plt.plot(filteredSignal) # plotting the signal.
plt.title('Highpass Filter')
plt.xlabel('Frequency(Hz)')
plt.ylabel('Amplitude')
# plt.show()

c,d = signal.ellip(5,3, 100, 380/(0.5*array), btype='lowpass') # ButterWorth low-filter
newFilteredSignal = signal.lfilter(c,d,filteredSignal) # Applying the filter to the signal
plt.plot(newFilteredSignal) # plotting the signal.
plt.title('Lowpass Filter')
plt.xlabel('Frequency(Hz)')
plt.ylabel('Amplitude')
# plt.show()

    # filename = "output-ellip" + myFiles[i]

sf.write("ellipout.wav",newFilteredSignal, array)