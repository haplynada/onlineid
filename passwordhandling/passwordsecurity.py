'''
Created on 18. sep. 2017

@author: Tor Larssen Sekse
'''

import hashlib
import uuid

def generate_salt():
    salt = uuid.uuid4().hex
    print(salt)
    return salt

def check_password(hashedpassword, salt, password):
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

def get_hashedpassword(user):
    hashedpassword = 
    '''
    this part needs to call on the database using the userid and get the hashedpassword
    '''
    return hashedpassword

def get_salt(user):
    salt =
        '''
    this part needs to call on the database using the userid and get the salt
    '''
    return salt

