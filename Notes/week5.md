# Week 5 - CI/CD & Software Engineering Practices

---

# Day 1 - Git & GitHub Integration

## Objective

Today we integrated our MLOps project with Git and GitHub. Version control is one of the most important skills for every DevOps, MLOps, and Software Engineer. From this point onward, every change to our project will be tracked and backed up in GitHub.

---

## Topics Covered

- Git Initialization
- GitHub Repository Creation
- .gitignore
- .dockerignore
- Git Commit
- Git Remote
- GitHub Authentication
- Push Project to GitHub

---

# Why Git?

Git is a Distributed Version Control System (DVCS) used to:

- Track source code changes
- Collaborate with developers
- Roll back to previous versions
- Maintain project history
- Integrate with CI/CD pipelines

Without Git, professional software development is nearly impossible.

---

# Why GitHub?

GitHub is a cloud platform that hosts Git repositories.

Benefits:

- Backup code
- Team collaboration
- Pull Requests
- Issue Tracking
- GitHub Actions (CI/CD)
- Portfolio for recruiters

---

# Initialize Git Repository

```bash
git init
```

Creates the hidden `.git` directory inside the project.

Verify:

```bash
ls -la
```

You should see:

```
.git/
```

---

# Verify Repository Location

Initially, Git was accidentally initialized in the home directory.

We verified the correct project location using:

```bash
pwd
git rev-parse --show-toplevel
```

Expected Output:

```
/home/malik/mlops-practice
```

This ensures only the MLOps project is tracked.

---

# Create .gitignore

Example:

```gitignore
venv/
__pycache__/
.ipynb_checkpoints/
*.pyc
```

Purpose:

- Ignore virtual environments
- Ignore Python cache
- Ignore notebook checkpoints
- Keep repository clean

---

# Create .dockerignore

Example:

```dockerignore
venv
.git
__pycache__
.ipynb_checkpoints
```

Purpose:

- Reduce Docker build context
- Faster Docker builds
- Smaller images

---

# Check Repository Status

```bash
git status
```

Shows:

- New files
- Modified files
- Deleted files
- Files ready to commit

---

# Stage Files

```bash
git add .
```

Stages every project file.

---

# Commit Changes

```bash
git commit -m "Initial commit"
```

Creates the first project snapshot.

---

# Create GitHub Repository

Repository Name:

```
mlops-practice
```

Repository Type:

- Public

Do **not** initialize with:

- README
- .gitignore
- License

because these already exist locally.

---

# Connect Local Repository

```bash
git remote add origin https://github.com/MALIKROTE/mlops-practice.git
```

Verify:

```bash
git remote -v
```

Output:

```
origin
```

---

# Authentication Issue

Initially received:

```
Invalid username or token.
Password authentication is not supported.
```

Reason:

GitHub no longer allows account passwords for Git operations over HTTPS.

Solution:

Authenticated using GitHub CLI (`gh auth login`) and completed the device authorization process.

---

# Push Code to GitHub

```bash
git push -u origin main
```

Successful Output:

```
[new branch] main -> main
branch 'main' set up to track 'origin/main'
```

Now the local `main` branch tracks the remote `main` branch.

Future pushes only require:

```bash
git push
```

---

# Useful Git Commands

Check status

```bash
git status
```

Stage files

```bash
git add .
```

Commit changes

```bash
git commit -m "message"
```

Push changes

```bash
git push
```

Pull latest changes

```bash
git pull
```

View commit history

```bash
git log --oneline
```

View remote repository

```bash
git remote -v
```

---

# Project Structure

Current project structure:

```
mlops-practice/
│
├── api/
├── data/
├── models/
├── notebooks/
├── Notes/
├── Dockerfile
├── README.md
├── requirements.txt
├── .gitignore
└── .dockerignore
```

---

# Interview Questions

### What is Git?

Git is a Distributed Version Control System used to track changes in source code.

---

### What is GitHub?

GitHub is a cloud platform used to host Git repositories and collaborate with developers.

---

### What is the difference between Git and GitHub?

Git is the version control software.

GitHub is a cloud hosting service for Git repositories.

---

### Why use .gitignore?

To prevent unnecessary files such as virtual environments, cache files, and temporary files from being committed.

---

### Difference between git add and git commit

**git add**

Stages files for commit.

**git commit**

Creates a permanent snapshot of staged changes.

---

### Difference between git push and git pull

**git push**

Uploads local commits to GitHub.

**git pull**

Downloads the latest commits from GitHub.

---

# Commands Learned Today

```bash
git init

git status

git add .

git commit -m "Initial commit"

git remote add origin <repository-url>

git remote -v

git push -u origin main

git push

git pull

git log --oneline
```

---

# Summary

Today we successfully:

- Initialized a Git repository
- Fixed the repository location
- Created `.gitignore`
- Created `.dockerignore`
- Made the initial commit
- Created a GitHub repository
- Connected the local repository to GitHub
- Authenticated using GitHub CLI
- Successfully pushed the project to GitHub
- Established a professional Git workflow for the remainder of the MLOps roadmap

The project is now version-controlled and securely hosted on GitHub, providing a solid foundation for CI/CD, collaboration, and future deployments.



# Week 5 - Day 2
# Topic: Unit Testing FastAPI using Pytest

## Objective

Learn how to automatically test FastAPI endpoints using pytest before deploying applications.

---

## Why Testing?

Testing helps verify that the API behaves correctly without manually using Swagger UI.

Benefits:

- Detect bugs early
- Prevent deployment failures
- Validate API responses automatically
- Essential for CI/CD pipelines

---

## Packages Installed

```bash
pip install pytest
pip install httpx
```

Update dependencies:

```bash
pip freeze > requirements.txt
```

---

## Project Structure

```
mlops-practice/
│
├── api/
├── tests/
│   └── test_api.py
├── models/
├── notebooks/
├── Notes/
├── Dockerfile
└── requirements.txt
```

---

## Test Client

FastAPI provides TestClient for testing APIs without running Uvicorn.

```python
from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)
```

---

## Home Endpoint Test

```python
response = client.get("/")
```

Checks:

- Status Code = 200
- Correct JSON response

---

## Prediction Endpoint Test

```python
response = client.post(
    "/predict",
    json={
        "value": 5
    }
)
```

Checks:

- Status Code = 200
- Prediction exists
- Prediction is float

---

## Bug Encountered

Initial test failed.

Error:

```
422 Unprocessable Entity
```

Reason:

Test sent:

```json
{
    "input":5
}
```

But API expected:

```json
{
    "value":5
}
```

The request field name did not match the Pydantic schema.

---

## Fix

Changed:

```python
json={
    "input":5
}
```

to

```python
json={
    "value":5
}
```

---

## Test Result

```bash
pytest
```

Output:

```
2 passed
```

---

## Key Learnings

- Unit testing validates API functionality.
- TestClient simulates API requests.
- pytest automates testing.
- Pydantic validates request bodies.
- A 422 error usually indicates invalid request data.
- Tests should match the API schema exactly.

---

## Commands Learned

```bash
pip install pytest

pip install httpx

pip freeze > requirements.txt

pytest
```

---

## Status

✅ Week 5 Day 2 Completed

# Week 5 - Day 3
# Topic: API Validation Testing with Pytest

## Objective

Learn how to test invalid API requests and ensure FastAPI properly validates incoming data using Pydantic.

---

## Why Validation Testing?

Users do not always send valid input.

Instead of crashing, APIs should reject invalid requests with meaningful error responses.

Validation testing ensures the API is secure, reliable, and predictable.

---

## Existing Tests

Previously implemented:

- Home endpoint test
- Prediction endpoint test

These verify the API works correctly with valid input.

---

## New Validation Tests

### 1. Missing Required Field

Request:

```json
{}
```

Expected Result:

```
422 Unprocessable Entity
```

Reason:

The required field `value` is missing.

---

### 2. Invalid Data Type

Request:

```json
{
    "value": "hello"
}
```

Expected Result:

```
422 Unprocessable Entity
```

Reason:

The API expects a float but received a string.

---

### 3. Null Value

Request:

```json
{
    "value": null
}
```

Expected Result:

```
422 Unprocessable Entity
```

Reason:

The field cannot be null because it is defined as a float.

---

### 4. Negative Number Test (Bonus)

Request:

```json
{
    "value": -5
}
```

Expected Result:

```
200 OK
```

Reason:

The current model accepts any floating-point number.

No business validation has been implemented yet.

---

## Why FastAPI Returns 422

Input validation is performed before the endpoint function executes.

Flow:

```
Client Request
       │
       ▼
Pydantic Validation
       │
 ┌─────┴─────┐
 │           │
Valid     Invalid
 │           │
 ▼           ▼
API      Return 422
Function
```

If validation fails, the endpoint function is never executed.

---

## Test Execution

Run:

```bash
pytest
```

Result:

```
6 passed
```

---

## Key Learnings

- FastAPI automatically validates request data.
- Pydantic checks input types before executing endpoint logic.
- Invalid requests return HTTP 422.
- Unit tests should include both success and failure scenarios.
- Edge-case testing increases application reliability.
- Automated tests help prevent bugs from reaching production.

---

## Commands Used

```bash
pytest
```

---

## Status

✅ Week 5 Day 3 Completed

# Week 5 - Day 4 Notes

## Topic: GitHub Actions (Continuous Integration)

### Objective

Learn how to automate testing using GitHub Actions so that every code change pushed to GitHub is automatically tested.

---

# What is GitHub Actions?

GitHub Actions is GitHub's built-in Continuous Integration (CI) and Continuous Deployment (CD) platform.

Instead of manually running tests every time we change the code, GitHub Actions automatically runs them whenever we push code to the repository.

Example workflow:

```text
Write Code
    │
    ▼
git push
    │
    ▼
GitHub Actions
    │
    ▼
Create Ubuntu Runner
    │
    ▼
Install Dependencies
    │
    ▼
Run Tests
    │
    ▼
Pass / Fail
```

---

# Why CI is Important

Benefits of Continuous Integration:

* Automatically verifies every code change.
* Prevents broken code from reaching production.
* Ensures the project works on a clean machine.
* Saves time by detecting issues early.
* Standard practice in DevOps and MLOps teams.

---

# GitHub Actions Workflow

Created workflow file:

```text
.github/workflows/python-tests.yml
```

Purpose:

* Trigger on every push
* Checkout repository
* Install Python
* Install dependencies
* Execute pytest

---

# First CI Failure

The first workflow failed with the error:

```text
ERROR: Invalid requirement: 'pip freeze'
```

Reason:

`requirements.txt` mistakenly contained:

```text
fastapi
uvicorn
pydantic
pip freeze
```

`pip freeze` is a terminal command, **not** a Python package.

---

# Correct requirements.txt

Updated to:

```text
fastapi
uvicorn
pydantic
torch
pytest
httpx
```

Later, we also decided to add:

```text
numpy
```

because PyTorch uses NumPy in many ML workflows.

---

# Important Difference

Correct command:

```bash
pip freeze > requirements.txt
```

This command **generates** a requirements file.

Incorrect:

```text
pip freeze
```

inside `requirements.txt`.

Remember:

* `pip freeze` → terminal command
* `requirements.txt` → package list only

---

# GitHub Authentication

While pushing to GitHub, authentication initially failed:

```text
Invalid username or token.
Password authentication is not supported.
```

After re-authenticating, the repository was successfully pushed.

---

# Successful GitHub Actions Run

After fixing `requirements.txt`, GitHub Actions completed successfully.

Result:

```text
6 tests passed
```

Workflow executed:

1. Created Ubuntu runner
2. Installed Python
3. Installed project dependencies
4. Executed pytest
5. All tests passed

This confirms the project works correctly on a clean environment.

---

# Warnings Observed

### FastAPI Warning

```text
StarletteDeprecationWarning
```

Safe to ignore for now.

It comes from FastAPI/Starlette internals.

---

### PyTorch Warning

```text
No module named 'numpy'
```

Reason:

NumPy was missing from the GitHub runner.

Solution:

Add `numpy` to `requirements.txt`.

---

# CI Pipeline Built

Current development workflow:

```text
Write Code
      │
      ▼
Run pytest Locally
      │
      ▼
git add
      │
      ▼
git commit
      │
      ▼
git push
      │
      ▼
GitHub Actions
      │
      ▼
Install Dependencies
      │
      ▼
Run Tests
      │
      ▼
Success / Failure
```

---

# Skills Learned Today

* Introduction to Continuous Integration (CI)
* GitHub Actions workflow
* Workflow file structure
* Automatic test execution
* Reading GitHub Actions logs
* Debugging CI failures
* Fixing dependency issues
* Understanding `requirements.txt`
* GitHub authentication for Git operations
* Importance of testing on a clean environment

---

# Key Takeaways

* CI automatically validates every code push.
* `requirements.txt` must contain only package names.
* Always test projects on a clean environment.
* GitHub Actions is an essential DevOps and MLOps skill.
* A passing CI pipeline increases confidence that the project is stable.

---

# Progress Summary

Completed so far:

* ✅ Week 1 - Python, NumPy, Pandas
* ✅ Week 2 - Machine Learning Fundamentals
* ✅ Week 3 - PyTorch Model Training
* ✅ Week 4 - FastAPI + Docker
* ✅ Week 5 Day 1 - Git & GitHub
* ✅ Week 5 Day 2 - API Testing with Pytest
* ✅ Week 5 Day 3 - Additional API Test Cases
* ✅ Week 5 Day 4 - GitHub Actions CI

Current project features:

* FastAPI Prediction API
* Trained PyTorch model
* Unit tests
* Dockerized application
* GitHub repository
* Automated CI pipeline using GitHub Actions
