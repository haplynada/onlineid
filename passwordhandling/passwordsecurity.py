'''
Created on 18. sep. 2017

@author: Tor Larssen Sekse
'''

import bcrypt


def generate_salt():
    salt = bcrypt.gensalt()
    return salt

def authenticate_password(hashedpassword, password):
    checker = False
    if bcrypt.checkpw(password.encode(), hashedpassword):
        checker = True
    else:
        checker = False
    return checker

def hash_password(salt, password):
    hashedpassword = bcrypt.hashpw(password.encode(), salt)
    return hashedpassword
