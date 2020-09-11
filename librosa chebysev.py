from scipy import signal
import matplotlib.pyplot as plt
import librosa
import soundfile as sf

(Frequency, array) = librosa.load('audio10.wav', sr=None)

len(Frequency)

plt.plot(Frequency)
plt.title('Original Signal Spectrum')
plt.xlabel('Frequency(Hz)')
plt.ylabel('Amplitude')
# plt.show()

b, a = signal.cheby1(5, 3, 1000 / (0.5 * array), btype='highpass')

filteredSignal = signal.lfilter(b, a, Frequency)
plt.plot(filteredSignal)  # plotting the signal.
plt.title('Highpass Filter')
plt.xlabel('Frequency(Hz)')
plt.ylabel('Amplitude')
# plt.show()

c, d = signal.cheby1(5, 3, 380 / (0.5 * array), btype='lowpass')  # ButterWorth low-filter
newFilteredSignal = signal.lfilter(c, d, filteredSignal)  # Applying the filter to the signal
plt.plot(newFilteredSignal)  # plotting the signal.
plt.title('Lowpass Filter')
plt.xlabel('Frequency(Hz)')
plt.ylabel('Amplitude')
# plt.show()
# filename = "output-chebysev" + myFiles[i]

sf.write( 'filename.wav', newFilteredSignal, array)
