'''
Created on 12. okt. 2017

@author: Tor Larssen Sekse
'''
from userhandling.inputcontrol import *
from userhandling.authenticateuser import authenticate_user

def change_email(user, password, email):
    checker = False
    if check_email(email) == True:
        authenticate_user(user, password)
        #store new email in the database
        checker = True
        return checker
    else:
        return checker

def change_firstname(user_id, first_name):
    import pymysql

    db = pymysql.connect(host="88.88.170.2",  # your host 
        user="server",       # username
        passwd="sudoonlineid",     # password
        db="OnlineID" # name of the database, commented out since I am creating the DB in the string below
            )  
 
# Create a Cursor object to execute queries.
    cur = db.cursor()
    query = "UPDATE information SET first_name=%s WHERE user_id=%s"
    cur.execute(query, (first_name, user_id))
    print("Changed first name of user_id", user_id, "to", first_name)
# filter and return result  
    db.commit()
    
def change_lastname(user_id, last_name):
    import pymysql

    db = pymysql.connect(host="88.88.170.2",  # your host 
        user="server",       # username
        passwd="sudoonlineid",     # password
        db="OnlineID" # name of the database, commented out since I am creating the DB in the string below
            )  
 
# Create a Cursor object to execute queries.
    cur = db.cursor()
    query = "UPDATE information SET last_name=%s WHERE user_id=%s"
    cur.execute(query, (last_name, user_id))
    print("Changed last name of user_id", user_id, "to", last_name)
# filter and return result  
    db.commit()
    
def change_phonenumber(user_id, phoneNumber):
    import pymysql

    db = pymysql.connect(host="88.88.170.2",  # your host 
        user="server",       # username
        passwd="sudoonlineid",     # password
        db="OnlineID" # name of the database, commented out since I am creating the DB in the string below
            )  
 
# Create a Cursor object to execute queries.
    cur = db.cursor()
    query = "UPDATE information SET phoneNumber=%s WHERE user_id=%s"
    cur.execute(query, (phoneNumber, user_id))
    print("Changed phone number of user_id", user_id, "to", phoneNumber)
# filter and return result  
    db.commit()
    
def change_adress(user_id, address):
    import pymysql

    db = pymysql.connect(host="88.88.170.2",  # your host 
        user="server",       # username
        passwd="sudoonlineid",     # password
        db="OnlineID" # name of the database, commented out since I am creating the DB in the string below
            )  
 
# Create a Cursor object to execute queries.
    cur = db.cursor()
    query = "UPDATE information SET adress=%s WHERE user_id=%s"
    cur.execute(query, (address, user_id))
    print("Changed address of user_id", user_id, "to", address)
# filter and return result  
    db.commit()
    
    
def change_postcode(user_id, postcode):
    import pymysql

    db = pymysql.connect(host="88.88.170.2",  # your host 
        user="server",       # username
        passwd="sudoonlineid",     # password
        db="OnlineID" # name of the database, commented out since I am creating the DB in the string below
            )  
 
# Create a Cursor object to execute queries.
    cur = db.cursor()
    query = "UPDATE information SET zip_code=%s WHERE user_id=%s"
    cur.execute(query, (postcode, user_id))
    print("Changed postcode of user_id", user_id, "to", postcode)
# filter and return result  
    db.commit()
    
def change_country(user_id, country):
    import pymysql

    db = pymysql.connect(host="88.88.170.2",  # your host 
        user="server",       # username
        passwd="sudoonlineid",     # password
        db="OnlineID" # name of the database, commented out since I am creating the DB in the string below
            )  
 
# Create a Cursor object to execute queries.
    cur = db.cursor()
    query = "UPDATE information SET country=%s WHERE user_id=%s"
    cur.execute(query, (country, user_id))
    print("Changed country of user_id", user_id, "to", country)
# filter and return result  
    db.commit()
    
def change_countrycode(user_id, countrycode):
    import pymysql

    db = pymysql.connect(host="88.88.170.2",  # your host 
        user="server",       # username
        passwd="sudoonlineid",     # password
        db="OnlineID" # name of the database, commented out since I am creating the DB in the string below
            )  
 
# Create a Cursor object to execute queries.
    cur = db.cursor()
    query = "UPDATE information SET phone_Countrycode=%s WHERE user_id=%s"
    cur.execute(query, (countrycode, user_id))
    print("Changed country of user_id", user_id, "to", countrycode)
# filter and return result  
    db.commit()
    
    
def change_birthday(user_id, birthday):
    import pymysql

    db = pymysql.connect(host="88.88.170.2",  # your host 
        user="server",       # username
        passwd="sudoonlineid",     # password
        db="OnlineID" # name of the database, commented out since I am creating the DB in the string below
            )  
 
# Create a Cursor object to execute queries.
    cur = db.cursor()
    query = "UPDATE information SET birthday=%s WHERE user_id=%s"
    cur.execute(query, (birthday, user_id))
    print("Changed country of user_id", user_id, "to", birthday)
# filter and return result  
    db.commit()
    
    