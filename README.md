# Flask API Study Project

## About This Repository

This repository is basically a study project focused on learning how to build a simple REST API using Flask and Python. The goal is to understand the core concepts of Flask framework, REST API design patterns, and best practices for building web APIs.

## Overview

This is a study environment for learning how to build REST APIs with Python and Flask.

## Setup Instructions

### 1. Create Virtual Environment

```powershell
python -m venv venv
```

### 2. Activate Virtual Environment

```powershell
# On Windows PowerShell
.\venv\Scripts\Activate.ps1

# If you get execution policy error, run:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### 3. Install Dependencies

```powershell
pip install -r requirements.txt
```

### 4. Create Environment File

Create a `.env` file in the root directory:

```
FLASK_APP=app.py
FLASK_ENV=development
FLASK_DEBUG=True
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///app.db
```

## Project Structure Suggestions

```
api-py-flask-study/
│
├── app.py                 # Main application entry point
├── config.py              # Configuration settings
├── requirements.txt       # Project dependencies
├── .env                   # Environment variables (not in git)
├── .gitignore            # Git ignore rules
│
├── models/               # Database models
│   └── __init__.py
│
├── routes/               # API routes/endpoints
│   └── __init__.py
│
├── services/             # Business logic
│   └── __init__.py
│
├── schemas/              # Request/response schemas
│   └── __init__.py
│
└── tests/                # Unit and integration tests
    └── __init__.py
```

## Basic Flask Concepts to Study

### 1. Simple Flask App Structure

- Creating Flask application instance
- Defining routes with `@app.route()`
- Handling HTTP methods (GET, POST, PUT, DELETE)
- Returning JSON responses

### 2. REST API Principles

- Resource-based URLs
- HTTP status codes
- Request/Response format
- CRUD operations

### 3. Database Integration

- SQLAlchemy models
- Database migrations
- CRUD operations
- Relationships

### 4. Request Validation

- Input validation with Marshmallow
- Error handling
- Custom validators

### 5. Testing

- Unit tests with pytest
- Integration tests
- Test fixtures

## Running the Application

```powershell
# Make sure virtual environment is activated
flask run

# Or specify host and port
flask run --host=0.0.0.0 --port=5000
```

## Testing

```powershell
# Run all tests
pytest

# Run with coverage
pytest --cov=.

# Run specific test file
pytest tests/test_example.py
```

## Useful Flask Commands

```powershell
# Check Flask version
flask --version

# List all routes
flask routes

# Open Python shell with app context
flask shell
```

## Common HTTP Status Codes

- `200 OK` - Request succeeded
- `201 Created` - Resource created successfully
- `204 No Content` - Request succeeded, no content to return
- `400 Bad Request` - Invalid request data
- `404 Not Found` - Resource not found
- `500 Internal Server Error` - Server error

## Resources for Learning

- [Flask Official Documentation](https://flask.palletsprojects.com/)
- [Flask-SQLAlchemy Documentation](https://flask-sqlalchemy.palletsprojects.com/)
- [REST API Design Best Practices](https://restfulapi.net/)
- [HTTP Status Codes](https://httpstatuses.com/)

## Next Steps

1. Create your main `app.py` file
2. Set up basic routes
3. Test with tools like Postman or curl
4. Add database models
5. Implement CRUD operations
6. Write tests

Happy learning! 🚀
