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