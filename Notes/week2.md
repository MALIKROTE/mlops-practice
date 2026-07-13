Week 2 Day 1 — Regression Notes
Goal

Learn how ML predicts continuous values.

Example:

Input:

Experience

Output:

Salary

This is called Regression.

1. Imports Used
Pandas
import pandas as pd

Purpose:

Create datasets
Handle tables
Data cleaning
NumPy
import numpy as np

Purpose:

Numerical operations
Arrays
Missing values (np.nan)
Matplotlib
import matplotlib.pyplot as plt

Purpose:

Visualization
Graphs
Train/Test Split
from sklearn.model_selection import train_test_split

Purpose:
Split data into:

Training Data → Model learns

Testing Data → Model is checked
Linear Regression
from sklearn.linear_model import LinearRegression

Purpose:

Create a regression ML model.

Evaluation Metric
from sklearn.metrics import mean_absolute_error

Purpose:

Measure prediction error.

2. Creating Dataset

Dictionary:

data = {
    "experience":[1,2,3,4],
    "salary":[25000,30000,40000,50000]
}

Convert dictionary to DataFrame:

df = pd.DataFrame(data)

Output:

experience	salary
1	25000
2	30000
3. DataFrame

A Pandas table.

Example:

df

Useful functions:

View first rows
df.head()
Dataset information
df.info()
Statistics
df.describe()
Dataset size
df.shape

Example:

(100,2)

means:

100 rows

2 columns

4. Feature and Target

ML has:

Feature (Input)

Variable used for prediction.

Example:

experience

Code:

X = df[["experience"]]
Target (Output)

What we want to predict.

Example:

salary

Code:

y = df["salary"]

Remember:

X = Question

y = Answer
5. Train/Test Split

Import:

from sklearn.model_selection import train_test_split

Code:

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

Meaning:

Dataset

    |
    |
Split

    |
    |

Training Data     Testing Data

Learn             Check
6. Creating Model

Create model:

model = LinearRegression()

Train model:

model.fit(
    X_train,
    y_train
)

Important:

.fit()

means:

"Model learns patterns from data"

7. Prediction

Predict:

prediction = model.predict(X_test)

Meaning:

Give new data:

Experience = 5

Model predicts salary
8. Compare Results

Create table:

comparison = pd.DataFrame({
    "Actual": y_test,
    "Prediction": prediction
})

Example:

Actual	Prediction
50000	48750
9. Model Evaluation

MAE:

Mean Absolute Error

Import:

from sklearn.metrics import mean_absolute_error

Calculate:

error = mean_absolute_error(
    y_test,
    prediction
)

Example output:

1250

Meaning:

Model prediction is wrong by around 1250 on average.

Complete ML Flow
Dataset

    ↓

Feature + Target

    ↓

Train/Test Split

    ↓

Create Model

    ↓

model.fit()

    ↓

model.predict()

    ↓

Evaluate Metric
Important Functions To Remember
Pandas
pd.DataFrame()

df.head()

df.info()

df.describe()

df.shape
Scikit Learn
train_test_split()

model.fit()

model.predict()

mean_absolute_error()

Week 2 Day 1 Completed ✅

Learned:

✔ Regression concept
✔ Linear Regression
✔ Training model
✔ Prediction
✔ MAE evaluation


Week 2 Day 2 — Classification Notes
Goal

Learn ML models that predict categories/classes.

Examples:

Email → Spam / Not Spam

Customer → Buy / Not Buy

Student → Pass / Fail

Unlike regression:

Regression:
Output = Number

Example:
Salary = 50000


Classification:
Output = Category

Example:
Pass = 1
Fail = 0
1. Imports Used
Pandas
import pandas as pd

Used for:

Creating datasets
DataFrames
Data handling
NumPy
import numpy as np

Used for:

Numerical operations
Arrays
Matplotlib
import matplotlib.pyplot as plt

Used for:

Graphs
Visualization
Train/Test Split
from sklearn.model_selection import train_test_split

Used to split dataset:

Training Data → Learn

Testing Data → Check
Logistic Regression Model
from sklearn.linear_model import LogisticRegression

Used for classification problems.

Example:

Study Hours + Attendance

        ↓

Pass / Fail
Accuracy Metric
from sklearn.metrics import accuracy_score

Used to check:

How many predictions are correct.

2. Creating Dataset

Example:

data = {
    "study_hours":[1,2,3,4,5],
    "attendance":[40,45,50,60,65],
    "pass":[0,0,0,1,1]
}

Convert to DataFrame:

df = pd.DataFrame(data)

Dataset:

study_hours	attendance	pass
1	40	0
5	65	1
3. Feature and Target

Features:

Input values:

X = df[["study_hours","attendance"]]

Target:

Output:

y = df["pass"]

Remember:

X = Input

y = Answer
4. Train/Test Split

Code:

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

Meaning:

Complete Dataset

        ↓

Split

        ↓

Training Data     Testing Data

Learn             Evaluate
5. Creating Model

Create classifier:

model = LogisticRegression()
6. Training Model
model.fit(
    X_train,
    y_train
)

Meaning:

Model learns patterns:

Study Hours
+
Attendance

        ↓

Pass / Fail
7. Prediction
prediction = model.predict(X_test)

Output:

1 = Pass

0 = Fail

Example:

[1 0]

Means:

First prediction:
Pass

Second prediction:
Fail

8. Compare Actual vs Prediction

Create comparison:

comparison = pd.DataFrame({
    "Actual": y_test,
    "Prediction": prediction
})

Example output:

Actual	Prediction
1	1
0	0

Meaning:

Both predictions are correct.

9. Accuracy

Calculate:

accuracy = accuracy_score(
    y_test,
    prediction
)

Example:

1.0

Means:

100% predictions were correct.

Regression vs Classification
Regression

Output:

Number

Example:

House Price
Salary
Temperature

Model:

LinearRegression()

Metric:

mean_absolute_error()
Classification

Output:

Category

Example:

Spam / Not Spam

Pass / Fail

Model:

LogisticRegression()

Metric:

accuracy_score()
ML Workflow
Dataset

    ↓

Features + Target

    ↓

Train/Test Split

    ↓

Create Model

    ↓

model.fit()

    ↓

model.predict()

    ↓

Evaluation
Week 2 Day 2 Completed ✅

Learned:

✔ Classification concept
✔ Logistic Regression
✔ Training classifier
✔ Prediction
✔ Accuracy evaluation


Week 2 Day 3 — Model Evaluation Metrics Notes
Goal

Understand how to evaluate a classification model.

A model prediction is not enough. We need to measure:

How many predictions are correct?
How many positive cases were found?
How many wrong predictions happened?
1. Imports Used
Pandas
import pandas as pd

Used for:

Creating DataFrames
Comparing actual vs prediction
NumPy
import numpy as np

Used for:

Numerical operations
Evaluation Metrics
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)

Used for:

Model evaluation
2. Actual vs Prediction

Actual values:

y_true = [1,0,1,1,0,1,0,0,1,0]

Prediction values:

y_pred = [1,0,1,0,0,1,0,1,1,0]

Meaning:

1 = Positive

0 = Negative
3. Accuracy

Question:

How many total predictions are correct?

Formula:

Accuracy =
Correct Predictions
------------------
Total Predictions

Code:

accuracy = accuracy_score(
    y_true,
    y_pred
)

Example:

0.8

Meaning:

80% predictions are correct
4. Confusion Matrix

Code:

cm = confusion_matrix(
    y_true,
    y_pred
)

Output:

[[4 1]
 [1 4]]

Structure:

              Predicted

              0      1

Actual 0      TN     FP

Actual 1      FN     TP
Confusion Matrix Terms
True Negative (TN)

Actual:

0

Prediction:

0

Correct negative prediction.

True Positive (TP)

Actual:

1

Prediction:

1

Correct positive prediction.

False Positive (FP)

Actual:

0

Prediction:

1

Wrong positive prediction.

Example:

Normal email predicted as spam.

False Negative (FN)

Actual:

1

Prediction:

0

Missed positive case.

Example:

Spam email predicted as normal.

5. Precision

Question:

When model predicts Positive,
how often is it correct?

Formula:

Precision = TP / (TP + FP)

Code:

precision = precision_score(
    y_true,
    y_pred
)

Example:

0.8

Meaning:

80% of positive predictions were correct.

6. Recall

Question:

Out of all actual positive cases,
how many did the model find?

Formula:

Recall = TP / (TP + FN)

Code:

recall = recall_score(
    y_true,
    y_pred
)

Example:

0.8

Meaning:

Model found 80% of actual positive cases.

7. F1 Score

F1 combines:

Precision + Recall

Formula:

F1 =
2 × (Precision × Recall)
------------------------
Precision + Recall

Code:

f1 = f1_score(
    y_true,
    y_pred
)

Example:

0.8
Easy Memory Trick
Accuracy
Overall how many correct?
Precision
Predicted YES → was it really YES?
Recall
Actual YES → did we find them?
F1 Score
Balance between Precision and Recall
Evaluation Flow
Model Prediction

        ↓

Actual vs Prediction

        ↓

Confusion Matrix

        ↓

Metrics

        ↓

Accuracy
Precision
Recall
F1 Score
Week 2 Day 3 Completed ✅

Learned:

✔ Accuracy
✔ Confusion Matrix
✔ True Positive
✔ True Negative
✔ False Positive
✔ False Negative
✔ Precision
✔ Recall
✔ F1 Score


Week 2 Final Notes — ML Basics
Goal

Understand the complete Machine Learning workflow:

Prepare data
Train models
Make predictions
Evaluate performance
Compare models
1. ML Types
Regression

Used when output is a number.

Examples:

Experience → Salary

House details → Price

Output:

50000

Common Model:

LinearRegression()

Metric:

mean_absolute_error()
Classification

Used when output is a category.

Examples:

Email → Spam / Not Spam

Student → Pass / Fail

Output:

1 = Yes

0 = No

Common Model:

LogisticRegression()

Metrics:

accuracy_score()

precision_score()

recall_score()

f1_score()
2. Important Imports
Pandas
import pandas as pd

Purpose:

Dataset handling
DataFrame creation
Data cleaning

Example:

df = pd.DataFrame(data)
NumPy
import numpy as np

Purpose:

Numerical operations
Arrays
Missing values

Example:

np.nan
Matplotlib
import matplotlib.pyplot as plt

Purpose:

Visualization
Graphs
3. Creating Dataset

Dictionary:

data = {

"feature":[1,2,3],

"target":[10,20,30]

}

Convert to DataFrame:

df = pd.DataFrame(data)
4. Understanding Dataset

First rows:

df.head()

Information:

df.info()

Statistics:

df.describe()

Size:

df.shape

Example:

(100,5)

means:

100 rows

5 columns
5. Feature and Target

Feature:

Input:

X = df[["column_name"]]

Target:

Output:

y = df["target"]

Remember:

X = Question

y = Answer
6. Train/Test Split

Import:

from sklearn.model_selection import train_test_split

Code:

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

Meaning:

Training Data

↓
Model learns


Testing Data

↓
Model is checked
7. Model Training

Create model:

Example:

model = LinearRegression()

Train:

model.fit(
X_train,
y_train
)

Meaning:

Model learns patterns
8. Prediction

Code:

prediction = model.predict(X_test)

Meaning:

Give input

↓

Model predicts output
9. Regression Evaluation
MAE

Mean Absolute Error

Import:

from sklearn.metrics import mean_absolute_error

Code:

error = mean_absolute_error(
y_test,
prediction
)

Meaning:

Average prediction mistake.

Example:

MAE = 1250

Model is wrong by around 1250
10. Classification Evaluation
Accuracy

Question:

How many predictions are correct?

Code:

accuracy_score(
y_true,
y_pred
)
Confusion Matrix

Code:

confusion_matrix(
y_true,
y_pred
)

Structure:

              Predicted

              0       1

Actual 0      TN      FP

Actual 1      FN      TP
True Positive (TP)

Actual:

1

Prediction:

1

Correct positive.

True Negative (TN)

Actual:

0

Prediction:

0

Correct negative.

False Positive (FP)

Actual:

0

Prediction:

1

Wrong positive.

False Negative (FN)

Actual:

1

Prediction:

0

Missed positive.

11. Precision

Question:

When model says YES,
is it really YES?

Code:

precision_score(
y_true,
y_pred
)
12. Recall

Question:

Did we find all actual YES cases?

Code:

recall_score(
y_true,
y_pred
)
13. F1 Score

Combination of:

Precision + Recall

Code:

f1_score(
y_true,
y_pred
)
14. Overfitting

Meaning:

Model memorizes training data.

Example:

Training accuracy = 100%

Testing accuracy = 50%

Problem:

Model cannot generalize.

15. Underfitting

Meaning:

Model is too simple.

Example:

Training accuracy = Low

Testing accuracy = Low

Model did not learn enough.

16. Model Comparison

Train multiple models:

Example:

Model 1:

Linear Regression


Model 2:

Polynomial Regression

Compare:

pd.DataFrame({

"Model":[
"Model1",
"Model2"
],

"MAE":[
error1,
error2
]

})

Rule:

Lower error = Better model
Complete ML Lifecycle
Dataset

    ↓

Data Cleaning

    ↓

Features + Target

    ↓

Train/Test Split

    ↓

Model Training

    ↓

Prediction

    ↓

Evaluation

    ↓

Model Comparison

    ↓

Save Model
Week 2 Completed ✅

Covered:

✔ Regression
✔ Classification
✔ Linear Regression
✔ Logistic Regression
✔ Train/Test Split
✔ Prediction
✔ MAE
✔ Accuracy
✔ Precision
✔ Recall
✔ F1 Score
✔ Confusion Matrix
✔ Overfitting
✔ Underfitting
✔ Model Comparison