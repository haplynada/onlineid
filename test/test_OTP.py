'''
Created on 11. jan. 2018

@author: Tor Larssen Sekse
'''

import pyotp

def setup_otp():
    secret = pyotp.random_base32()
    
    return secret
    
def check_otp(secret, onetimecode):
    active = pyotp.TOTP(secret)
    if active.verify(onetimecode) == True: 
        return True
    else: 
        return False
    

    
    
secret = setup_otp()
print(secret)

token = input("Enter OTP: ")

print(check_otp(secret, token))