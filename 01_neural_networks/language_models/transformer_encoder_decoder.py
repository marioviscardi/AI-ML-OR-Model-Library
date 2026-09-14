import torch
from torch import nn
class T(nn.Module):
 def __init__(self,v=1000,d=128): super().__init__(); self.e=nn.Embedding(v,d); self.t=nn.Transformer(d,4,2,2,batch_first=True); self.o=nn.Linear(d,v)
 def forward(self,s,t): return self.o(self.t(self.e(s),self.e(t)))
m=T(); print(m(torch.randint(0,1000,(2,12)),torch.randint(0,1000,(2,8))).shape)
