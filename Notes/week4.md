Week 4 Day 1 — Introduction to FastAPI & Model Serving
Goal

Understand how a trained Machine Learning model is exposed as a web service using FastAPI.

Instead of making predictions inside a Jupyter Notebook, other applications can send HTTP requests to our API and receive predictions.

1. What is FastAPI?

FastAPI is a modern Python web framework used to build APIs.

It is widely used in MLOps because it is:

Fast
Easy to learn
Automatically generates API documentation
Works well with Machine Learning libraries
2. Why Do We Need an API?

Without an API:

Notebook

↓

Run prediction manually

Only the developer can use the model.

With an API:

Client

↓

HTTP Request

↓

FastAPI

↓

PyTorch Model

↓

Prediction

↓

HTTP Response

Now any application can use the model.

Examples:

Web application
Mobile application
Backend service
Another API
3. What is an API?

API stands for:

Application Programming Interface

Think of it as a messenger between two programs.

Example:

Customer

↓

Waiter (API)

↓

Kitchen (Model)

↓

Waiter

↓

Customer

The customer never talks directly to the kitchen.

Similarly:

The client never talks directly to the ML model.

4. Installing FastAPI

Activate virtual environment:

cd ~/mlops-practice

source venv/bin/activate

Install packages:

pip install fastapi uvicorn

Verify installation:

pip show fastapi

pip show uvicorn
5. Project Structure
mlops-practice/

├── api/
│   └── main.py
│
├── data/
├── models/
├── notebooks/
├── scripts/
├── Notes/
└── venv/

Purpose of api/:

Store all FastAPI application files.

6. Creating FastAPI App

Example:

from fastapi import FastAPI

app = FastAPI()

Meaning:

Creates the FastAPI application object.

7. First Endpoint

Example:

@app.get("/")
def home():
    return {
        "message": "Hello MLOps!"
    }

Explanation:

@app.get("/")

Creates an HTTP GET endpoint.
/ is called the root endpoint.

When a browser visits:

http://127.0.0.1:8000/

Response:

{
    "message": "Hello MLOps!"
}
8. Running the Server

Command:

uvicorn api.main:app --reload

Explanation:

uvicorn

ASGI server that runs the FastAPI application.

api.main
api → folder
main → main.py
app

The FastAPI object:

app = FastAPI()
--reload

Automatically restarts the server whenever code changes are saved.

Useful during development.

9. API Documentation

Visit:

http://127.0.0.1:8000/docs

FastAPI automatically generates interactive documentation.

Features:

View endpoints
Test endpoints
See request format
See response format

No extra configuration required.

10. Common Log Messages

Example:

INFO: Uvicorn running on http://127.0.0.1:8000

Meaning:

Server started successfully.

GET / HTTP/1.1 200 OK

Meaning:

Root endpoint responded successfully.

GET /docs HTTP/1.1 200 OK

Meaning:

Swagger UI opened successfully.

GET /openapi.json HTTP/1.1 200 OK

Meaning:

FastAPI generated the OpenAPI specification.

GET /favicon.ico 404 Not Found

Meaning:

Browser requested a favicon (website icon).

Safe to ignore unless you add one later.

11. Request Flow
Browser

↓

GET /

↓

Uvicorn

↓

FastAPI

↓

@app.get("/")

↓

home()

↓

JSON Response

↓

Browser
12. Why FastAPI is Popular in MLOps

FastAPI provides:

High performance
Automatic API documentation
Data validation
Easy integration with ML frameworks
Easy deployment using Docker and Kubernetes
Week 4 Day 1 Completed ✅

Learned:

✔ What is FastAPI

✔ What is an API

✔ Why APIs are needed

✔ Project structure

✔ FastAPI application

✔ GET endpoint

✔ Running Uvicorn

✔ Automatic API documentation

✔ Understanding server logs

✔ Request/Response flow




Week 4 Day 2 — Building Your First Prediction API
Goal

Create a REST API that accepts input from a client and returns a prediction.

Current flow:

Client

↓

POST /predict

↓

FastAPI

↓

Prediction Logic

↓

JSON Response

(Today we used value * 2 as a placeholder. In the next lesson, this will be replaced by a real PyTorch model.)

1. GET vs POST
GET

Used to retrieve information.

Example:

@app.get("/")
def home():
    return {"message": "PyTorch Prediction API"}

Browser request:

GET /

Response:

{
    "message": "PyTorch Prediction API"
}
POST

Used to send data to the server.

Example:

@app.post("/predict")

Request:

{
    "value": 5
}

Response:

{
    "input": 5,
    "prediction": 10
}
2. Pydantic BaseModel

FastAPI uses Pydantic to validate incoming data.

Example:

from pydantic import BaseModel

class InputData(BaseModel):
    value: float

Expected JSON:

{
    "value": 5
}

FastAPI automatically:

Reads JSON
Validates the data
Converts it into a Python object
3. API Endpoint

Example:

@app.post("/predict")
def predict(data: InputData):

Meaning:

@app.post() creates a POST endpoint.
data is automatically created from the incoming JSON.
4. Accessing Request Data

Example:

data.value

If the request is:

{
    "value": 5
}

Then:

data.value

equals:

5
5. Prediction Logic

Temporary logic:

prediction = data.value * 2

Purpose:

Understand the API workflow before introducing the ML model.

6. Returning JSON

Example:

return {
    "input": data.value,
    "prediction": prediction
}

FastAPI automatically converts the Python dictionary into a JSON response.

7. Automatic Validation

Correct request:

{
    "value": 5
}

Incorrect request:

{
    "number": 5
}

or

{
    "value": "hello"
}

FastAPI returns a validation error automatically.

No extra validation code is required.

8. FastAPI Request Flow
Client

↓

POST /predict

↓

JSON Request

↓

Pydantic Validation

↓

predict()

↓

Prediction Logic

↓

Python Dictionary

↓

JSON Response

↓

Client
9. Important Concepts
BaseModel

Defines the expected structure of incoming JSON.

POST Endpoint

Receives data from the client.

Request Body

The JSON sent by the client.

Example:

{
    "value": 5
}
Response Body

The JSON returned by the server.

Example:

{
    "input": 5,
    "prediction": 10
}
10. Common Beginner Mistake

Creating the FastAPI application:

❌ Incorrect:

app = FastAPI

This only refers to the class.

✅ Correct:

app = FastAPI()

This creates a FastAPI application instance.

Remember:

list()          # Creates a list
dict()          # Creates a dictionary
FastAPI()       # Creates a FastAPI application
SimpleModel()   # Creates a PyTorch model
11. Current Project Structure
mlops-practice/

├── api/
│   └── main.py
│
├── models/
│   └── simple_model.pth
│
├── notebooks/
├── scripts/
├── data/
├── Notes/
└── venv/
Week 4 Day 2 Completed ✅

Learned:

✔ GET endpoint

✔ POST endpoint

✔ Request body

✔ Response body

✔ Pydantic BaseModel

✔ JSON request handling

✔ Automatic validation

✔ JSON responses

✔ FastAPI application creation

✔ Understanding request flow

Week 4 Day 3 — Serving a PyTorch Model with FastAPI
Goal

Replace the dummy prediction logic with a trained PyTorch model.

The API now performs real Machine Learning inference.

1. Complete Architecture
Client

↓

POST /predict

↓

FastAPI

↓

Load PyTorch Model

↓

Create Tensor

↓

Model Inference

↓

Prediction

↓

JSON Response

This is the basic architecture of an ML inference service.

2. Import Required Libraries
from fastapi import FastAPI
from pydantic import BaseModel

import torch
from torch import nn

Purpose:

FastAPI → Create API
BaseModel → Validate request data
torch → PyTorch framework
nn → Neural network components
3. Create FastAPI Application
app = FastAPI()

Creates the FastAPI application instance.

4. Define Input Schema
class InputData(BaseModel):
    value: float

Expected request:

{
    "value": 5
}

FastAPI automatically validates and converts the JSON into a Python object.

5. Recreate the Model Architecture

PyTorch saves only the model parameters (weights and bias), not the model class.

Therefore, the same architecture must be recreated:

class SimpleModel(nn.Module):

    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(1, 1)

    def forward(self, x):
        return self.linear(x)
6. Load the Trained Model
model = SimpleModel()

model.load_state_dict(
    torch.load(
        "/home/malik/mlops-practice/models/simple_model.pth"
    )
)

model.eval()
Why load once?

The model is loaded when the API starts, not for every request.

Benefits:

Faster response time
Less disk I/O
Better performance
7. Prediction Endpoint
@app.post("/predict")
def predict(data: InputData):

Receives a POST request containing JSON input.

8. Convert Input to Tensor

Incoming JSON:

{
    "value": 5
}

PyTorch requires tensors:

input_tensor = torch.tensor(
    [[data.value]],
    dtype=torch.float32
)

Result:

tensor([[5.0]])
9. Run Inference
with torch.no_grad():
    output = model(input_tensor)

Why torch.no_grad()?

During inference:

No training
No gradient calculation
Lower memory usage
Faster execution
10. Convert Tensor to Python Number

Model output:

tensor([[9.3733]])

Convert to a Python value:

prediction = output.item()

Result:

9.3733

This allows FastAPI to return it as JSON.

11. Return JSON Response
return {
    "input": data.value,
    "prediction": prediction
}

Response:

{
    "input": 5,
    "prediction": 9.3733
}
12. Request Flow
Client

↓

POST /predict

↓

JSON Request

↓

Pydantic Validation

↓

Tensor Creation

↓

PyTorch Model

↓

Prediction

↓

Python Dictionary

↓

JSON Response

↓

Client
13. Why Prediction Isn't Exactly 10

The model was trained to learn the relationship from data.

It was not programmed with:

prediction = value * 2

Instead, it learned weights and bias during training.

Therefore, predictions are approximate.

Example:

Expected:

5 → 10

Model prediction:

5 → 9.3733

This is normal for a trained ML model.

14. Difference Between Rule-Based and ML-Based Prediction

Rule-based:

prediction = value * 2
Exact result
Manually coded logic

Machine Learning:

Input

↓

Learned Weights

↓

Prediction
Learned from data
Approximate prediction
15. Project Structure
mlops-practice/

├── api/
│   └── main.py
│
├── models/
│   └── simple_model.pth
│
├── notebooks/
├── scripts/
├── data/
├── Notes/
└── venv/
Week 4 Day 3 Completed ✅

Learned:

✔ Load trained PyTorch model

✔ Recreate model architecture

✔ load_state_dict()

✔ model.eval()

✔ Tensor creation

✔ torch.no_grad()

✔ Model inference

✔ Convert tensor to Python value

✔ Return ML predictions through FastAPI

✔ Complete ML inference request flow

Overall ML Inference Lifecycle
Train Model

↓

Save Model (.pth)

↓

FastAPI Starts

↓

Load Model

↓

Client Sends Request

↓

Convert JSON → Tensor

↓

PyTorch Inference

↓

Prediction

↓

JSON Response


Week 4 Day 4 – Dockerizing a Machine Learning API
Goal

Package the complete Machine Learning application into a Docker container so it can run consistently on any machine without manually installing Python or dependencies.

Why Docker?

Without Docker:

Python version may differ.
Required libraries may not be installed.
Different operating systems may behave differently.
"It works on my machine" becomes a common problem.

Docker solves this by packaging:

Python
FastAPI
PyTorch
Model file
Project code
Dependencies

into a single portable image.

Docker Workflow
Application Code
        │
        ▼
Dockerfile
        │
        ▼
docker build
        │
        ▼
Docker Image
        │
        ▼
docker run
        │
        ▼
Running Container
Project Structure
mlops-practice/

├── api/
│   └── main.py
│
├── models/
│   └── simple_model.pth
│
├── requirements.txt
├── Dockerfile
├── .dockerignore
│
├── notebooks/
├── scripts/
├── data/
├── Notes/
└── venv/
requirements.txt

Lists all Python packages required by the application.

Example:

fastapi
uvicorn
torch
pydantic

During the Docker build, these packages are installed automatically.

Dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
Understanding Each Instruction
FROM
FROM python:3.12-slim
Selects the base image.
Includes Python 3.12.
Slim version keeps the image smaller.
WORKDIR
WORKDIR /app

Sets the working directory inside the container.

All future commands execute from:

/app
COPY
COPY requirements.txt .

Copies requirements.txt into the container.

Later:

COPY . .

Copies the complete project.

RUN
RUN pip install --no-cache-dir -r requirements.txt

Installs all required Python packages.

This step happens only while building the image.

EXPOSE
EXPOSE 8000

Documents that the application listens on port 8000.

CMD
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]

Starts the FastAPI application when the container launches.

Why Relative Paths?

Instead of:

torch.load("/home/malik/mlops-practice/models/simple_model.pth")

Use:

torch.load("models/simple_model.pth")

Reason:

Absolute paths only work on one computer.
Relative paths work on laptops, servers, cloud VMs, and Docker containers.
.dockerignore

Purpose:

Prevent unnecessary files from being copied into the Docker image.

Example:

venv/
.git/
__pycache__/
*.pyc
.ipynb_checkpoints/
notebooks/
Notes/
data/

Benefits:

Faster builds
Smaller build context
Cleaner images
Build Docker Image

Command:

docker build -t mlops-api:v1 .

Explanation:

build → Create image
-t → Assign a name and tag
mlops-api → Image name
v1 → Version tag
. → Use the current directory as the build context
View Images

Command:

docker images

Example:

REPOSITORY    TAG    IMAGE ID       SIZE
mlops-api     v1     xxxxxxxxxxxx   994MB
Run Container

Command:

docker run -p 8000:8000 mlops-api:v1

Meaning:

Host Port 8000
      │
      ▼
Container Port 8000

The API becomes accessible at:

http://localhost:8000
Test the API

Open:

http://localhost:8000/docs

Example request:

{
    "value": 5
}

Example response:

{
    "input": 5,
    "prediction": 9.373371124267578
}

This confirms:

FastAPI is running.
The PyTorch model loaded successfully.
Inference works inside the Docker container.
Docker Image vs Docker Container
Docker Image
Read-only template
Built once
Can create many containers

Example:

mlops-api:v1
Docker Container

A running instance of an image.

Example:

Docker Image
      │
      ▼
docker run
      │
      ▼
Running Container
MLOps Workflow
Dataset
      │
      ▼
Train Model
      │
      ▼
Save Model (.pth)
      │
      ▼
FastAPI
      │
      ▼
Docker Image
      │
      ▼
Docker Container
      │
      ▼
REST API
      │
      ▼
Prediction
Commands Learned
docker --version

Check Docker installation.

docker build -t mlops-api:v1 .

Build Docker image.

docker images

List available images.

docker run -p 8000:8000 mlops-api:v1

Run the container.

Key Concepts Learned
Docker Image
Docker Container
Dockerfile
requirements.txt
.dockerignore
Build Context
Relative Paths
Port Mapping
FastAPI inside Docker
PyTorch Model Serving
Containerized ML API
Week 4 Day 4 Completed ✅

You have successfully:

✔ Built a Docker image.

✔ Containerized a FastAPI application.

✔ Loaded a trained PyTorch model inside Docker.

✔ Exposed the model as a REST API.

✔ Verified predictions from a running container.

Milestone Achieved

You have now completed a complete end-to-end Machine Learning deployment pipeline:

Data
   │
   ▼
Model Training
   │
   ▼
Model Saving
   │
   ▼
FastAPI Service
   │
   ▼
Docker Image
   │
   ▼
Docker Container
   │
   ▼
Prediction API

This is the foundation of modern MLOps systems. Future topics such as Kubernetes, CI/CD, model registries, and cloud deployments build upon this workflow.

Week 4 - Day 5 Notes
Topic: Production-Ready Project Structure & Docker Verification
Objective

Learn how to organize an ML API into a clean, maintainable project structure and verify that it runs successfully both locally and inside a Docker container.

Project Structure
mlops-practice/
│
├── api/
│   ├── __init__.py
│   ├── main.py
│   ├── model.py
│   ├── schemas.py
│   └── config.py
│
├── models/
│   └── simple_model.pth
│
├── data/
├── notebooks/
├── scripts/
├── tests/
├── Notes/
│
├── Dockerfile
├── requirements.txt
├── .dockerignore
└── README.md
Purpose of Each File
main.py
Creates the FastAPI application.
Defines API endpoints.
Calls the prediction function.
model.py
Loads the trained PyTorch model.
Performs inference.
Keeps ML logic separate from API logic.
schemas.py
Stores Pydantic request/response models.
Validates incoming JSON data.
config.py
Stores configuration values.
Example:
Model path
File locations
Future environment variables
Why Separate Files?

Instead of placing everything inside one file:

API
Model loading
Prediction logic
Configuration

we divide responsibilities.

Benefits
Easier to maintain
Easier to debug
Cleaner code
Better team collaboration
Easier testing
Production-ready structure
Single Responsibility Principle (SRP)

Each file should have one responsibility.

Example:

main.py → API
model.py → ML model
schemas.py → Validation
config.py → Configuration

This is a widely used software engineering principle.

FastAPI Flow
Client

   │

POST /predict

   │

FastAPI

   │

Pydantic Validation

   │

predict()

   │

PyTorch Model

   │

Prediction

   │

JSON Response
Docker Build

Build the Docker image:

docker build -t mlops-api:v2 .

Creates a reusable Docker image containing:

Python
FastAPI
PyTorch
Project files
Dependencies
Docker Run

Run the container:

docker run -p 8001:8000 mlops-api:v2

Explanation:

Host Port: 8001
Container Port: 8000

Reason:

Port 8000 was already used by the local Uvicorn server.

Verify API

Open:

http://localhost:8001/docs

Test request:

{
    "value": 5
}

Response:

{
    "input": 5,
    "prediction": 9.373371124267578
}

This confirms:

Docker image works.
FastAPI works.
Model loads correctly.
Predictions are returned successfully.
Commands Learned

Start FastAPI locally:

uvicorn api.main:app --reload

Build Docker image:

docker build -t mlops-api:v2 .

Run Docker container:

docker run -p 8001:8000 mlops-api:v2

View Docker images:

docker images

View running containers:

docker ps

Stop a running container:

docker stop <container_id>
Common Errors Encountered
1. Parent directory does not exist

Reason:

Saving a model to a folder that doesn't exist.

Solution:

Create the directory or use the correct project path.

2. FastAPI.get() missing required positional argument

Reason:

Forgot parentheses.

Incorrect:

app = FastAPI

Correct:

app = FastAPI()
3. Address already in use

Reason:

Another process was already using port 8000.

Solutions:

Stop the existing process.
Use another host port (e.g., 8001).
4. Docker Build Failed (torchc)

Reason:

Typo in package name.

Incorrect:

torchc

Correct:

torch
Key Concepts Learned
Production folder structure
Separation of concerns
Single Responsibility Principle (SRP)
API layer
Model layer
Configuration layer
Pydantic validation
Docker image
Docker container
Port mapping
API verification inside Docker
Real-World MLOps Workflow
Train Model
      │
      ▼
Save Model (.pth)
      │
      ▼
Load Model
      │
      ▼
FastAPI
      │
      ▼
Docker
      │
      ▼
Deploy
Week 4 Summary

Day 1

FastAPI Basics

Day 2

Request Validation with Pydantic

Day 3

Load PyTorch Model & Perform Inference

Day 4

Dockerize the ML API

Day 5

Production Project Structure
Docker Verification
Separation of Concerns
Interview Questions
Why use FastAPI?
Build high-performance REST APIs.
Automatic request validation.
Interactive Swagger documentation.
Easy integration with ML models.
Why use Pydantic?
Validates input data.
Prevents invalid requests.
Converts JSON into Python objects.
Why Dockerize an ML API?
Consistent execution across environments.
Easy deployment.
Dependency isolation.
Portable application.
Why separate model.py from main.py?
Improves maintainability.
Makes testing easier.
Follows the Single Responsibility Principle.
Keeps business logic independent from API logic.
Key Takeaways
Organize projects into logical modules.
Keep API, model, validation, and configuration separate.
Verify applications both locally and inside Docker.
Docker images should behave the same regardless of the machine they run on.
Production-ready code is not just about making it work—it's about making it maintainable, testable, and deployable.