import torch
import torch.nn as nn

class ECGModel(nn.Module):

    def __init__(self):
        super().__init__()

        self.model = nn.Sequential(

            nn.Linear(187,128),
            nn.ReLU(),

            nn.Linear(128,64),
            nn.ReLU(),

            nn.Linear(64,5)
        )

    def forward(self,x):
        return self.model(x)