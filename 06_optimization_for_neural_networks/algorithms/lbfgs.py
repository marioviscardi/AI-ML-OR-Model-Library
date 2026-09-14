import torch
from torch import nn
x=torch.linspace(-2,2,100)[:,None];y=3*x+1;m=nn.Linear(1,1);o=torch.optim.LBFGS(m.parameters(),lr=.8,max_iter=30);L=nn.MSELoss()
def c():o.zero_grad();z=L(m(x),y);z.backward();return z
o.step(c);print(m.weight.item(),m.bias.item())
