from models import session, User, Expense 
from utilities import hash_password, check_password

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
            
            if existing_user:
                print('Username already taken. Please choose another one.')
                continue
        elif choice == '2': # Login code 
            pass 
        elif choice == '3':
            exit()

if __name__ == '__main__':
    main()
