'''
Created on 5. okt. 2017
this is a stupid comment
@author: Tor Larssen Sekse
'''
from passwordhandling.passwordsecurity import authenticate_password
from userhandling.getuserdata import get_hashedpassword, get_salt
from userhandling.authenticateusername import authenticate_username

def authenticate_user(user, password):
    checker = False
    if authenticate_username(user) == True:
        hashedpassword = get_hashedpassword(user)
        passwordsalt = get_salt(user)
        checker = authenticate_password(hashedpassword, passwordsalt, password)
        return checker
    else :
        return checker
