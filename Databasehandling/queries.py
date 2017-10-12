'''
Created on 12. okt. 2017

@author: Alexander Mackenzie-Low
'''
from Databasehandling.connect import * #Import connect function


#print(connectGet('SELECT * FROM information'))

#userid, table, get whatever information back

#edits

def getId(email): #enter email get unique ID
    import pymysql

    db = pymysql.connect(host="127.0.0.1",  # your host 
        user="root",       # username
        passwd="Alexander12#",     # password
        db="OnlineID")   # name of the database
 
# Create a Cursor object to execute queries.
    cur = db.cursor()
    query = "SELECT id from information WHERE email =%s;"
    cur.execute(query, (email))
# filter and return result  
    result = str(cur.fetchone()[0])
    return(result)

print(getId('ola.nordmann@kakeland.no'))