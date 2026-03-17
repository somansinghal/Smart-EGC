import numpy as np
from scipy.signal import find_peaks

def detect_heart_rate(signal, fs=250):

    peaks,_ = find_peaks(signal, height=0.5, distance=fs*0.4)

    rr_intervals = np.diff(peaks) / fs

    bpm = 60 / np.mean(rr_intervals)

    return int(bpm)