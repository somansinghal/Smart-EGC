import torch
import numpy as np

def predict_ecg(signal):

    hr = np.mean(signal)

    if hr > 120:
        return "Tachycardia"

    if hr < 50:
        return "Bradycardia"

    return "Normal"