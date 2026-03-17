import torch
import torch.nn as nn

class ECGCNN(nn.Module):

    def __init__(self):
        super().__init__()

        self.conv1 = nn.Conv1d(1,16,5)
        self.pool = nn.MaxPool1d(2)

        self.conv2 = nn.Conv1d(16,32,5)

        self.fc1 = nn.Linear(736,64)
        self.fc2 = nn.Linear(64,5)

    def forward(self,x):

        x=self.pool(torch.relu(self.conv1(x)))
        x=self.pool(torch.relu(self.conv2(x)))

        x=x.view(x.size(0),-1)

        x=torch.relu(self.fc1(x))
        x=self.fc2(x)

        return x