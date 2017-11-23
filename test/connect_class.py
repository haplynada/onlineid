'''
Created on 23. nov. 2017

@author: Tor Larssen Sekse
'''
import pymysql

class Connect():
    db = pymysql.connect(host="88.88.170.2",  # your host 
    user="server",       # username
    passwd="sudoonlineid",     # password
    db="OnlineID" # name of the database, commented out since I am creating the DB in the string below
    )    
     
    # Create a Cursor object to execute queries.
    cur = db.cursor()
    return cur
