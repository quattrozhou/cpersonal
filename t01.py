import csv, pdb

import matplotlib.pylab as plt

import numpy as np

from scipy.signal import butter, lfilter, freqz

import scipy.fftpack

file_path = "/home/czhou/data/stock/AMD.csv"

# spamReader = csv.reader(open(file_path, newline=''), delimiter=' ', quotechar='|')

# for row in spamReader:
#     # print(', '.join(row))
#     print(len(row))


import_result_str = ""

result_list = list()

with open(file_path, newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        # print(row)
        # pdb.set_trace()
        result_list.append(row[4])

# print(result_list)
result_list.pop(0)

N = len(result_list)
print(N)

data = np.float64(result_list)

def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_lowpass_filter(data, cutoff=0.333, fs=30.0, order=6):
    data.astype(np.dtype('float64'))

    # print(data.dtype)
    # pdb.set_trace()

    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y

y = butter_lowpass_filter(data)

# yf = scipy.fftpack.fft(data)

# fig, ax = plt.subplots()
# ax.plot(range(int(N/50)),  np.abs(yf[0:N/50]))
# plt.show()

# plt.plot(range(len(result_list)), result_list)
# plt.grid(True)

# plt.show()

t = range(int(N))

# plt.subplot(2, 1, 2)
# plt.plot(t, data, 'b-', label='data')
plt.plot(t, y, 'g-', linewidth=2, label='filtered data')
plt.xlabel('Time [sec]')
plt.grid()
plt.legend()

plt.subplots_adjust(hspace=0.35)
plt.show()