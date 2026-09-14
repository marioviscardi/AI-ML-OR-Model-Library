import torch
from torch import nn
m=nn.Linear(4,1);opt=torch.optim.AdamW(m.parameters(),lr=.001,weight_decay=.01);print(opt)
