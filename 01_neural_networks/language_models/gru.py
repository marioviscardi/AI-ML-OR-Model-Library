import torch
from torch import nn
m=nn.GRU(8,32,batch_first=True); y,h=m(torch.randn(4,20,8)); print(y.shape,h.shape)
