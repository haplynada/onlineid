'''
Created on 5. okt. 2017

@author: Tor Larssen Sekse/Alexander Mackenzie-Low/Bjarke Larsen
''' 
import pymysql

def get_firstname(user_id):
    
    db = pymysql.connect(host="127.0.0.1",  # your host 
        user="root",       # username
        passwd="root",     # password
        db="OnlineID")   # name of the database
 
# Create a Cursor object to execute queries.
    cur = db.cursor()
    query = "SELECT first_name from information WHERE user_id =%s;"
    cur.execute(query, (user_id))
# filter and return result  
    result = str(cur.fetchone()[0])
    return(result)
    print(result)

def get_lastname(user_id):
    
    db = pymysql.connect(host="127.0.0.1",  # your host 
        user="root",       # username
        passwd="root",     # password
        db="OnlineID")   # name of the database
 
# Create a Cursor object to execute queries.
    cur = db.cursor()
    query = "SELECT last_name from information WHERE user_id =%s;"
    cur.execute(query, (user_id))
# filter and return result  
    result = str(cur.fetchone()[0])
    return(result)
    print(result)    

def get_adress(user_id):
    
    db = pymysql.connect(host="127.0.0.1",  # your host 
        user="root",       # username
        passwd="root",     # password
        db="OnlineID")   # name of the database
 
# Create a Cursor object to execute queries.
    cur = db.cursor()
    query = "SELECT adress from information WHERE user_id =%s;"
    cur.execute(query, (user_id))
# filter and return result  
    result = str(cur.fetchone()[0])
    return(result)
    print(result)

def get_adress_number(user_id):
    
    db = pymysql.connect(host="127.0.0.1",  # your host 
        user="root",       # username
        passwd="root",     # password
        db="OnlineID")   # name of the database
 
# Create a Cursor object to execute queries.
    cur = db.cursor()
    query = "SELECT adress_number from information WHERE user_id =%s;"
    cur.execute(query, (user_id))
# filter and return result  
    result = str(cur.fetchone()[0])
    return(result)
    print(result)

def get_zip_code(user_id):
    
    db = pymysql.connect(host="127.0.0.1",  # your host 
        user="root",       # username
        passwd="root",     # password
        db="OnlineID")   # name of the database
 
# Create a Cursor object to execute queries.
    cur = db.cursor()
    query = "SELECT zip_code from information WHERE user_id =%s;"
    cur.execute(query, (user_id))
# filter and return result  
    result = str(cur.fetchone()[0])
    return(result)
    print(result)

def get_country(user_id):
    
    db = pymysql.connect(host="127.0.0.1",  # your host 
        user="root",       # username
        passwd="root",     # password
        db="OnlineID")   # name of the database
 
# Create a Cursor object to execute queries.
    cur = db.cursor()
    query = "SELECT country from information WHERE user_id =%s;"
    cur.execute(query, (user_id))
# filter and return result  
    result = str(cur.fetchone()[0])
    return(result)
    print(result)

def get_birthday(user_id):
    
    db = pymysql.connect(host="127.0.0.1",  # your host 
        user="root",       # username
        passwd="root",     # password
        db="OnlineID")   # name of the database
 
# Create a Cursor object to execute queries.
    cur = db.cursor()
    query = "SELECT birthday from information WHERE user_id =%s;"
    cur.execute(query, (user_id))
# filter and return result  
    result = str(cur.fetchone()[0])
    return(result)
    print(result)

def get_sex(user_id):
    
    db = pymysql.connect(host="127.0.0.1",  # your host 
        user="root",       # username
        passwd="root",     # password
        db="OnlineID")   # name of the database
 
# Create a Cursor object to execute queries.
    cur = db.cursor()
    query = "SELECT sex from information WHERE user_id =%s;"
    cur.execute(query, (user_id))
# filter and return result  
    result = str(cur.fetchone()[0])
    return(result)
    print(result)

def get_phone_Country(user_id):
    
    db = pymysql.connect(host="127.0.0.1",  # your host 
        user="root",       # username
        passwd="root",     # password
        db="OnlineID")   # name of the database
 
# Create a Cursor object to execute queries.
    cur = db.cursor()
    query = "SELECT phone_Countrycode from information WHERE user_id =%s;"
    cur.execute(query, (user_id))
# filter and return result  
    result = str(cur.fetchone()[0])
    return(result)
    print(result) 

def get_phonenumber(user_id):
    
    db = pymysql.connect(host="127.0.0.1",  # your host 
        user="root",       # username
        passwd="root",     # password
        db="OnlineID")   # name of the database
 
# Create a Cursor object to execute queries.
    cur = db.cursor()
    query = "SELECT phonenumber from information WHERE user_id =%s;"
    cur.execute(query, (user_id))
# filter and return result  
    result = str(cur.fetchone()[0])
    return(result)
    print(result)

def get_email(user_id):
    
    db = pymysql.connect(host="127.0.0.1",  # your host 
        user="root",       # username
        passwd="root",     # password
        db="OnlineID")   # name of the database
 
# Create a Cursor object to execute queries.
    cur = db.cursor()
    query = "SELECT email from information WHERE user_id =%s;"
    cur.execute(query, (user_id))
# filter and return result  
    result = str(cur.fetchone()[0])
    return(result)
    print(result)

def get_hashed_Passwords(user_id):
    
    db = pymysql.connect(host="127.0.0.1",  # your host 
        user="root",       # username
        passwd="root",     # password
        db="OnlineID")   # name of the database
 
# Create a Cursor object to execute queries.
    cur = db.cursor()
    query = "SELECT hashed_Passwords from information WHERE user_id =%s;"
    cur.execute(query, (user_id))
# filter and return result  
    result = str(cur.fetchone()[0])
    return(result)
    print(result)

def get_salt(user_id):
    
    db = pymysql.connect(host="127.0.0.1",  # your host 
        user="root",       # username
        passwd="root",     # password
        db="OnlineID")   # name of the database
 
# Create a Cursor object to execute queries.
    cur = db.cursor()
    query = "SELECT salt from information WHERE user_id =%s;"
    cur.execute(query, (user_id))
# filter and return result  
    result = str(cur.fetchone()[0])
    return(result)
    print(result)                                  