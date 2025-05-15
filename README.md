# FastAPI 12-Factor Demo Project

This demo project showcases how to build a simple microservice using FastAPI while adhering to the **12-Factor App** principles. The app includes a health check endpoint and a utility to calculate the square of a number.

## Key Features
- **Health Check Endpoint:** A simple `/health/check` to monitor the health of the service.
- **Square Calculator Endpoint:** Calculate the square of a given number via `/health/square/{number}`.
- **Configuration with Pydantic:** Environment variables are loaded using Pydantic to ensure clear and secure configurations.
- **Pre-commit Hooks:** Automatically formats code and checks for quality before committing.
- **Unit Tests:** Tests using Pytest ensure basic functionality is covered.

## Prerequisites

Make sure you have the following installed:
- Python 3.11+
- Git

## Setup Instructions

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/fastapi-12factor.git
    cd fastapi-12factor
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows: .\venv\Scripts\activate
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**

    Create a `.env` file in the project root with the following:

    ```env
    APP_NAME=FastAPI 12-Factor Demo
    APP_ENV=development
    API_PORT=8000
    ```

## Running the Application

1. **Start the FastAPI server:**

    ```bash
    uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
    ```

2. **Access the app:**
    - Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
    - Health Check: [http://localhost:8000/health/check](http://localhost:8000/health/check)
    - Square Calculator: [http://localhost:8000/health/square/5](http://localhost:8000/health/square/5)

## Running Tests

To run the test suite, use:

```bash
pytest
