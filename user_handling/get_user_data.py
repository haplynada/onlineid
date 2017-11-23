'''
Created on 5. okt. 2017

@author: Tor Larssen Sekse/Alexander Mackenzie-Low/Bjarke Larsen
''' 
import pymysql
from database_handling.connect import connect

def get_all(user_id):
    cur = connect()
    
    query = "SELECT * from information WHERE user_id =%s;"
    cur.execute(query, (user_id))
# filter and return result  
    result = str(cur.fetchall()[0])
    return(result)


def get_firstname(user_id):
    cur = connect()
    
    query = "SELECT first_name from information WHERE user_id =%s;"
    cur.execute(query, (user_id))
# filter and return result  
    result = str(cur.fetchone()[0])
    return(result)

def get_lastname(user_id):
    cur = connect()
    query = "SELECT last_name from information WHERE user_id =%s;"
    cur.execute(query, (user_id))
# filter and return result  
    result = str(cur.fetchone()[0])
    return(result)
       
def get_adress(user_id):
    cur = connect()
    query = "SELECT adress from information WHERE user_id =%s;"
    cur.execute(query, (user_id))
# filter and return result  
    result = str(cur.fetchone()[0])
    return(result)
   
def get_adress_number(user_id):
    cur = connect()
    query = "SELECT adress_number from information WHERE user_id =%s;"
    cur.execute(query, (user_id))
# filter and return result  
    result = str(cur.fetchone()[0])
    return(result)
  
def get_post_code(user_id):
    cur = connect()
    query = "SELECT zip_code from information WHERE user_id =%s;"
    cur.execute(query, (user_id))
# filter and return result  
    result = str(cur.fetchone()[0])
    return(result)
   
def get_country(user_id):
    cur = connect()
    query = "SELECT country from information WHERE user_id =%s;"
    cur.execute(query, (user_id))
# filter and return result  
    result = str(cur.fetchone()[0])
    return(result)
 
def get_birthday(user_id):
    cur = connect()
    query = "SELECT birthday from information WHERE user_id =%s;"
    cur.execute(query, (user_id))
# filter and return result  
    result = str(cur.fetchone()[0])
    return(result)
 
def get_sex(user_id):
    cur = connect()
    query = "SELECT sex from information WHERE user_id =%s;"
    cur.execute(query, (user_id))
# filter and return result  
    result = str(cur.fetchone()[0])
    return(result)
  
def get_phone_Country(user_id):
    cur = connect()
    query = "SELECT phone_Countrycode from information WHERE user_id =%s;"
    cur.execute(query, (user_id))
# filter and return result  
    result = str(cur.fetchone()[0])
    return(result)
  
def get_phonenumber(user_id):
    cur = connect()
    query = "SELECT phonenumber from information WHERE user_id =%s;"
    cur.execute(query, (user_id))
# filter and return result  
    result = str(cur.fetchone()[0])
    return(result)
  
def get_email(user_id):
    cur = connect()
    query = "SELECT email from information WHERE user_id =%s;"
    cur.execute(query, (user_id))
# filter and return result  
    result = str(cur.fetchone()[0])
    return(result)
 
def get_hashed_Password(user_id):
    cur = connect()
    query = "SELECT hashed_Passwords from information WHERE user_id =%s;"
    cur.execute(query, (user_id))
# filter and return result  
    result = str(cur.fetchone()[0])
    return(result)
   
def get_salt(user_id):
    cur = connect()
    query = "SELECT salt from information WHERE user_id =%s;"
    cur.execute(query, (user_id))
# filter and return result  
    result = str(cur.fetchone()[0])
    return(result)
                                   