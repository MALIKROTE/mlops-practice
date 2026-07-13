import torch
from torch import nn

from api.config import MODEL_PATH


class SimpleModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(1, 1)

    def forward(self, x):
        return self.linear(x)


model = SimpleModel()
model.load_state_dict(torch.load(MODEL_PATH))
model.eval()


def predict(value: float):
    with torch.no_grad():
        x = torch.tensor([[value]], dtype=torch.float32)
        prediction = model(x)
        return prediction.item()