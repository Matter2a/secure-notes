# Secure Notes Security Lab

A security-focused notes API built with Python and FastAPI.

## Features

* REST API built with FastAPI
* Health check endpoint
* Interactive API documentation
* Automated testing (planned)
* PostgreSQL integration (planned)
* Authentication and authorization (planned)

## Tech Stack

* Python
* FastAPI
* SQLAlchemy
* PostgreSQL (planned)
* Pytest

## Getting Started

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
cd secure-notes
```

### 2. Create a virtual environment

```powershell
py -m venv .venv
```

### 3. Install dependencies

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

### 4. Run the application

```powershell
.\.venv\Scripts\python.exe -m uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000/docs to explore the API.

## Security

This project is intended for educational purposes. Do not use real passwords, tokens, or sensitive user data in development or testing.

## Status

Under active development.
