"""Transformer autoregressivo mínimo para modelagem de linguagem."""
import torch
from torch import nn

class TinyLM(nn.Module):
    def __init__(self, vocab_size=5000, d_model=128, nhead=4, layers=2, max_len=256):
        super().__init__()
        self.token = nn.Embedding(vocab_size, d_model)
        self.pos = nn.Embedding(max_len, d_model)
        layer = nn.TransformerEncoderLayer(d_model, nhead, 4*d_model, batch_first=True)
        self.encoder = nn.TransformerEncoder(layer, layers)
        self.head = nn.Linear(d_model, vocab_size)

    def forward(self, x):
        b, t = x.shape
        positions = torch.arange(t, device=x.device)
        h = self.token(x) + self.pos(positions)[None, :, :]
        mask = torch.triu(torch.ones(t, t, device=x.device), diagonal=1).bool()
        h = self.encoder(h, mask=mask)
        return self.head(h)

x = torch.randint(0, 5000, (4, 64))
model = TinyLM()
logits = model(x)
print(logits.shape)
