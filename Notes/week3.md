Week 3 Day 1 — PyTorch Basics Notes
Goal

Understand PyTorch fundamentals.

PyTorch is a deep learning framework used for:

Neural Networks
Deep Learning
Model training
GPU acceleration
1. Import PyTorch
import torch

Check version:

torch.__version__

Example:

2.x.x
2. Tensor

Tensor is the main data structure in PyTorch.

Comparison:

NumPy → ndarray

PyTorch → Tensor

Example:

x = torch.tensor([1,2,3,4])

Output:

tensor([1,2,3,4])
3. Tensor Properties
Data Type
x.dtype

Example:

torch.int64
Shape
x.shape

Example:

torch.Size([4])

Meaning:

4 values in tensor.

4. Matrix Tensor

Example:

matrix = torch.tensor([
    [1,2],
    [3,4]
])

Shape:

matrix.shape

Output:

torch.Size([2,2])

Meaning:

2 rows

2 columns

5. Tensor Operations

Addition:

a = torch.tensor([1,2,3])

b = torch.tensor([4,5,6])

a+b

Output:

tensor([5,7,9])

Multiplication:

a*b

Output:

tensor([4,10,18])
6. Random Tensor

Very common in neural networks.

Create:

random_tensor = torch.rand(3,3)

Creates:

3 x 3 tensor

with random values between:

0 and 1
7. Important Difference

NumPy:

import numpy as np

array = np.array([1,2,3])

PyTorch:

import torch

tensor = torch.tensor([1,2,3])

Similar idea, different ecosystem.

PyTorch Flow
Data

 ↓

Tensor

 ↓

Neural Network

 ↓

Training

 ↓

Model

 ↓

Prediction
Week 3 Day 1 Completed ✅

Learned:

✔ PyTorch installation
✔ Import torch
✔ Tensor creation
✔ Tensor shape
✔ Tensor operations
✔ Random tensors




Week 3 Day 2 — Neural Network Basics Notes
Goal

Understand the basic structure of a Neural Network using PyTorch.

A neural network learns patterns by adjusting:

Weights
Bias
1. Import PyTorch
import torch

from torch import nn

nn means:

Neural Network module

It provides:

Layers
Models
Loss functions
Training utilities
2. Neural Network Concept

Basic flow:

Input Data

      ↓

Neural Network Layers

      ↓

Prediction

      ↓

Compare with Actual Output

      ↓

Update Weights
3. Creating Data

Example problem:

Learn:

y = 2x

Input:

X = torch.tensor([
    [1],
    [2],
    [3],
    [4]
], dtype=torch.float32)

Output:

y = torch.tensor([
    [2],
    [4],
    [6],
    [8]
], dtype=torch.float32)
4. Neural Network Layer

A simple neural network:

Input

 ↓

Linear Layer

 ↓

Output

PyTorch layer:

nn.Linear()

A linear layer learns:

weight
+
bias

Formula:

y = weight * x + bias
5. Creating a Neural Network

Example:

class SimpleModel(nn.Module):

    def __init__(self):

        super().__init__()

        self.linear = nn.Linear(
            1,
            1
        )


    def forward(self,x):

        return self.linear(x)
6. Understanding nn.Linear
nn.Linear(1,1)

Meaning:

Input:

1 value

Output:

1 value

Example:

Input:
Experience

Output:
Salary
7. Create Model
model = SimpleModel()

Check:

model

Output:

SimpleModel(
 (linear): Linear(in_features=1, out_features=1)
)
8. Forward Pass

Prediction:

prediction = model(X)

The model uses:

Input

↓

Weights + Bias

↓

Output

Before training:

Prediction will be wrong because weights are random.

9. Model Parameters

Check learned values:

for param in model.parameters():

    print(param)

Example output:

weight:

tensor([[-0.9829]])

bias:

tensor([0.4086])

These are randomly initialized.

During training they change.

10. Important Concept

Traditional ML:

Give features

Model learns relationship

Neural Network:

Give data

Network learns:

Weights
+
Bias
Neural Network Learning Process
Input

 ↓

Prediction

 ↓

Calculate Error

 ↓

Adjust Weights

 ↓

Better Prediction
Week 3 Day 2 Completed ✅

Learned:

✔ Neural Network basics
✔ PyTorch nn.Module
✔ Linear layer
✔ Forward pass
✔ Weights
✔ Bias
✔ Model parameters




Week 3 Day 3 — PyTorch Training Loop Notes
Goal

Understand how a Neural Network learns.

Training means:

Make predictions
Calculate error
Adjust weights
Repeat until error reduces
1. Training Flow

Complete learning process:

Input Data

      ↓

Forward Pass

      ↓

Prediction

      ↓

Calculate Loss

      ↓

Backpropagation

      ↓

Update Weights

      ↓

Repeat
2. Create Training Data

Example:

Learning:

y = 2x

Input:

X = torch.tensor([
    [1],
    [2],
    [3],
    [4]
], dtype=torch.float32)

Output:

y = torch.tensor([
    [2],
    [4],
    [6],
    [8]
], dtype=torch.float32)
3. Neural Network Model

Create model:

class SimpleModel(nn.Module):

    def __init__(self):

        super().__init__()

        self.linear = nn.Linear(
            1,
            1
        )


    def forward(self,x):

        return self.linear(x)
4. Loss Function

Loss tells:

How wrong is the model?

For regression:

loss_fn = nn.MSELoss()

MSE:

Mean Squared Error

Formula:

(prediction - actual)^2

Lower loss means better model.

5. Optimizer

Optimizer updates weights.

Example:

optimizer = torch.optim.SGD(
    model.parameters(),
    lr=0.01
)

Meaning:

SGD:

Algorithm to update weights


lr:

Learning speed
6. Epoch

Epoch means:

One complete pass through training data.

Example:

epochs = 100

Means:

Model sees data 100 times.

7. Training Loop

Code:

for epoch in range(epochs):

    prediction = model(X)


    loss = loss_fn(
        prediction,
        y
    )


    optimizer.zero_grad()


    loss.backward()


    optimizer.step()
8. Forward Pass

Prediction step:

prediction = model(X)

Model calculates:

Input

↓

Weights + Bias

↓

Prediction
9. Backpropagation

Code:

loss.backward()

Purpose:

Finds how much each weight contributed to error.

Then adjusts weights.

10. Update Weights

Code:

optimizer.step()

Purpose:

Changes:

Weight
Bias

to reduce error.

11. Example Training Output

Initial loss:

52.13

After training:

0.006

Meaning:

Model improved.

12. Final Prediction Example

After training:

Input:

1 → 2.12

2 → 4.05

3 → 5.99

4 → 7.93

Expected:

2,4,6,8

Model learned the pattern.

Important Concepts
Loss

Measures:

How wrong is prediction?
Backpropagation

Finds:

What should change?
Optimizer

Does:

Actually changes weights
PyTorch Learning Cycle
Data

 ↓

Model

 ↓

Prediction

 ↓

Loss

 ↓

Backward

 ↓

Optimizer

 ↓

Better Model
Week 3 Day 3 Completed ✅

Learned:

✔ Training loop
✔ Loss function
✔ MSELoss
✔ Optimizer
✔ SGD
✔ Epochs
✔ Forward pass
✔ Backpropagation
✔ Weight updates


Week 3 Day 4 — Saving and Loading PyTorch Models Notes
Goal

Learn how to save a trained model and load it again for prediction.

In real MLOps systems:

Train Model

      ↓

Save Model

      ↓

Deploy Model

      ↓

Load Model

      ↓

Prediction
1. Why Save Models?

Without saving:

Train every time ❌

With saving:

Train once

↓

Save model

↓

Use anywhere
2. Model Parameters

A Neural Network learns:

Weight
Bias

Example:

y = weight * x + bias

These values are stored in:

model.state_dict()
3. Save Model

PyTorch saves model parameters using:

torch.save()

Example:

torch.save(
    model.state_dict(),
    "models/simple_model.pth"
)

Creates:

models/

└── simple_model.pth
4. state_dict()

Meaning:

A dictionary containing:

Model weights
Model bias

Check:

model.state_dict()
5. Loading Model

Important:

First create the same model architecture.

Example:

new_model = SimpleModel()

Then load saved parameters:

new_model.load_state_dict(
    torch.load(
        "models/simple_model.pth"
    )
)

Now:

new_model

=

trained model
6. Evaluation Mode

Before prediction:

new_model.eval()

Meaning:

Switch model to inference mode.

Used for:

Testing
Prediction
Deployment
7. Training Mode vs Evaluation Mode

Training:

model.train()

Used for:

Learning
Updating weights

Prediction:

model.eval()

Used for:

Inference
Production
8. Prediction After Loading

Example:

prediction = new_model(X)

Output:

Close to actual values

Example:

Expected:

2,4,6,8

Prediction:

2.15,4.07,5.99,7.91
9. Complete Model Lifecycle
Dataset

 ↓

Train Model

 ↓

Save model.pth

 ↓

Load Model

 ↓

API / Application

 ↓

Prediction
MLOps Connection

Saved PyTorch model:

simple_model.pth

Later:

FastAPI

↓

Docker

↓

Kubernetes

↓

Production
Week 3 Day 4 Completed ✅

Learned:

✔ Save model
✔ state_dict
✔ Load model
✔ Evaluation mode
✔ Inference concept
✔ Model lifecycle



Week 3 Day 5 — Model Inference Practice Notes
Goal

Learn how to use a trained PyTorch model for prediction without training again.

Real ML workflow:

Train Model

      ↓

Save Model

      ↓

Load Model

      ↓

New Data

      ↓

Prediction
1. Training vs Inference
Training

Used when the model learns.

model.train()

Process:

Data

↓

Prediction

↓

Loss

↓

Backpropagation

↓

Update Weights
Inference

Used when the model only predicts.

model.eval()

Process:

New Data

↓

Trained Model

↓

Prediction
2. Load Model Architecture

PyTorch saves only:

Weights
Bias

It does not save the model structure.

So we recreate the class:

class SimpleModel(nn.Module):

    def __init__(self):

        super().__init__()

        self.linear = nn.Linear(
            1,
            1
        )


    def forward(self,x):

        return self.linear(x)
3. Create Model
model = SimpleModel()

Initially:

Random weights
4. Load Trained Parameters
model.load_state_dict(
    torch.load(
        "models/simple_model.pth"
    )
)

Now:

Random Model

↓

Trained Model
5. Evaluation Mode

Before prediction:

model.eval()

Why?

Because:

No weight updates
No training operations
Faster prediction
6. New Input Data

Example:

new_data = torch.tensor(
    [
        [5],
        [10],
        [20]
    ],
    dtype=torch.float32
)

The model predicts output for unseen data.

7. Prediction

Use:

with torch.no_grad():

    prediction = model(new_data)

Why torch.no_grad()?

During inference:

No gradients required
Less memory usage
Faster execution
8. Convert Tensor Output

Tensor:

prediction

Convert:

prediction.numpy()

or:

prediction.tolist()
Example Result

Input:

5
10
20

Prediction:

9.37
17.85
34.81

Expected approximately:

10
20
40
Complete PyTorch Lifecycle
Dataset

↓

Tensor

↓

Neural Network

↓

Training Loop

↓

Save Model

↓

Load Model

↓

Inference

↓

Prediction
MLOps Connection

Saved model:

simple_model.pth

Later becomes:

PyTorch Model

↓

FastAPI Endpoint

↓

Docker Container

↓

Kubernetes Deployment
Week 3 Completed ✅

Learned:

✔ PyTorch basics
✔ Tensors
✔ Neural Networks
✔ Training loop
✔ Loss functions
✔ Optimizers
✔ Saving models
✔ Loading models
✔ Inference workflow