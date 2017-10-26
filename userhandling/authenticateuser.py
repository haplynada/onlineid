'''
Created on 5. okt. 2017
this is a stupid comment
@author: Tor Larssen Sekse
'''
from passwordhandling.passwordsecurity import authenticate_password
from userhandling.getuserdata import get_hashed_Password, get_salt
from Databasehandling.queries import getuser

def authenticate_user(email, password):
    user = getuser(email)
    hashedpassword = get_hashed_Password(user)
    passwordsalt = get_salt(user)
    checker = authenticate_password(hashedpassword, passwordsalt, password)
    return checker