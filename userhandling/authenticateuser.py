'''
Created on 5. okt. 2017

@author: Tor Larssen Sekse
'''
from userhandling.checkusername import check_username
from passwordhandling.passwordsecurity import get_hashedpassword, get_salt,\
    check_password

def authenticate_user(user, password):
    checker = False
    if check_username(user) == True:
        hashedpassword = get_hashedpassword(user)
        salt = get_salt(user)
        checker = check_password(hashedpassword, salt, password)
        return checker
    else :
        return checker
