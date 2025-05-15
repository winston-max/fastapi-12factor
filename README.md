FastAPI 12-Factor Demo
This is a minimal FastAPI-based microservice project that follows the 12-Factor App methodology. The app demonstrates core principles like environment-based configuration, portability, and stateless processes.

Features
Health Check Endpoint: /health/check – A simple endpoint to check if the app is running.

Square Calculator Endpoint: /health/square/{number} – An endpoint to compute the square of a given number.

Environment Variable Configuration: Uses Pydantic to load settings from environment variables.

Pre-commit Hooks: Ensures that your code is always formatted according to style guidelines before committing.

Unit Tests: Uses Pytest for testing the app’s functionality.

Modular Project Structure: Organized to keep things scalable and clean.
