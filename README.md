# InkWell ✒️

InkWell is a simple, clean, and modern blog application built with Python and the Flask web framework. It provides a platform for users to register, create, and manage their own blog posts. This project was built to demonstrate a complete, production-ready Flask application structure, including blueprints, extensions, and database migrations.

***

## Features

- **User Authentication**: Secure user registration, login, and logout functionality.
- **Session Management**: Keeps users logged in across sessions.
- **Post Management (CRUD)**: Logged-in users can Create, Read, Update, and Delete their own blog posts.
- **Clean UI**: A minimal and responsive design.
- **Database Migrations**: Uses Flask-Migrate to handle changes to the database schema.

***

## Technologies Used

- **Backend**: Python, Flask
- **Database**: Flask-SQLAlchemy (with SQLite for development)
- **Database Migrations**: Flask-Migrate
- **Authentication**: Flask-Login
- **Forms**: Flask-WTF
- **Environment Variables**: python-dotenv

***

## Setup and Installation

Follow these steps to get the application running locally on your machine.

### 1. Clone the Repository
```bash
git clone [https://github.com/your-username/InkWell.git](https://github.com/your-username/InkWell.git)
cd InkWell