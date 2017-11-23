'''
Created on 12. okt. 2017
The change_xxxx functions changes user data in the database. The user needs to be
authenticated before any of these functions are called, because they don't authenticate
the user before posting their data 
@author: Tor Larssen Sekse
'''
from user_handling.input_control import *
import pymysql
from database_handling.connect import connect


def change_email(user, email):
    checker = False
    if check_email(email) == True:
        cur = connect()
        query = "UPDATE information SET email=%s WHERE user_id=%s"
        cur.execute(query, (email, user))
        # filter and return result  
        db.commit()
        checker = True
        return checker

    else:
        return checker

def change_firstname(user, first_name):
    checker = False
    if check_firstname(first_name) == True:
        cur = connect()
        query = "UPDATE information SET first_name=%s WHERE user_id=%s"
        cur.execute(query, (first_name, user))
        #filter and return result  
        db.commit()
        checker = True
        return checker
    else:
        return checker
    
def change_lastname(user, last_name):
    checker = False
    if check_lastname(last_name) == True:
        cur = connect()
        query = "UPDATE information SET last_name=%s WHERE user_id=%s"
        cur.execute(query, (last_name, user))
        # filter and return result  
        db.commit()
        checker = True
        return checker
    else:
        return checker
    
def change_phonenumber(user, phone_number):
    checker = False
    if check_phonenumber(phone_number) == True:
        cur = connect()
        query = "UPDATE information SET phoneNumber=%s WHERE user_id=%s"
        cur.execute(query, (phone_number, user))
        # filter and return result  
        db.commit()
        checker = True
        return checker
    else:
        return checker
    
def change_adress(user, adress):
    checker = False
    if check_adress(adress) == True:
        cur = connect()
        query = "UPDATE information SET adress=%s WHERE user_id=%s"
        cur.execute(query, (adress, user))
        # filter and return result  
        db.commit()
        checker = True
        return checker
    else:
        return checker
    
def change_postcode(user, postcode):
    checker = False

    cur = connect()
    query = "UPDATE information SET zip_code=%s WHERE user_id=%s"
    cur.execute(query, (postcode, user_id))
    print("Changed postcode of user_id", user_id, "to", postcode)
# filter and return result  
    db.commit()
    
def change_country(user_id, country):
    cur = connect()
    query = "UPDATE information SET country=%s WHERE user_id=%s"
    cur.execute(query, (country, user_id))
    print("Changed country of user_id", user_id, "to", country)
# filter and return result  
    db.commit()
    
def change_countrycode(user_id, countrycode):
    cur = connect()
    query = "UPDATE information SET phone_Countrycode=%s WHERE user_id=%s"
    cur.execute(query, (countrycode, user_id))
    print("Changed country of user_id", user_id, "to", countrycode)
# filter and return result  
    db.commit()
    
    
def change_birthday(user_id, birthday):
    cur = connect()
    query = "UPDATE information SET birthday=%s WHERE user_id=%s"
    cur.execute(query, (birthday, user_id))
    print("Changed country of user_id", user_id, "to", birthday)
# filter and return result  
    db.commit()