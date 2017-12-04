'''
Created on 12. okt. 2017
The change_xxxx functions changes user data in the database. The user needs to be
authenticated before any of these functions are called, because they don't authenticate
the user before posting their data 
@author: Tor Larssen Sekse
'''
from user_handling.input_control import *
from database_handling.connect import Connect
from user_handling.authenticate_user import generate_salt, hash_password


def change_email(user_id, email):
    """
    The change_email function changes user data in the database. The user needs to be
    authenticated before this function is called, because it doesn't authenticate
    the user before posting their data 
    
    Args:
        user_id: an int containing the users user_id in the database
        email: a string containing the new data
    Returns: 
        True/False depending on whether the data is changed or not
    
    """
    checker = False
    if check_email(email) == True:
        with Connect() as db:
            query = "UPDATE information SET email=%s WHERE user_id=%s"
            db.cur.execute(query, (email, user_id))
            # filter and return result  
            db.conn.commit()
            checker = True
            return checker

    else:
        return checker

def change_firstname(user_id, first_name):
    """
    The change_firstname function changes user data in the database. The user needs to be
    authenticated before this function is called, because it doesn't authenticate
    the user before posting their data 
    
    Args:
        user_id: an int containing the users user_id in the database
        first_name: a string containing the new data
    Returns: 
        True/False depending on whether the data is changed or not
    
    """
    checker = False
    if check_firstname(first_name) == True:
        with Connect() as db: 
            query = "UPDATE information SET first_name=%s WHERE user_id=%s"
            db.cur.execute(query, (first_name, user_id))
            #filter and return result  
            db.conn.commit()
            checker = True
            return checker
    else:
        return checker
    
def change_lastname(user_id, last_name):
    """
    The change_lastname function changes user data in the database. The user needs to be
    authenticated before this function is called, because it doesn't authenticate
    the user before posting their data 
    
    Args:
        user_id: an int containing the users user_id in the database
        last_name: a string containing the new data
    Returns: 
        True/False depending on whether the data is changed or not
    
    """
    checker = False
    if check_lastname(last_name) == True:
        with Connect() as db: 
            query = "UPDATE information SET last_name=%s WHERE user_id=%s"
            db.cur.execute(query, (last_name, user_id))
            # filter and return result  
            db.conn.commit()
            checker = True
            return checker
    else:
        return checker
    
def change_phonenumber(user_id, phone_number):
    """
    The change_phonenumber function changes user data in the database. The user needs to be
    authenticated before this function is called, because it doesn't authenticate
    the user before posting their data 
    
    Args:
        user_id: an int containing the users user_id in the database
        phone_number: a string containing the new data
    Returns: 
        True/False depending on whether the data is changed or not
    
    """
    checker = False
    if check_phonenumber(phone_number) == True:
        with Connect() as db: 
            query = "UPDATE information SET phoneNumber=%s WHERE user_id=%s"
            db.cur.execute(query, (phone_number, user_id))
            # filter and return result  
            db.conn.commit()
            checker = True
            return checker
    else:
        return checker
    
def change_adress(user_id, adress):
    """
    The change_adress function changes user data in the database. The user needs to be
    authenticated before this function is called, because it doesn't authenticate
    the user before posting their data 
    
    Args:
        user_id: an int containing the users user_id in the database
        adress: a string containing the new data
    Returns: 
        True/False depending on whether the data is changed or not
    
    """
    checker = False
    if check_adress(adress) == True:
        with Connect() as db: 
            query = "UPDATE information SET adress=%s WHERE user_id=%s"
            db.cur.execute(query, (adress, user_id))
            # filter and return result  
            db.conn.commit()
            checker = True
            return checker
    else:
        return checker
    
def change_adress_number(user_id, adress_number):
    """
    The change_adress_number function changes user data in the database. The user needs to be
    authenticated before this function is called, because it doesn't authenticate
    the user before posting their data 
    
    Args:
        user_id: an int containing the users user_id in the database
        adress_number: a string containing the new data
    Returns: 
        True/False depending on whether the data is changed or not
    
    """
    checker = False
    if check_adressnumber(adress_number) == True:
        with Connect() as db: 
            query = "UPDATE information SET adress_number=%s WHERE user_id=%s"
            db.cur.execute(query, (adress_number, user_id))
            # filter and return result  
            db.conn.commit()
            checker = True
            return checker
    else:
        return checker
    
def change_post_code(user_id, postcode):
    """
    The change_post_code function changes user data in the database. The user needs to be
    authenticated before this function is called, because it doesn't authenticate
    the user before posting their data 
    
    Args:
        user_id: an int containing the users user_id in the database
        postcode: a string containing the new data
    Returns: 
        True/False depending on whether the data is changed or not
    
    """
    checker = False
    if check_postcode(postcode) == True: 
        with Connect() as db: 
            query = "UPDATE information SET zip_code=%s WHERE user_id=%s"
            db.cur.execute(query, (postcode, user_id))
            db.conn.commit()
            checker = True
            return checker
    else: 
        return checker
    
def change_country(user_id, country):
    """
    The change_country function changes user data in the database. The user needs to be
    authenticated before this function is called, because it doesn't authenticate
    the user before posting their data 
    
    Args:
        user_id: an int containing the users user_id in the database
        country: a string containing the new data
    Returns: 
        True/False depending on whether the data is changed or not
    
    """
    checker = False
    if check_country(country) == True:
        with Connect() as db: 
            query = "UPDATE information SET country=%s WHERE user_id=%s"
            db.cur.execute(query, (country, user_id))
            db.conn.commit()
            checker = True
            return checker
    else:
        return checker
    
def change_countrycode(user_id, countrycode):
    """
    The change_countrycode function changes user data in the database. The user needs to be
    authenticated before this function is called, because it doesn't authenticate
    the user before posting their data 
    
    Args:
        user_id: an int containing the users user_id in the database
        countrycode: a string containing the new data
    Returns: 
        True/False depending on whether the data is changed or not
    
    """
    checker = False
    if check_countrycode(countrycode) == True:
        with Connect() as db:
            query = "UPDATE information SET phone_Countrycode=%s WHERE user_id=%s"
            db.cur.execute(query, (countrycode, user_id))
            db.conn.commit()
            checker = True
            return checker
    else:
        return checker
    
def change_birthday(user_id, birthday):
    """
    The change_birthday function changes user data in the database. The user needs to be
    authenticated before this function is called, because it doesn't authenticate
    the user before posting their data 
    
    Args:
        user_id: an int containing the users user_id in the database
        birthday: a string containing the new data
    Returns: 
        True/False depending on whether the data is changed or not
    
    """
    checker = False
    if check_birthday(birthday) == True:
        with Connect() as db: 
            query = "UPDATE information SET birthday=%s WHERE user_id=%s"
            db.cur.execute(query, (birthday, user_id))
            db.conn.commit()
            checker = True
            return checker
    else: 
        return checker
    
def change_gender(user_id, gender):
    """
    The change_gender function changes user data in the database. The user needs to be
    authenticated before this function is called, because it doesn't authenticate
    the user before posting their data 
    
    Args:
        user_id: an int containing the users user_id in the database
        gender: a string containing the new data
    Returns: 
        True/False depending on whether the data is changed or not
    
    """
    checker = False
    if check_gender(gender) == True: 
        with Connect() as db:
            query = "UPDATE information SET sex=%s WHERE user_id=%s"
            db.cur.execute(query, (gender, user_id))
            db.conn.commit()
            checker = True
            return checker
    else: 
        return checker

def change_password(user_id, password):
    """
    The change_email function changes user data in the database. The user needs to be
    authenticated before this function is called, because it doesn't authenticate
    the user before posting their data. This function will also generate a new salt instead 
    of reusing the one stored in the database already. The new salt will then be stored.
    
    Args:
        user_id: an int containing the users user_id in the database
        password: a string containing the new data
    Returns: 
        True/False depending on whether the data is changed or not
    
    """
    checker = False
    if check_password(password) == True:
        password_salt = generate_salt()
        hashed_password = hash_password(password_salt, password)
        with Connect() as db: 
            query = "UPDATE information SET hashed_passwords=%s WHERE user_id=%s"
            db.cur.execute(query, (hashed_password, user_id))
            db.conn.commit()
            query = "UPDATE information SET salt=%s WHERE user_id=%s"
            db.cur.execute(query, (password_salt, user_id))
            db.conn.commit()
            checker = True
            return checker
    else: 
        return checker
            
    