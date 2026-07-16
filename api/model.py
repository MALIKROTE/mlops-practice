import torch
from torch import nn

from api.config import settings
from api.logger import logger


MODEL_PATH = settings.model_path


class SimpleModel(nn.Module):

    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(1, 1)

    def forward(self, x):
        return self.linear(x)


def load_model():

    logger.info(f"Loading model from {MODEL_PATH}")

    model = SimpleModel()

    model.load_state_dict(
        torch.load(MODEL_PATH)
    )

    model.eval()

    logger.info("Model loaded successfully")

    return model


def predict(model, value: float):

    input_tensor = torch.tensor(
        [[value]],
        dtype=torch.float32
    )

    with torch.no_grad():
        output = model(input_tensor)

    return output.item()