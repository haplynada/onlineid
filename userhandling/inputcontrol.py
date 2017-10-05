'''
Created on 5. okt. 2017

@author: Tor Larssen Sekse
'''
validchars_email = set('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.-_ @')
validchars_name = set('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')

def check_password(password):
    password_length = len(password)
    if password_length >= 8  and (any(char.isdigit() for char in password)) and password_length <=15: 
        return True
    else:
        return "invalid password"

def check_email(email):
    if set(email).issubset(validchars_email):
        if "@" and "." in email: 
            return True
    else:
        return "invalid email"
    
def check_firstname(name):
    if set(name).issubset(validchars_name):
        return True
    else:
        return "invalid first name"
    
def check_lastname(name):
    if set(name).issubset(validchars_name):
        return True
    else:
        return "invalid last name"
    
    
def check_phonenumber(phone):
    phone = phone.replace(" ", "")
    phone_length = len(phone)
    if phone_length == 8 and (phone.isdigit()):  
        return True
        return "invalid phone number"
    
def check_adress(adress):
    if set(adress).issubset(validchars_name):
        return True
    else:
        return "invalid adress"
    
def check_postcode(postcode):
    postcode_length = len(postcode)
    if postcode_length == 4 and postcode.isdigit():
        return True
    else:
        return "invalid postcode"
    
    