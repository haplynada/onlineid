'''
Created on 12. okt. 2017

@author: Tor Larssen Sekse
'''
from userhandling.newuser import create_user

try: 
    print(create_user("email", "password", "firstname", "lastname", "phone", "postcode", "country", "countrycode", "adress", "adressnumber", "birthday", "male"))
except SyntaxError:
    print("yay")