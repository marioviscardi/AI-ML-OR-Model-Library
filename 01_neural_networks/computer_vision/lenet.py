import torch
from torch import nn
class LeNet(nn.Module):
 def __init__(self,c=10):
  super().__init__(); self.m=nn.Sequential(nn.Conv2d(1,6,5),nn.Tanh(),nn.AvgPool2d(2),nn.Conv2d(6,16,5),nn.Tanh(),nn.AvgPool2d(2),nn.Flatten(),nn.Linear(400,120),nn.Tanh(),nn.Linear(120,84),nn.Tanh(),nn.Linear(84,c))
 def forward(self,x): return self.m(x)
print(LeNet()(torch.randn(2,1,32,32)).shape)
