from models import session, User, Expense 
from utilities import hash_password, check_password

# Menu options as a list of dicts 
MENU_OPTIONS = [
    {'id': '1', 'label': 'Register', 'function': None},
    {'id': '2', 'label': 'Login', 'function': None},
    {'id': '3', 'label': 'Exit', 'function': exit}
]



#starts CLI interface
def main():
    while True:# it will keep presenting the user with the options unless they choose exit
        #printing choices for the user
        print('1. Register')# the user will be able to see these options 
        print('2. Login')   # user will be able to choose what they want to do
        print('3. Exit')
        choice = input('Enter your choice: ')# user will type in number corresponding to their
                                            # choice and hit enter 
        
        if choice == '1': # Registration code 
            username = input('Enter a username: ')
            password = input('Enter a password: ')
            
            #If a user with that username exists, it will prompt the user to choose another one.
            existing_user = session.query(User).filter_by(username=username).first()
            if existing_user:
                print('Username already taken. Please choose another one.')
                continue
            # Instead of storing the raw password, it is hash with the hash_password function. 
            hashed_password = hash_password(password)
            user = User(username=username, password=hashed_password)
            # After hashing the password and creating the new User object, I added this object to the session
            session.add(user)
            session.commit()# writes this change to the actual database
            print('User registered!')

        elif choice == '2': # Login code 
            # prompts user to enter username and password 
            # values are stored in username and password variables  
            username = input('Enter your username: ')
            password = input('Enter your password: ') 

            # checks of there's a user with the provided username in the database 
            # session.query(User) tells SQLAlchemy to prepare a query targeting the User model/table.
            # .filter_by(username=username) filters the results to only those rows where the username matches the provided input.
            #.first() fetches the first result, if there's any. If there's no matching user, it will return None.
            user = session.query(User).filter_by(username=username).first()

            #checks if the user and password was found
            if user and check_password(password, user.password):
                print('Logged in!')
            else:
                print('Invalid credentials.')
                
        elif choice == '3':
            exit()

if __name__ == '__main__':
    main()
