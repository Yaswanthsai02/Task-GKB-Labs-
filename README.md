# User Data Management Web Application

This is a basic web application built with Python and Flask that allows users to input their data, validate it, store it in a SQLite database, retrieve it, and display it in a table format.

## Objective

The objective of this project is to create a simple web application that demonstrates CRUD (Create, Read, Update, Delete) operations using Flask and SQLite.

## Features

- User input form for collecting name, email, age, and date of birth.
- Client-side validation to ensure the email format is valid and age is a positive integer.
- Storage of validated user data in a SQLite database.
- Retrieval of stored data from the database and display in a tabular format.

## Requirements

1. Choose a Programming Language: Python
2. User Input Form:
    - Name (text input)
    - Email (email input)
    - Age (number input)
    - Date of Birth (date input)
    - Client-side validation for email format and age as a positive integer
3. Database:
    - SQLite database to store user data
    - Table with fields: ID (auto-increment), Name, Email, Age, Date of Birth
4. Data Storage:
    - Store validated user data in the database
5. Data Retrieval:
    - Retrieve data from the database and display it in a tabular format
6. Git Repository:
    - Create a Git repository for the project
    - Commit code including all necessary files and database schema
7. Documentation:
    - Include a README.md file explaining setup and usage of the application

## Setup

1. Clone the repository to your local machine:

    ```bash
    git clone <repository_url>
    ```

2. Install Flask if not already installed:

    ```bash
    pip install flask
    ```

## Usage

1. Run the Flask application:

    ```bash
    python app.py
    ```

2. Access the application in your web browser at `http://127.0.0.1:5000/`.

3. Fill in the user input form with valid data and click "Submit".

4. View the stored data by visiting `http://127.0.0.1:5000/data`.

## Technologies Used

- Python
- Flask
- SQLite
- HTML/CSS


