import torch
from torch import nn
class Enc(nn.Module):
 def __init__(self,v=100,e=32,h=64): super().__init__(); self.e=nn.Embedding(v,e); self.r=nn.GRU(e,h,batch_first=True)
 def forward(self,x): return self.r(self.e(x))
class Dec(nn.Module):
 def __init__(self,v=100,e=32,h=64): super().__init__(); self.e=nn.Embedding(v,e); self.r=nn.GRU(e,h,batch_first=True); self.o=nn.Linear(h,v)
 def forward(self,x,h): y,h=self.r(self.e(x),h); return self.o(y),h
e,d=Enc(),Dec(); _,h=e(torch.randint(0,100,(2,8))); y,_=d(torch.randint(0,100,(2,5)),h); print(y.shape)
