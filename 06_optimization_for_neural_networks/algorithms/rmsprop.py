import torch
from torch import nn
m=nn.Linear(4,1);opt=torch.optim.RMSprop(m.parameters(),lr=.001);print(opt)
