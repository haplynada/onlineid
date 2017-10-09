'''
Created on 18. sep. 2017

@author: Tor Larssen Sekse
'''

import hashlib
import uuid

def generate_salt():
    salt = uuid.uuid4().hex
    return salt

def authenticate_password(hashedpassword, salt, password):
    checker = False
    testpassword =hashlib.sha256(password.encode() + salt.encode()).hexdigest()
    if testpassword == hashedpassword:
        checker = True
    else:
        checker = False
    return checker

def hash_password(salt, password):
    hashedpassword = hashlib.sha256(password.encode() + salt.encode()).hexdigest()
    return hashedpassword
