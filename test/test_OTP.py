'''
Created on 11. jan. 2018

@author: Tor Larssen Sekse, Bjarke Larsen
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


def menu():
    secret = ""
    run = True
    while run == True:
        user = input("Enter 1 for setup OTP\n"
                     "Enter 2 for check OTP\n"
                     "Enter Q for Quit: ")
        if user == "Q" or user == "q":
            break
        elif user == "1":
            secret = setup_otp()
            print(secret)
        elif user == "2":
            token = input("Enter OTP: ")
            print(check_otp(secret, token))

    

if __name__ == "__main__":
    menu()
