

import matplotlib.pyplot as plt
# import librosa
import librosa.display
import numpy as np
audio_data = "dummy.wav"
y, sr = librosa.load(audio_data)
y_filt = librosa.effects.preemphasis(y)
print(y)
# and plot the results for comparison
S_orig = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)
S_preemph = librosa.amplitude_to_db(np.abs(librosa.stft(y_filt)), ref=np.max)
# print(type(S_orig))
librosa.display.specshow(S_orig, y_axis='log', x_axis='time')
plt.title('Original signal')
plt.show()
#
librosa.display.specshow(S_preemph, y_axis='log', x_axis='time')
plt.title('Pre-emphasized signal')
plt.show()
plt.savefig('books_read.png')