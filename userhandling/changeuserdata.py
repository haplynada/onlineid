'''
Created on 12. okt. 2017

@author: Tor Larssen Sekse
'''
from userhandling.inputcontrol import *
from userhandling.authenticateuser import authenticate_user

def change_email(user, password, email):
    checker = False
    if check_email(email) == True:
        authenticate_user(user, password)
        #store new email in the database
        checker = True
        return checker
    else:
        return checker

def change_firstname():
    
def change_lastname():
    
def change_phonenumber():
    
def change_adress():
    
def change_postcode():
    
def change_country():
    
def change_countrycode():
    
def change_birthday():
    