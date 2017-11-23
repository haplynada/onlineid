'''
Created on 5. okt. 2017
Authenticate
@author: Tor Larssen Sekse
'''

from user_handling.get_user_data import get_hashed_Password
from database_handling.queries import get_user
import bcrypt

def authenticate_user(email, password):
    user = get_user(email)
    hashedpassword = get_hashed_Password(user)
    checker = authenticate_password(hashedpassword, password)
    return checker

def generate_salt():
    salt = bcrypt.gensalt()
    return salt

def authenticate_password(hashed_password, password):
    checker = False
    if bcrypt.checkpw(password.encode(), hashed_password.encode()):
        checker = True
    else:
        checker = False
    return checker

def hash_password(salt, password):
    hashedpassword = bcrypt.hashpw(password.encode(), salt)
    return hashedpassword
