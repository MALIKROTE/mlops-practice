Week 1 — Python for ML Notes
1. NumPy

NumPy = Numerical Python

Used for:

arrays
mathematical operations
ML data processing

Import:

import numpy as np

Create array:

numbers = np.array([10,20,30,40])

Useful operations:

numbers.mean()
numbers.sum()
numbers.max()
numbers.min()

Check dimensions:

numbers.shape

Example:

data = np.array([
    [25,2],
    [30,5],
    [35,8]
])

Shape:

(3,2)

Meaning:

3 rows  = 3 examples
2 columns = 2 features
2. Pandas

Pandas is used for working with datasets.

Import:

import pandas as pd

Create DataFrame:

df = pd.DataFrame({
    "age":[25,30,35],
    "salary":[30000,50000,70000]
})

DataFrame looks like:

age	salary
25	30000
30	50000
35	70000
Data inspection

First rows:

df.head()

Information:

df.info()

Statistics:

df.describe()
3. Features and Target

ML dataset has:

Features (X)

Input given to model.

Example:

age
experience
location

Code:

X = df[["age","experience"]]
Target (y)

Output model predicts.

Example:

salary

Code:

y = df["salary"]
4. Train/Test Split

Why split?

Because model should be tested on unseen data.

Flow:

Complete Dataset
        |
        |
   Split Data
        |
        |
Training Data     Testing Data
     |                 |
Learn model       Check model

Code:

from sklearn.model_selection import train_test_split


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)
Important Terms
Training Data

Used for learning patterns.

Testing Data

Used for checking performance.

Feature

Input variable.

Example:

house size
number of rooms
Label / Target

Prediction output.

Example:

house price
Week 1 ML Workflow
Raw Dataset
      |
      ↓
Pandas Load Data
      |
      ↓
Clean Data
      |
      ↓
Select Features + Target
      |
      ↓
Train/Test Split
      |
      ↓
Model Training (Week 2)