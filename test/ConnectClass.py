'''
Created on 23. nov. 2017

@author: Tor Larssen Sekse
'''
import pymysql

class Connect:
    
    def __init__(self):
        self.db = pymysql.connect(host="88.88.170.2",  # your host 
        user="server",       # username
        passwd="sudoonlineid",     # password
        db="OnlineID" # name of the database, commented out since I am creating the DB in the string below
        )    
        self.db_cur = self.db.cursor()
        
    def query(self, query, parameters):
        return self.db_cur.execute(query, parameters)
        
    def __del__(self):
        self.db.close()