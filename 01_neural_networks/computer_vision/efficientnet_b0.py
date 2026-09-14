import torch
from torchvision.models import efficientnet_b0
m=efficientnet_b0(weights=None,num_classes=10); print(m(torch.randn(1,3,224,224)).shape)
