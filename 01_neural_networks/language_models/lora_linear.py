import torch
from torch import nn
class LoRA(nn.Module):
 def __init__(self,i,o,r=4,a=8):
  super().__init__(); self.base=nn.Linear(i,o); [p.requires_grad_(False) for p in self.base.parameters()]; self.A=nn.Parameter(torch.randn(i,r)*.01); self.B=nn.Parameter(torch.zeros(r,o)); self.s=a/r
 def forward(self,x): return self.base(x)+(x@self.A@self.B)*self.s
print(LoRA(32,16)(torch.randn(4,32)).shape)
