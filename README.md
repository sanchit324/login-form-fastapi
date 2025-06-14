# FastAPI User Authentication

A secure user authentication system built with FastAPI, SQLAlchemy, and JWT tokens.

## Features

- User registration with email and password
- User login with JWT token generation
- Password hashing using bcrypt
- Protected routes with JWT token authentication
- PostgreSQL database with SQLAlchemy ORM
- Database migrations with Alembic

## Prerequisites

- Python 3.8+
- PostgreSQL database
- pip (Python package manager)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd fastapi-login
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory with the following variables:
   ```env
   DATABASE_URL=postgresql://username:password@localhost:5432/your_database
   SECRET_KEY=your-secret-key-here
   ALGORITHM=HS256
   TOKEN_EXPIRATION_TIME=60
   ```

5. Run database migrations:
   ```bash
   alembic upgrade head
   ```

## Running the Application

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`

## API Endpoints

### User Registration
- **URL**: `/users/`
- **Method**: `POST`
- **Body**:
  ```json
  {
    "name": "John Doe",
    "email": "john@example.com",
    "password": "securepassword123"
  }
  ```

### User Login
- **URL**: `/auth/login`
- **Method**: `POST`
- **Headers**:
  - `Content-Type: application/x-www-form-urlencoded`
- **Body**:
  - `username`: User's email
  - `password`: User's password

### Get Current User
- **URL**: `/users/me`
- **Method**: `GET`
- **Headers**:
  - `Authorization: Bearer <your_jwt_token>`

## Project Structure

```
fastapi-login/
├── alembic/              # Database migration files
├── app/
│   ├── __init__.py
│   ├── main.py           # FastAPI application
│   ├── config.py         # Application configuration
│   ├── database.py       # Database connection
│   ├── models.py         # SQLAlchemy models
│   ├── oauth2.py         # Authentication utilities
│   ├── routes/           # API routes
│   │   ├── __init__.py
│   │   ├── auth.py       # Authentication routes
│   │   └── user.py       # User routes
│   ├── schema.py         # Pydantic models
│   └── utils.py          # Utility functions
├── .env                  # Environment variables
├── .gitignore
├── alembic.ini           # Alembic configuration
├── requirements.txt      # Project dependencies
└── README.md            # This file
```

## Testing with Postman

1. **Register a new user**:
   - Method: `POST`
   - URL: `http://127.0.0.1:8000/users/`
   - Headers: `Content-Type: application/json`
   - Body (raw JSON):
     ```json
     {
       "name": "Test User",
       "email": "test@example.com",
       "password": "test123"
     }
     ```

2. **Login to get token**:
   - Method: `POST`
   - URL: `http://127.0.0.1:8000/auth/login`
   - Headers: `Content-Type: application/x-www-form-urlencoded`
   - Body (form-data):
     - `username`: test@example.com
     - `password`: test123

3. **Access protected route**:
   - Method: `GET`
   - URL: `http://127.0.0.1:8000/users/me`
   - Headers:
     - `Authorization: Bearer <your_jwt_token>`

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
