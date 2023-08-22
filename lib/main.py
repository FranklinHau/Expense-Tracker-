from models import session, User, Expense 
from utilities import hash_password, check_password

def main():
    while True:
        print('1. Register')
        print('2. Login')
        print('3. Exit')
        choice = input('Enter your choice: ')

        