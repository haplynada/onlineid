'''
Created on 12. jan. 2018

@author: Bjarke Larsen, Tor Larssen Sekse
'''

import pyotp
from database_handling.connect import *


def setup_otp(self, user_id: str):
    secret = pyotp.random_base32()

    with Connect() as db:  # connecting to database
        try:
            query = "UPDATE authentication SET has_2fa='True', 2fa_secret =%s WHERE user_id =%s;" \

            db.cur.execute(query, secret, self.__user_id)
        except:
            pass
    print(secret)
    return secret



def check_otp(self, secret: str, onetimecode: str):
    active = pyotp.TOTP(secret)
    if active.verify(onetimecode) == True:
        return True
    else:
        return False

