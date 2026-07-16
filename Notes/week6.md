# Week 6 - Day 1

## Topics Covered

- Environment Variables
- `.env` files
- Configuration Management
- Pydantic Settings
- Production-ready FastAPI configuration

## Key Concepts

- Configuration should be separated from application code.
- Environment variables allow the same application to run in different environments.
- `.env` files are useful for local development.
- Sensitive information should not be committed to Git.
- Pydantic Settings provides typed and centralized configuration management.
- Docker and Kubernetes commonly inject configuration through environment variables.

## Best Practices

- Keep secrets out of source control.
- Use a single settings class for configuration.
- Avoid hardcoded paths and values.
- Build your application once and configure it at deployment time.

# Week 6 - Day 2

## Topics Covered

- Introduction to Logging
- Python `logging` module
- Log Levels
- Creating a reusable logger
- Logging in FastAPI
- Production logging concepts

---

## What is Logging?

Logging is the process of recording events that occur while an application is running.

Unlike `print()`, logging provides:
- Timestamp
- Log level
- Logger name
- Consistent formatting
- Better debugging information

---

## Why Not Use `print()`?

`print()` is useful during development but has several limitations:

- No severity levels
- No timestamps
- Difficult to filter messages
- Not suitable for production applications

The Python `logging` module is the standard way to record application events.

---

## Log Levels

### DEBUG
Detailed information used during development.

Example:
- Variable values
- Tensor shapes
- Intermediate calculations

---

### INFO
Normal application events.

Example:
- Application started
- Model loaded
- Prediction request received

---

### WARNING
Something unexpected happened, but the application can continue.

Example:
- Configuration value missing (using default)
- Deprecated API usage

---

### ERROR
An operation failed.

Example:
- Prediction failed
- File not found

---

### CRITICAL
A serious error that may stop the application.

Example:
- Model cannot be loaded
- Application startup failed

---

## Logger Configuration

A reusable logger was created in:

api/logger.py

Responsibilities:
- Configure logging format
- Set log level
- Provide a common logger for the application

---

## Logging in FastAPI

Current logging includes:
- Application startup
- Application startup completion

Future logging will include:
- Model loading
- Prediction requests
- Prediction results
- Exceptions

---

## Production Logging

Containerized applications should write logs to stdout/stderr.

Docker collects these logs automatically.

Kubernetes allows viewing them using:

kubectl logs <pod-name>

In production, logs are commonly aggregated using systems such as:
- EFK (Elasticsearch, Fluent Bit, Kibana)
- Loki + Grafana

---

## Best Practices

- Use `logging` instead of `print()`.
- Write clear and meaningful log messages.
- Use appropriate log levels.
- Log exceptions with `logger.exception()`.
- Never log passwords, API keys, or other sensitive information.
- Keep log messages consistent and easy to search.

---

## Key Takeaways

- Logging helps monitor and troubleshoot applications.
- Production systems rely heavily on logs for debugging.
- A centralized logger improves consistency across the application.
- Good logging is an essential part of MLOps and DevOps practices.

# Week 6 – Day 3

## Topics Covered

- FastAPI Application Lifecycle
- Lifespan API
- Startup Phase
- Shutdown Phase
- `asynccontextmanager`
- `yield`

---

## What is Application Lifecycle?

Every FastAPI application goes through three phases:

1. Startup
2. Running
3. Shutdown

The lifecycle allows us to initialize resources before serving requests and clean them up when the application stops.

---

## Lifespan API

FastAPI provides the `lifespan` parameter to manage startup and shutdown events.

Example:

```python
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app):
    # Startup
    yield
    # Shutdown
```

The lifespan function is passed to the FastAPI application:

```python
app = FastAPI(lifespan=lifespan)
```

---

## Understanding `yield`

The `yield` statement divides the lifecycle into two parts.

### Before `yield`

Startup tasks execute.

Examples:
- Load ML model
- Connect to database
- Initialize cache
- Read configuration

### After `yield`

Shutdown tasks execute.

Examples:
- Close database connection
- Release resources
- Clean up background tasks

---

## Why Use Lifespan?

Without lifespan:

- Expensive initialization may happen repeatedly.
- Startup logic becomes scattered across the application.

With lifespan:

- Startup logic is centralized.
- Resources are initialized only once.
- Cleanup happens automatically.

---

## Why Is This Important for MLOps?

Machine learning models can be very large.

Loading a model for every request would be inefficient because it repeatedly:

- Reads the model from disk
- Deserializes it
- Allocates memory

Instead:

```
Application Starts
        │
        ▼
Load Model Once
        │
        ▼
Keep Model in Memory
        │
        ▼
Serve All Prediction Requests
        │
        ▼
Application Stops
```

This approach reduces latency and improves performance.

---

## Logging with Lifespan

Using the logger inside the lifespan function provides visibility into application startup and shutdown.

Example:

```python
logger.info("Application startup")

yield

logger.info("Application shutdown")
```

Observed output:

```
INFO mlops-api - Application startup
...
INFO mlops-api - Application shutdown
```

This confirms that the startup and shutdown phases executed successfully.

---

## Production Perspective

### Docker

When a Docker container starts:

- Container starts
- FastAPI startup executes
- Application becomes ready

### Kubernetes

When a Pod starts:

- Container starts
- Lifespan startup executes
- Readiness checks pass
- Pod begins receiving traffic

---

## Best Practices

- Use the modern Lifespan API instead of startup/shutdown event decorators for new projects.
- Keep startup logic inside the lifespan function.
- Perform expensive initialization only once.
- Clean up resources during shutdown.
- Use logging to track startup and shutdown events.

---

## Key Takeaways

- Every FastAPI application has a lifecycle.
- `yield` separates startup and shutdown logic.
- Lifespan centralizes initialization and cleanup.
- ML models should be loaded during startup and reused.
- Proper lifecycle management is essential for production-ready FastAPI applications.

# Week 6 - Day 4

## Topics Covered

- Model Loading
- Model Inference
- Separation of Responsibilities
- Production ML API Architecture

---

## Model Loading vs Model Inference

Machine learning applications perform two different tasks:

### 1. Model Loading

Responsibilities:

- Create the model object
- Load trained weights from the `.pth` file
- Set the model to evaluation mode
- Prepare the model for inference

This should happen **once** when the application starts.

---

### 2. Model Inference

Responsibilities:

- Accept input data
- Convert input into a tensor
- Run prediction using the loaded model
- Return the prediction

This happens for **every API request**.

---

## Why Separate These Tasks?

Loading a model is an expensive operation because it involves:

- Reading the model from disk
- Deserializing the model
- Allocating memory

Running inference is comparatively lightweight because it uses the already-loaded model.

Separating these responsibilities improves performance and keeps the code easier to maintain.

---

## Production Architecture

The recommended production flow is:

Application Starts
        │
        ▼
Load Model Once
        │
        ▼
Keep Model in Memory
        │
        ▼
Prediction Request
        │
        ▼
Run Inference
        │
        ▼
Return Prediction

---

## Why Not Load the Model for Every Request?

Loading the model for every request causes:

- Higher latency
- Increased CPU usage
- Unnecessary disk I/O
- Poor scalability

Instead, production systems load the model once and reuse it for all incoming requests.

---

## Key Takeaways

- Model loading and prediction are two separate responsibilities.
- Expensive initialization should happen during application startup.
- Prediction requests should reuse the already-loaded model.
- Separating concerns results in cleaner, more maintainable code.

# Week 6 - Day 5

## Topics Covered

- FastAPI Application State (`app.state`)
- Sharing Resources Across Requests
- Model Lifecycle
- Production ML API Architecture

---

## What is `app.state`?

`app.state` is a built-in FastAPI object used to store application-wide resources.

Resources stored in `app.state` are available throughout the lifetime of the application.

Example resources:

- Machine Learning Model
- Database Connection
- Redis Client
- Configuration Objects
- Cache Objects

---

## Why Use `app.state`?

Instead of creating resources repeatedly for every request, we initialize them once during application startup and reuse them.

Example:

```
Application Starts
        │
        ▼
Load Model
        │
        ▼
app.state.model
        │
        ▼
Reuse for Every Request
```

This improves performance and keeps resource management centralized.

---

## Why Not Use Global Variables?

Global variables may work in small applications, but they have several drawbacks:

- Harder to test
- Hidden shared state
- Poor maintainability
- Less explicit ownership

Using `app.state` makes it clear that the resource belongs to the FastAPI application.

---

## Production Request Flow

```
Client
   │
   ▼
FastAPI Endpoint
   │
   ▼
Retrieve Model from app.state
   │
   ▼
Run Prediction
   │
   ▼
Return Response
```

The model is reused for every prediction request.

---

## Relationship Between Components

During Week 6, the application architecture evolved as follows:

```
config.py
      │
      ▼
logger.py
      │
      ▼
lifespan()
      │
      ▼
Load Resources
      │
      ▼
app.state
      │
      ▼
Prediction Endpoint
```

Each component has a specific responsibility:

- `config.py` → Application configuration
- `logger.py` → Logging
- `lifespan()` → Startup and shutdown tasks
- `app.state` → Shared application resources

---

## Best Practices

- Initialize expensive resources only once.
- Store shared resources in `app.state`.
- Avoid loading models during every request.
- Keep startup logic inside the FastAPI lifespan function.
- Reuse loaded resources whenever possible.

---

## Key Takeaways

- `app.state` stores application-wide resources.
- Machine learning models should be loaded once and reused.
- Centralized resource management improves performance and maintainability.
- Separating initialization from request handling is a standard production practice.

# Week 6 - Day 6

## Topics Covered

- Refactoring the model layer
- Separating model definition, loading, and prediction
- Preparing for FastAPI integration

---

## Responsibilities in model.py

### Model Definition

Defines the neural network architecture using `torch.nn.Module`.

### Model Loading

Loads trained weights from the saved `.pth` file.

Responsibilities:

- Create model object
- Load weights
- Switch to evaluation mode
- Return the ready model

### Prediction

Uses the loaded model to perform inference.

Responsibilities:

- Convert input into a tensor
- Run inference
- Return prediction

---

## Why Separate These Responsibilities?

Benefits:

- Easier testing
- Better maintainability
- Clear separation of concerns
- Ready for production deployment

---

## Production Flow

```
Application Starts
        │
        ▼
Load Model
        │
        ▼
Store Model
        │
        ▼
Prediction Requests
        │
        ▼
Run Inference
```

---

## Best Practices

- Keep model loading separate from prediction.
- Call `model.eval()` before inference.
- Reuse the loaded model for every request.
- Log important events during model loading.

---

## Key Takeaways

- Model definition, loading, and prediction are separate responsibilities.
- Clean separation prepares the application for production.
- The next step is integrating the loaded model with FastAPI's lifecycle.