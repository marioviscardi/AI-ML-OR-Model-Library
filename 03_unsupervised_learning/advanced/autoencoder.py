import torch
from torch import nn
class AE(nn.Module):
 def __init__(self): super().__init__(); self.e=nn.Sequential(nn.Linear(64,32),nn.ReLU(),nn.Linear(32,8)); self.d=nn.Sequential(nn.Linear(8,32),nn.ReLU(),nn.Linear(32,64))
 def forward(self,x): return self.d(self.e(x))
print(AE()(torch.randn(16,64)).shape)
