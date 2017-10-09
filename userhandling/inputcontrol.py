'''
Created on 5. okt. 2017

@author: Tor Larssen Sekse
'''
validchars_email = set('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.-_ @')
validchars_name = set('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ')
countries = ["norway", "sweden", "denmark", "iceland", "united states", "england", "great britain", \
             "germany",]
countrycodes = ["0047", "0046", "0045", "00354", "0111", "0044", "0049"]
def check_password(password):
    password_length = len(password)
    if password_length >= 8  and (any(char.isdigit() for char in password)) and password_length <=15: 
        return True
    else:
        return False

def check_email(email):
    if set(email).issubset(validchars_email):
        if "@" in email: 
            if "." in email:
                return True
            else:
                return False
        else:
            return False
    else:
        return False
    
def check_firstname(name):
    if set(name).issubset(validchars_name):
        return True
    else:
        return False
    
def check_lastname(name):
    if set(name).issubset(validchars_name):
        return True
    else:
        return False
    
def check_phonenumber(phone):
    phone = phone.replace(" ", "")
    phone_length = len(phone)
    if phone_length == 8 and (phone.isdigit()):  
        return True
    else: 
        return False
    
def check_adress(adress):
    if set(adress).issubset(validchars_email):
        return True
    else:
        return False
    
def check_postcode(postcode):
    postcode_length = len(postcode)
    if postcode_length == 4 and postcode.isdigit():
        return True
    else:
        return False

def check_country(country):
    country = country.lower()
    if country in countries:
        return True
    else:
        return False

def check_countrycode(countrycode):
    if countrycode in countrycodes: 
        return True
    else: 
        return False
    