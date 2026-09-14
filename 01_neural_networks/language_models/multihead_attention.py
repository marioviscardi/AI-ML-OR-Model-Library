import torch
from torch import nn
m=nn.MultiheadAttention(64,4,batch_first=True); x=torch.randn(2,10,64); y,w=m(x,x,x); print(y.shape,w.shape)
