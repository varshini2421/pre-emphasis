import wave
import numpy
import matplotlib.pyplot as plt
from scipy import signal
import librosa
import soundfile as sf
from scipy.signal import filtfilt

# open the audio file and extract some information


# extract audio from wav file
input_signal , sampleRate = librosa.load("audio10.wav",sr = None)


# create the filter
N = 4
nyq = 0.5 * sampleRate
low = 100 / nyq
high = 7000 / nyq
b, a = signal.butter(N, [low, high], btype='band')

# apply filter
output_signal = signal.filtfilt(b, a, input_signal)

amp = 1.0
input_signal = amp * input_signal / max(abs(max(input_signal)),abs(min(input_signal)))

# ceate output file
sf.write('bandpasss.wav',output_signal,sampleRate)




#
