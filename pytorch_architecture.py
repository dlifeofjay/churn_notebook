import torch
import torch.nn as nn


class Churn(nn.Module):
    def __init__(self, n_feat, hidden1, hidden2, hidden3, out):
        super().__init__()
        self.model = nn.Sequential(
            nn.Linear(n_feat, hidden1),
            nn.ReLU(),
            nn.Linear(hidden1, hidden2),
            nn.ReLU(),
            nn.Linear(hidden2, hidden3),
            nn.ReLU(),
            nn.Linear(hidden3, out)
        )
    def forward(self, X):
        return self.model(X)