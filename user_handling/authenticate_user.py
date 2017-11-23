'''
Created on 5. okt. 2017
authenticate user contains all functions involved in authenticating the user on the server
and the functions involved with handling passwords
@author: Tor Larssen Sekse
'''
#imports functions to get needed data and bcrypt for the password handling
from user_handling.get_user_data import get_hashed_Password
from database_handling.queries import get_user
import bcrypt

#authenticate_user takes in an email adress and a password, then gets the userid and hashedpassword
# from the database, and authenticates the user. 
def authenticate_user(email, password):
    #gathers data from the database
    user = get_user(email)
    hashed_password = get_hashed_Password(user)
    #authenticates the password against the hashed one stored in the database
    checker = authenticate_password(hashed_password, password)
    #returns True/False depending on if the user was authenticated or not
    return checker

#Generates a random salt for use in hashing the password
def generate_salt():
    salt = bcrypt.gensalt()
    return salt

#takes in hashed_password and password and runs bcrypt.checkpw function to determine if they
#match. returns True/False
def authenticate_password(hashed_password, password):
    checker = False
    if bcrypt.checkpw(password.encode(), hashed_password.encode()):
        checker = True
    else:
        checker = False
    return checker

#Takes in a salt and password and run bcrypt.hashpw and returns the hashed password
def hash_password(salt, password):
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password
