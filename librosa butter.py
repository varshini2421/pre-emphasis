
import librosa.display
from matplotlib.pyplot import ylabel, plot, show, xlabel, title, stem
import numpy as np
import scipy as sp
import soundfile as sf
from scipy import signal
from scipy.io.wavfile import read
from scipy.io.wavfile import write

audio = 'audio02.wav'
(frequency, sr) = librosa.core.load(audio, sr=None)

a=len(frequency)
# print(a)
plot(frequency)
# show()

cut_off = 1000
nyq = 0.5 * sr
wn = cut_off / nyq
# Wn= 1000/(sr/2)
b, a = signal.butter(4, wn, btype='highpass', analog=False)
filteredSignal = signal.lfilter(b, a, frequency)
plot(filteredSignal)  # plotting the signal.
title('Highpass Filter')
xlabel('Frequency(Hz)')
ylabel('Amplitude')
# show()

c,d = signal.butter(5, 380/(0.5*sr), btype='lowpass') # ButterWorth low-filter
newFilteredSignal = signal.lfilter(c,d,filteredSignal) # Applying the filter to the signal
plot(newFilteredSignal) # plotting the signal.
title('Lowpass Filter')
xlabel('Frequency(Hz)')
ylabel('Amplitude')
# show()

sf.write('butter.wav',newFilteredSignal,sr)
