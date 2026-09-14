import torch
from torchvision.models import googlenet
m=googlenet(weights=None,aux_logits=False,num_classes=10); print(m(torch.randn(1,3,224,224)).shape)
