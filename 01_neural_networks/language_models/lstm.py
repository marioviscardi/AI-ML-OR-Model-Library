import torch
from torch import nn
m=nn.LSTM(8,32,batch_first=True); y,(h,c)=m(torch.randn(4,20,8)); print(y.shape,h.shape,c.shape)
