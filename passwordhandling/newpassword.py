'''
Created on 5. okt. 2017

@author: Tor Larssen Sekse
'''

from passwordhandling.passwordsecurity import generate_salt, hash_password
from userhandling.authenticateuser import authenticate_user

def new_password(user, oldpassword, newpassword):
    password_stored = False
    
    if authenticate_user(user, oldpassword) == True: 
        newpasswordsalt = generate_salt()
        newhashedpassword =hash_password(passwordsalt, newpassword)
        #store newhashedpassword in the database
    else:
        password_stored = False
    
    return password_stored