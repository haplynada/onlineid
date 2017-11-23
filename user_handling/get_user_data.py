'''
Created on 5. okt. 2017

@author: Tor Larssen Sekse/Alexander Mackenzie-Low/Bjarke Larsen
'''
from database_handling.connect import connect

def get_all(user_id):
    """Fetches all user-data from the database, based on the user_id.

    The function connects to the database, the curser execute the query. The result from the database is then
    filtered and returned.

    Args:
        user_id: An generated number from the database, which is a primary-key in the databse. It is unique to
            each user and intended to be used for look-up.
        ex: "1"

    Returns:
        A Tuple with each information listed.
        ex: (First_name, Last_name, Street.....)

    This aproach goes for every function below, but they only return one value based on the user_id.
    """
    cur = connect()
    query = "SELECT * from information WHERE user_id =%s;"
    cur.execute(query, (user_id))
    result = str(cur.fetchall()[0])
    return(result)


def get_firstname(user_id):
    cur = connect()
    query = "SELECT first_name from information WHERE user_id =%s;"
    cur.execute(query, (user_id))
    result = str(cur.fetchone()[0])
    return(result)

def get_lastname(user_id):
    cur = connect()
    query = "SELECT last_name from information WHERE user_id =%s;"
    cur.execute(query, (user_id))
    result = str(cur.fetchone()[0])
    return(result)
       
def get_adress(user_id):
    cur = connect()
    query = "SELECT adress from information WHERE user_id =%s;"
    cur.execute(query, (user_id))
    result = str(cur.fetchone()[0])
    return(result)
   
def get_adress_number(user_id):
    cur = connect()
    query = "SELECT adress_number from information WHERE user_id =%s;"
    cur.execute(query, (user_id))
    result = str(cur.fetchone()[0])
    return(result)
  
def get_post_code(user_id):
    cur = connect()
    query = "SELECT zip_code from information WHERE user_id =%s;"
    cur.execute(query, (user_id))
    result = str(cur.fetchone()[0])
    return(result)
   
def get_country(user_id):
    cur = connect()
    query = "SELECT country from information WHERE user_id =%s;"
    cur.execute(query, (user_id))
    result = str(cur.fetchone()[0])
    return(result)
 
def get_birthday(user_id):
    cur = connect()
    query = "SELECT birthday from information WHERE user_id =%s;"
    cur.execute(query, (user_id))
    result = str(cur.fetchone()[0])
    return(result)
 
def get_sex(user_id):
    cur = connect()
    query = "SELECT sex from information WHERE user_id =%s;"
    cur.execute(query, (user_id))
    result = str(cur.fetchone()[0])
    return(result)
  
def get_phone_Country(user_id):
    cur = connect()
    query = "SELECT phone_Countrycode from information WHERE user_id =%s;"
    cur.execute(query, (user_id))
    result = str(cur.fetchone()[0])
    return(result)
  
def get_phonenumber(user_id):
    cur = connect()
    query = "SELECT phonenumber from information WHERE user_id =%s;"
    cur.execute(query, (user_id))
    result = str(cur.fetchone()[0])
    return(result)
  
def get_email(user_id):
    cur = connect()
    query = "SELECT email from information WHERE user_id =%s;"
    cur.execute(query, (user_id))
    result = str(cur.fetchone()[0])
    return(result)
 
def get_hashed_Password(user_id):
    cur = connect()
    query = "SELECT hashed_Passwords from information WHERE user_id =%s;"
    cur.execute(query, (user_id))
    result = str(cur.fetchone()[0])
    return(result)
   
def get_salt(user_id):
    cur = connect()
    query = "SELECT salt from information WHERE user_id =%s;"
    cur.execute(query, (user_id))
    result = str(cur.fetchone()[0])
    return(result)

def get_user_id(email):
    cur = connect()
    query = "SELECT user_id from information WHERE email =%s;"
    cur.execute(query, (email))
    result = str(cur.fetchone()[0])
    return (result)