# API Test Suite
![Tests](https://github.com/ndeoki/api-test-suite/actions/workflows/tests.yml/badge.svg)

An automated test suite for validating REST API endpoints, built with Python and pytest. Tests run automatically on every push via GitHub Actions.

## Overview

This suite verifies the behavior of REST API endpoints against their documented specifications, covering the full range of CRUD operations and including negative test cases. It demonstrates requirements-based test design, data-driven testing, and continuous integration.

## What It Tests

- **GET** requests: status codes, response structure, and data correctness
- **POST** requests: resource creation and response validation
- **PUT** requests: resource updates
- **DELETE** requests: resource deletion
- **Negative cases**: verifying correct error responses (e.g. 404 for nonexistent resources)

## Tools & Techniques

- **pytest** — test framework, using fixtures for setup/teardown and parametrization for data-driven tests
- **requests** — HTTP client for API calls
- **GitHub Actions** — continuous integration, running the full suite on every push

## Running the Tests

```bash
# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the suite
pytest -v
```

## Continuous Integration

A GitHub Actions workflow (`.github/workflows/tests.yml`) automatically runs the test suite on every push, installing dependencies in a clean environment and reporting results.