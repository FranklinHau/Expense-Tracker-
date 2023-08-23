from models import session, User, Expense 
from utilities import hash_password, check_password

# Menu options as a list of dicts 
# each dict has an 'id', 'label', and a 'function
# id = user input, label = description of the option, function = execute for the option
MENU_OPTIONS = [
    {'id': '1', 'label': 'Register', 'function': None},
    {'id': '2', 'label': 'Login', 'function': None},
    {'id': '3', 'label': 'Exit', 'function': exit}
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

# Function to handle user login 
def login():
    # gather user input for username and password  
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    # check if entered username exists in the database
    user = session.query(User).filter_by(username=username).first()
    # if user exists and entered password matches stored hashed password, login is successful
    if user and check_password(password, user.password):
        print('Logged in!')
    else:
        # if credentials don't match, inform the user 
        print('Invalid credentials.')

# Link functions to their respective options in MENU_OPTIONS
for option in MENU_OPTIONS:
    if option['label'] == 'Register':
        option['function'] = register 
    elif option['label'] == 'Login':
        option['function'] = login


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
