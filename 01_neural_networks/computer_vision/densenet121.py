import torch
from torchvision.models import densenet121
m=densenet121(weights=None,num_classes=10); print(m(torch.randn(1,3,224,224)).shape)
