"""Scaled dot-product self-attention, forma compacta."""
import torch
from torch import nn

class SelfAttention(nn.Module):
    def __init__(self, d_model=64):
        super().__init__()
        self.q = nn.Linear(d_model, d_model)
        self.k = nn.Linear(d_model, d_model)
        self.v = nn.Linear(d_model, d_model)
        self.scale = d_model ** -0.5

    def forward(self, x):
        q, k, v = self.q(x), self.k(x), self.v(x)
        scores = q @ k.transpose(-2, -1) * self.scale
        weights = scores.softmax(dim=-1)
        return weights @ v

x = torch.randn(2, 10, 64)
print(SelfAttention()(x).shape)
