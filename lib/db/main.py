from models import session, User, Expense
from utilities import hash_password, check_password
from datetime import datetime

current_user = None # to be use to keep tract of the logged-in user

# Menu options as a list of dicts 
# each dict has an 'id', 'label', and a 'function
# id = user input, label = description of the option, function = execute for the option
MENU_OPTIONS = [
    {'id': '1', 'label': 'Register', 'function': None},
    {'id': '2', 'label': 'Login', 'function': None},
    {'id': '3', 'label': 'Add Expense', 'function': None},
    {'id': '4', 'label': "Exit", 'function': exit},
    {'id': '5', 'label': "List Expenses", 'function': list_expenses}, 
]

# Function to handle user registration 
def register():
    # gather user input for the username and password
    username = input('Enter a username: ')
    password = input('Enter a password: ')
    # checks if the existing username already exist in the database 
    existing_user = session.query(User).filter_by(username=username).first()

    if existing_user:
        # if the username is already taken, inform the user and exit the function  
        print('Username already taken. PLease choose another one. ')
        return
    # if username is unique, hash the password for security 
    hashed_password = hash_password(password)
    # creating a new User Instance with the given username and hashed password 
    user = User(username=username, password=hashed_password)
    # add the new user to the SQLAlchemy session for DB insertion 
    session.add(user)
    # commit the session to persist the user data into the database 
    session.commit()
    # if registration is successful
    print('Registration successful!')

    add_expense(user.id) # adding user.id here since we just created this user 

# Function to handle user login 
def login():
    # gather user input for username and password  
    username = input('Enter your username: ')
    password = input('Enter your password: ')

    # check if entered username exists in the database
    user = session.query(User).filter_by(username=username).first()

    # if user exists and entered password matches stored hashed password, login is successful
    if user and check_password(password, user.password):
        # setting the currrent user to the user who just logged in 
        global current_user
        current_user = user
        print('Logged in!')
        add_expense(user.id)
    else:
        # if credentials don't match, inform the user 
        print('Invalid credentials.')

        add_expense(user.id) # Adding user.id since the user has just logged in 
    

# Links functions to their respective options in MENU_OPTIONS
for option in MENU_OPTIONS:
    if option['label'] == 'Register':
        option['function'] = register 
    elif option['label'] == 'Login':
        option['function'] = login
    elif option['label'] == 'Add Expense': 
        option['function'] = add_expense_logged_in
    elif option['label'] == 'List Expenses':
        option['function'] = list_expenses

# function that allows a user to add their expenses 
def add_expense(user_id): 
    category = input("Enter the category of the expense (e.g, Food, Rent, Entertainment): ")
    amount = float(input('Enter the amount of the expense: '))
    date_input = input('Enter the date of the expense format YYYY-MM-DD: ')
    date_obj = datetime.strptime(date_input, '%Y-%m-%d').date()
    
    # if user uses a non-numeric amount
    # looping until the user provides a valid amount 
    while True: 
        try: # trying to converting the user input into a float
            amount = float(input('Enter the amount of the expense: '))
            break 
        except ValueError:
            # if conversion fails, it means the input wasn't a valid number
            print('Please enter a valid number for the amount.')

    # Looping until the user provides a date in the correct format 
    while True:
        date_input = input('Enter the date of the expense (format YYYY-MM-DD): ')
        try:
            # trying to convert the user input into a date object
            date_obj = datetime.strptime(date_input, '%Y-%m-%d').date()
            break
        except ValueError:
            # if conversion fails, it means the input wans't a valid date format
            print('Invalid date format. Please use YYYY-MM-DD format.')
     

    # Expense instance 
    expense = Expense(category=category, amount=amount, date=date_obj, user_id=user_id)
    session.add(expense)
    session.commit()
    print('Expense added successfully!')

# functions checks if user is logged in before calling the add_expense function 
def add_expense_logged_in():
    #checking if there's a current user set 
    if current_user:
        add_expense(current_user.id)
    else:
    # if no user is logged in, informs users to login first 
        print('Please login first!')

# this function list all expenses of the currently logged in user 
def list_expenses(): 
    # if no user is logged in, informs the user to login first 
    if not current_user: 
        print('Please login first!')
        return
    
    # Query the database to get all expenses for the current user 
    expenses = session.query(Expense).filter_by(user_id=current_user.id).all()

    # if the user has no expense, inform the user 
    if not expenses:
        print('You have no expenses recorded.')
        return 
    # displays all the expenses 
    print('\nYour expenses:')
    for expense in expenses: 
        print(f"Date: {expense.date}, Category: {expense.category}, Amount: ${expense.amount}")

# function that runs the CLI interface 
def main():
    while True:
        # displaying th e menu options to the user 
        for option in MENU_OPTIONS:
            print(f'{option["id"]}. {option["label"]}')
        # take user's choice as input 
        choice = input('Enter your choice: ')

        # fetch the selected option from MENU_OPTIONS based on user input 
        selected_option = next((opt for opt in MENU_OPTIONS if opt['id'] == choice), None)
        # if invalid option is selected and has an associated function, execute it 
        if selected_option and selected_option['function']:
            selected_option['function']()
        else:
            # inform the user if an invalid option is chosen
            print('Invalid option. Please choose again.')
# ensuring that the main function is called only if this script is run directly and not imported  
if __name__ == '__main__':
    main()
