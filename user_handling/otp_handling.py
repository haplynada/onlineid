'''
Created on 12. jan. 2018

@author: Bjarke Larsen, Tor Larssen Sekse
'''

import pyotp
from database_handling.connect import *


def setup_otp(db_email: str):
    secret = pyotp.random_base32()

    with Connect() as db:  # connecting to database
        try:
            query = "UPDATE information SET has_2fa='True' WHERE email =%s;"
            db.cur.execute(query, db_email)
        except:
            pass
    print(secret)
    return secret



def check_otp(secret, onetimecode):
    active = pyotp.TOTP(secret)
    if active.verify(onetimecode) == True:
        return True
    else:
        return False

