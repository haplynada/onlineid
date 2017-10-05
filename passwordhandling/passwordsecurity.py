'''
Created on 18. sep. 2017

@author: Torls
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





'''

passwordsalt = "ec27bbacaa484ce1b961dea1e956251e"
password =input("Enter password:")
hashedpassword = hashlib.sha256(password.encode() + passwordsalt.encode()).hexdigest()
print(hashedpassword)

if hashedpassword =="a6f8bedb7dd926e375135de5b4c3e51870fccdb3b5de7346a10c6605b71d0264":
    print("yay")
else:
    print("fail")
    
'''