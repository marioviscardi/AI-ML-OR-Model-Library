import torch
from torch import nn
m=nn.Linear(4,1);opt=torch.optim.SGD(m.parameters(),lr=.01);print(opt)
