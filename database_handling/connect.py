'''
Created on 5. okt. 2017

@author: Alexander Mackenzie
'''
import pymysql
def connect():
    db = pymysql.connect(host="88.88.170.2",  # your host 
         user="server",       # username
         passwd="sudoonlineid",     # password
         db="OnlineID" # name of the database, commented out since I am creating the DB in the string below
         )    
     
    # Create a Cursor object to execute queries.
    cur = db.cursor()
