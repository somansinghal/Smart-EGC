import numpy as np
from scipy.signal import butter, filtfilt

def bandpass_filter(signal, low=0.5, high=40, fs=250):

    nyquist = 0.5 * fs

    low = low / nyquist
    high = high / nyquist

    b,a = butter(4,[low,high],btype='band')

    filtered = filtfilt(b,a,signal)

    return filtered