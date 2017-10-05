'''
Created on 5. okt. 2017

@author: Tor Larssen Sekse
'''

from passwordhandling.passwordsecurity import generate_salt, hash_password

def store_password(user, password):
    password_stored = False
    salt = generate_salt()
    hashedpassword =hash_password(salt, password)
    '''
    this part stores the hashedpassword and the salt in the database
    '''
    password_stored = True
    
    return password_stored
HELLO