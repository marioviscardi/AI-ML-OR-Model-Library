import torch
from torch import nn
def blk(a,b): return nn.Sequential(nn.Conv2d(a,b,3,padding=1),nn.ReLU(),nn.Conv2d(b,b,3,padding=1),nn.ReLU())
class UNet(nn.Module):
 def __init__(self,c=2):
  super().__init__(); self.e1=blk(3,32); self.p=nn.MaxPool2d(2); self.e2=blk(32,64); self.b=blk(64,128); self.u2=nn.ConvTranspose2d(128,64,2,2); self.d2=blk(128,64); self.u1=nn.ConvTranspose2d(64,32,2,2); self.d1=blk(64,32); self.o=nn.Conv2d(32,c,1)
 def forward(self,x):
  a=self.e1(x); b=self.e2(self.p(a)); z=self.b(self.p(b)); z=self.d2(torch.cat([self.u2(z),b],1)); z=self.d1(torch.cat([self.u1(z),a],1)); return self.o(z)
print(UNet()(torch.randn(1,3,128,128)).shape)
