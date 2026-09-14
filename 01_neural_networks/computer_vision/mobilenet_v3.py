import torch
from torchvision.models import mobilenet_v3_small
m=mobilenet_v3_small(weights=None,num_classes=10); print(m(torch.randn(1,3,224,224)).shape)
