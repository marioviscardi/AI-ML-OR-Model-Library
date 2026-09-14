"""Comparação dos principais otimizadores disponíveis no PyTorch."""
import torch
from torch import nn

model=nn.Sequential(nn.Linear(10,32),nn.ReLU(),nn.Linear(32,1))
optimizers = {
    "SGD": torch.optim.SGD(model.parameters(), lr=1e-2),
    "Momentum": torch.optim.SGD(model.parameters(), lr=1e-2, momentum=.9),
    "Adagrad": torch.optim.Adagrad(model.parameters(), lr=1e-2),
    "RMSprop": torch.optim.RMSprop(model.parameters(), lr=1e-3),
    "Adam": torch.optim.Adam(model.parameters(), lr=1e-3),
    "AdamW": torch.optim.AdamW(model.parameters(), lr=1e-3),
}
print(list(optimizers))
