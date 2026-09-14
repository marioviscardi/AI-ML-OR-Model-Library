import torch
from torchvision.models import vit_b_16
m=vit_b_16(weights=None,num_classes=10); print(m(torch.randn(1,3,224,224)).shape)
