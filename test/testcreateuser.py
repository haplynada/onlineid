'''
Created on 12. okt. 2017

@author: Tor Larssen Sekse
'''
from userhandling.newuser import create_user

try: 
    create_user("£", "password", "firstname", "lastname", "phone", "postcode", "country", "countrycode", "adress", "birthday")
except SyntaxError:
    print("yay")