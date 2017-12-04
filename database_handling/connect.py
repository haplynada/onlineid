'''
Created on 5. okt. 2017

@author: Alexander Mackenzie/ Tor Larssen Sekse
'''
import pymysql

class Connect(object):
    
    def __init__(self):
        self.conn = pymysql.connect(host="88.88.170.2",  # your host 
        user="server",       # username
        passwd="sudoonlineid",     # password
        db="OnlineID" # name of the database, commented out since I am creating the DB in the string below
        )    
        self.cur = self.conn.cursor()
        
    def __enter__(self):
        return Connect()
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.close()


"""
Not in use/broken commented for "keeping"

def connect():
    db = pymysql.connect(host="88.88.170.2",  # your host 
         user="server",       # username
         passwd="sudoonlineid",     # password
         db="OnlineID" # name of the database, commented out since I am creating the DB in the string below
         )    
     
    # Create a Cursor object to execute queries.
    #cur = db.cursor()
    return db
"""
