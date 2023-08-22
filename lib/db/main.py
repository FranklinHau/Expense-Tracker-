from models import session, User, Expense 
from utilities import hash_password, check_password

# Menu options as a list of dicts 
MENU_OPTIONS = [
    {'id': '1', 'label': 'Register', 'function': None},
    {'id': '2', 'label': 'Login', 'function': None},
    {'id': '3', 'label': 'Exit', 'function': exit}
]

# Register function 
def register():
    username = input('Enter a username: ')
    password = input('Enter a password: ')
    existing_user = session.query(User).filter_by(username=username).first()
    if existing_user:
        print('Username already taken. PLease choose another one. ')
        return 
    hashed_password = hash_password(password)
    user = User(username=username, password=hashed_password)
    session.add(user)
    session.commit()

# Login function 
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    user = session.query(User).filter_by(username=username).first()
    if user and check_password(password, user.password):
        print('Logged in!')
    else:
        print('Invalid credentials.')

# Link functions to the menu options 
for option in MENU_OPTIONS:
    if option['label'] == 'Register':
        option['function'] = register 
    elif option['label'] == 'Login':
        option['function'] = login


# starts CLI interface
def main():
    while True:
        for option in MENU_OPTIONS:
        
        
       
            
if __name__ == '__main__':
    main()
