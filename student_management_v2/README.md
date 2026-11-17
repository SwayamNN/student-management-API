# Student Management API V2

A RESTful Student Management API built using **FastAPI, SQLAlchemy, and PostgreSQL**.

## Overview

This project provides an API to manage student records and course enrollments. It demonstrates backend development concepts including CRUD operations, database relationships, validation, and pagination.

## Technologies Used

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic
- Uvicorn
- Git and GitHub

## Features

- Create, read, update, and delete students
- Search students by name
- Filter students by marks and age
- Sort students by marks
- Pagination
- Input validation using Pydantic
- PostgreSQL database integration
- SQLAlchemy ORM
- Student–Enrollment relationships
- Retrieve student enrollments
- Automatic timestamps
- Database transaction handling
- Student count endpoint

## Project Structure

```text
student_management_v2/
├── main.py
├── database.py
├── models.py
├── schemas.py
├── crud.py
├── create_tables.py
├── test_connection.py
├── test_relationship.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/SwayamNN/student-management-API.git
cd student-management-API/student_management_v2
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv env
source env/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file:

```env
DB_HOST=localhost
DB_NAME=college
DB_USER=postgres
DB_PASSWORD=your_password
DB_PORT=5432
```

Replace the database credentials with your own PostgreSQL configuration.

### 5. Create database tables

```bash
python create_tables.py
```

### 6. Start the API

```bash
fastapi dev main.py
```

## API Documentation

Once the server is running, visit:

- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Learning Outcomes

Through this project, I practised:

- Building REST APIs with FastAPI
- Working with PostgreSQL
- SQLAlchemy ORM and database relationships
- Pydantic validation
- CRUD architecture
- Database transactions and error handling
- API testing using Swagger UI

## Author

**Swayam**

GitHub: [https://github.com/SwayamNN](https://github.com/SwayamNN)
