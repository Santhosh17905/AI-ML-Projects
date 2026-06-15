import torch
import torch.nn as nn
import torch.nn.functional as F
import os

class Linear_QNet(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super().__init__()
        self.linear1 = nn.Linear(input_size, hidden_size)
        self.linear2 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        x = F.relu(self.linear1(x))
        return self.linear2(x)

    def save(self, file_name='models/model.pth'):
        os.makedirs('models', exist_ok=True)
        torch.save(self.state_dict(), file_name)

    def load(self, file_name='models/model.pth'):
        self.load_state_dict(torch.load(file_name))
        self.eval()