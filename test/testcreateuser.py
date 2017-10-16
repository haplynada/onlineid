'''
Created on 12. okt. 2017

@author: Tor Larssen Sekse
'''
from userhandling.newuser import create_user

try: 
    print(create_user("bjarke@bjarke.com", "bjarke", "bjarke", "bjarke", "98765432", "9900", "norway", "47", "bjarkesvei", "9", "1985-12-12", "male"))
except SyntaxError:
    print("yay")