# Expenses Management CLI Application

## Phase 3 Project

This application is a simple Command Line Interface (CLI) tool designed for user registration, login, and potentially managing expenses. It uses SQLite as its backend database and implements bcrypt for secure password hashing.

`````
Expenses-Management-CLI-Application/
│
├── lib/
│ └── db/
│ ├── migration/
│ ├── alembic.ini
│ ├── expenses.db
│ ├── main.py
│ ├── models.py
│ └── utilities.py
│
├── Pipfile
├── Pipfile.lock
└── README.md
`````

***

## Table of Contents

* Features
* Prerequisites
* Setup and Installation
* Usage
* Security Measures
* Future Enhancements
* Contribution
* Resources 

## Features 

1. User Registration: Users can register with a unique username and password.
2. User Login: Registered users can login with their credentials.
3. Menu Driven: Easy to navigate through various functionalities using a menu.

## Prerequisites

* install: Python 3.8
* install: SQLAlchemy: $ pipenv install sqlalchemy alembic
* install: bcrypt library: $ pip install bcrypt

## Setup and Installation

1. Ensure Python 3.8 is installed. You can verify using:
   * run: python --version
2. Clone the repository:
    *Fork repository
    * run: git clone [SSH repository_link]
3. Navigate to the project directory and install the required packages:
    * cd [project_directory]
    * pip install -r requirements.txt
4. run pipenv install
5. get to your virtual: 
    * run pipenv shell 
6. Run the application:
    *$ python lib/db/main.py

***

## Usage

### Website
https://youtu.be/pf-2rqUJH0I

* Upon launching the application, the user is presented with the main menu with the following options:
* You have to enter 1, 2, 3

1. Register
2. Login
3. Exit

* Register: Users can choose a unique username and password to register.

* Login: Registered users can login using their username and password.

* Exit: Close the application.

* After registration or login to your account, the user is presented with the user menu:
* You have to enter 1, 2, 3, 4, 5, 6, 7

1. Add Expense 
2. List Expenses 
3. Expenses Today 
4. Expenses This Week 
5. Expenses This Month 
6. Expenses This Year 
7. Return to Main Menu   


* 1 Add Expense: You can type any kind of expense with the smount and date

* 2 List Expenses: List all the expenses that you have enter 

* 3 to 6. : show all the expenses for today, week, month, and year. 

* 7 Takes you back to Main Menu 

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

## Resources

Alembic documentation » Operation Reference
https://alembic.sqlalchemy.org/en/latest/ops.html

The Python SQL Toolkit and Object Relational Mapper
https://www.sqlalchemy.org/

stack overflow 
https://stackoverflow.com/questions

Flatiron School classes documentation 
https://flatironschool.com

w3 Schools
https://www.w3schools.com

*** 

## License 
MIT License






  
