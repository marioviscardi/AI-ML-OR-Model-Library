import torch
from torch import nn
class GPT(nn.Module):
 def __init__(self,v=2000,d=128,n=3,L=128):
  super().__init__(); self.tok=nn.Embedding(v,d); self.pos=nn.Embedding(L,d); layer=nn.TransformerEncoderLayer(d,4,4*d,batch_first=True); self.b=nn.TransformerEncoder(layer,n); self.h=nn.Linear(d,v)
 def forward(self,x):
  t=x.size(1); p=torch.arange(t,device=x.device); m=torch.triu(torch.full((t,t),float('-inf'),device=x.device),1); return self.h(self.b(self.tok(x)+self.pos(p)[None],mask=m))
print(GPT()(torch.randint(0,2000,(2,32))).shape)
