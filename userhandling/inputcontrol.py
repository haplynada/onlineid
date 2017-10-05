'''
Created on 5. okt. 2017

@author: Tor Larssen Sekse
'''
validchars = set('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.-_ @')
def check_password(password):
    password_length = len(password)
    if password_length >= 8  and (any(char.isdigit() for char in password)) and password_length <=15: 
        return True
    else :
        return "invalid password"

def check_email(email):
    if set(email).issubset(validchars):
        if "@" and "." in email: 
            return True
    else:
        return "invalid email"
    
    
def check_phonenumber(phone):
    phone = phone.replace(" ", "")
    phone_length = len(phone)
    if phone_length == 8 and (phone.isdigit()):
       
        return True
    else:
        return "invalid phone number"
    
    
RUINED