'''
Created on 12. okt. 2017

@author: Tor Larssen Sekse
'''
from userhandling.newuser import create_user

try: 
    print(create_user("Hans@hansen.dk", "K234Jdfhen", "Peter", "Larsen", "12345678", "1234", "denmark", "0045", "hansveien", "19", "1988-12-12", "female"))
except SyntaxError:
    print("yay")