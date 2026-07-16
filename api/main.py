######## DAY 2 code #####
# from fastapi import FastAPI

# from pydantic import BaseModel

# app = FastAPI()

# class InputData(BaseModel):
#     value: float

# @app.get("/")
# def home():
#     return {"message": "PyTorch Prediction API"}

# @app.post("/predict")
# def predict(data: InputData):
#     prediction = data.value * 2

#     return {
#         "input": data.value,
#         "prediction": prediction
#     }


##### Day 3 Serving a Real PyTorch Model #####

# from fastapi import FastAPI
# from pydantic import BaseModel

# import torch
# from torch import nn

# #FastAPI app

# app = FastAPI()

# #Input scheme

# class InputData(BaseModel):
#     value:float


# class SimpleModel(nn.Module):

#     def __init__(self):
#         super().__init__()
#         self.linear = nn.Linear(1, 1)

#     def forward(self, x):
#         return self.linear(x)


# # -----------------------------
# # Load Trained Model
# # -----------------------------
# model = SimpleModel()

# model.load_state_dict(
#     # torch.load(
#     #     "/home/malik/mlops-practice/models/simple_model.pth"
#     # )

#     # for 4th day code adding below code commenting above

#     torch.load(
#     "models/simple_model.pth"
#     )
# )

# model.eval()


# # -----------------------------
# # Home Endpoint
# # -----------------------------
# @app.get("/")
# def home():
#     return {"message": "PyTorch Prediction API"}


# # -----------------------------
# # Prediction Endpoint
# # -----------------------------
# @app.post("/predict")
# def predict(data: InputData):

#     input_tensor = torch.tensor(
#         [[data.value]],
#         dtype=torch.float32
#     )

#     with torch.no_grad():
#         output = model(input_tensor)

#     prediction = output.item()

#     return {
#         "input": data.value,
#         "prediction": prediction
#     }


##### Day 5 use below #####

# from fastapi import FastAPI
# from api.schemas import InputData
# from api.model import predict

# app = FastAPI()


# @app.get("/")
# def home():
#     return {"message": "PyTorch Prediction API"}


# @app.post("/predict")
# def prediction(data: InputData):
#     result = predict(data.value)

#     return {"input": data.value, "prediction": result}

##### WEEK 6 Day 1 #####

# from fastapi import FastAPI

# from api.config import settings

# app = FastAPI(
#     title=settings.app_name,
#     version=settings.app_version,
# )


##### week 6 Day 2 #####

from fastapi import FastAPI

from api.config import settings
from api.logger import logger

logger.info("Starting FastAPI application")

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
)

logger.info("FastAPI application started successfully")