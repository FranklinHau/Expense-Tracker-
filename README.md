# Expenses Management CLI Application

## Phase 3 Project

This application is a simple Command Line Interface (CLI) tool designed for user registration, login, and potentially managing expenses. It uses SQLite as its backend database and implements bcrypt for secure password hashing.

***

## Table of Contents

* Features
* Prerequisites
* Setup and Installation
* Usage
* Security Measures
* Future Enhancements
* Contribution

## Features 

1. User Registration: Users can register with a unique username and password.
2. User Login: Registered users can login with their credentials.
3. Menu Driven: Easy to navigate through various functionalities using a menu.

## Prerequisites

* install: Python 3.8
* install: SQLAlchemy: $ pipenv install sqlalchemy alembic
* install: bcrypt library: $ pip install bcrypt

## Setup and Installation

1. Ensure Python 3. is installed. You can verify using:
   run: python --version
2. Clone the repository:
    Fork repository
    run: git clone [SSH repository_link]
3. Navigate to the project directory and install the required packages:
    cd [project_directory]
    pip install -r requirements.txt
4. run pipenv install
5. get to your virtual: run pipenv shell 
5. Run the application:
    python main.py

***

## Usage

* Upon launching the application, the user is presented with the main menu with the following options:

1. Register
2. Login
3. Exit

* Register: Users can choose a unique username and password to register.

* Login: Registered users can login using their username and password.

* Exit: Close the application.

***

## Security Measures

*Password Hashing: User passwords are hashed using bcrypt before storing in the database. This ensures that even if the database is compromised, the actual passwords remain secure.

*Unique Usernames: The application ensures that each username is unique.

***

## Future Enhancements
* Password visibility: Implementing a mechanism to hide passwords during input for improved security.

***

## Contribution
Contributions are welcome! Please fork the repository and open a pull request with your changes, or open an issue for feedback and suggestions.


  
