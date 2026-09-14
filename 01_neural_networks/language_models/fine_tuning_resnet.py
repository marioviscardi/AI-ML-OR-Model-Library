from torchvision.models import resnet18,ResNet18_Weights
from torch import nn
m=resnet18(weights=ResNet18_Weights.DEFAULT)
for p in m.parameters(): p.requires_grad=False
m.fc=nn.Linear(m.fc.in_features,5)
print(sum(p.numel() for p in m.parameters() if p.requires_grad))
