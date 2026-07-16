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