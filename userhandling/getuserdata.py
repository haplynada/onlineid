'''
Created on 5. okt. 2017

@author: Tor Larssen Sekse/Alexander Mackenzie-Low
''' 
import pymysql

def get_hashedpassword(user):
    
    db = pymysql.connect(host="127.0.0.1",  # your host 
        user="root",       # username
        passwd="root",     # password
        db="OnlineID")   # name of the database
 
# Create a Cursor object to execute queries.
    cur = db.cursor()
    query = "SELECT hashed_Passwords from information WHERE user_id =%s;"
    cur.execute(query, (user))
# filter and return result  
    result = str(cur.fetchone()[0])
    return(result)
    print(result)

def get_salt(user):
    
    db = pymysql.connect(host="127.0.0.1",  # your host 
        user="root",       # username
        passwd="root",     # password
        db="OnlineID")   # name of the database
 
# Create a Cursor object to execute queries.
    cur = db.cursor()
    query = "SELECT salt from information WHERE user_id =%s;"
    cur.execute(query, (user))
# filter and return result  
    result = str(cur.fetchone()[0])
    return(result)
    print(result)
