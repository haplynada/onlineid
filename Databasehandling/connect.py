'''
Created on 5. okt. 2017

@author: Alexander Mackenzie
'''
import pymysql
 
db = pymysql.connect(host="127.0.0.1",  # your host 
                     user="root",       # username
                     passwd="",     # password
                     db="OnlineID")   # name of the database
 
# Create a Cursor object to execute queries.
cur = db.cursor()
 
# Select data from table using SQL query.
cur.execute("SELECT * FROM information")
 
# print the result    
print(cur.fetchall())
