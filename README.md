# Library Management System

## Introduction

A web-based Library Management System that allows users to perform CRUD operations on books. The system includes a frontend built with HTML, CSS, and JavaScript, and a backend API built with Flask in Python.

## Features

- Add new books
- Search books by author, published year, and genre
- List all books
- Update book details
- Delete books
- Interactive user interface

## Technologies Used

- Frontend: HTML, CSS, JavaScript
- Backend: Python (Flask)
- API Documentation: Swagger

## Installation

### Prerequisites

- Python 3.6+
- Git

### Backend Setup

1. **Clone the repository:**

    ```bash
    git clone 
    cd 
    ```

2. **Create a virtual environment and activate it:**

    ```bash
    python -m venv venv
    venv\Scripts\activate  
    ```

3. **Install dependencies:**

    ```bash
    pip install flask-swagger-ui
    ```

### Running the Application

1. **Start the Flask server:**

    ```bash
    python app.py
    ```

2. **Access the application:**

    Open your browser and navigate to `http://127.0.0.1:5000` to access the Library Management System.

### API Documentation

Access the Swagger UI at `http://127.0.0.1:5000/docs` for detailed API documentation.

## Project Structure

- `library.py`: Flask backend application.
- `swagger.json`: Swagger configuration for API documentation.
- `DOCKERFILE`: To build the docker image
- `README.md`: The file you're currently reading

## Usage

- **Add Book:** Fill in the form and submit to add a new book.
- **Search Book:** Use the search form to filter books by author, year, or genre.
- **Update/Delete Book:** Use the corresponding buttons in the books table to update or delete a book.