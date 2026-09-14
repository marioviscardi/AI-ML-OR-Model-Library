import torch
from torchvision.models import resnet18
m=resnet18(weights=None,num_classes=10); print(m(torch.randn(1,3,224,224)).shape)
