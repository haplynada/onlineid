'''
Created on 6. nov. 2017

@author: Tor Larssen Sekse
'''
from user_handling.input_control import check_email, check_email_database

email = "sau@sau.no"

print(check_email_database(email))