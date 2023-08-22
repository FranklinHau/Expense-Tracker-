#store passwords and later verify if an input password matches the stored hashed version.
import bcrypt


def hash_password(password):#function to create a hashed version of the provided password.
    salt = bcrypt.gensalt()# generates a new random salt. passwords will be different due to the unique salts
    #This hashes the encoded password using the generated salt
    return bcrypt.hashpw(password.encode('utf-8'), salt)#Bcrypt expects the password in this format.

#function to verify if the provided password matches the stored hashed password.
def check_password(password, hashed):
    #encoded the password into a byte-string format, just like in the hash_password function.
    return bcrypt.checkpw(password.encode('utf-8'), hashed)
    #If they match, it returns True, indicating that the password is correct; otherwise, it returns False.