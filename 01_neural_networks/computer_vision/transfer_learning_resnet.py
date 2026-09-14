"""Transfer learning com ResNet18 em PyTorch."""
import torch
from torch import nn
from torchvision.models import resnet18, ResNet18_Weights

num_classes = 5
weights = ResNet18_Weights.DEFAULT
model = resnet18(weights=weights)

for p in model.parameters():
    p.requires_grad = False

model.fc = nn.Linear(model.fc.in_features, num_classes)
print(model)
print("Preprocessamento recomendado:", weights.transforms())
