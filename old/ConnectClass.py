'''
Created on 23. nov. 2017

@author: Tor Larssen Sekse
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
            