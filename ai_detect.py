import torch
import numpy as np
from cnn_model import ECGCNN

model = ECGCNN()
model.load_state_dict(torch.load("ecg_model.pt"))
model.eval()

labels = [
"Normal",
"PVC",
"Atrial Fibrillation",
"Tachycardia",
"Bradycardia"
]

def detect(signal):

    signal = np.array(signal)

    signal = signal[:187]

    tensor = torch.tensor(signal).float().unsqueeze(0).unsqueeze(0)

    output = model(tensor)

    pred = torch.argmax(output)

    return labels[pred]