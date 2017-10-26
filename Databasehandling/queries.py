'''
Created on 12. okt. 2017

@author: Alexander Mackenzie-Low
'''
from Databasehandling.connect import * #Import connect function


#print(connectGet('SELECT * FROM information'))

#userid, table, get whatever information back

#edits

def getuser(email): #enter email get unique ID
    import pymysql

    db = pymysql.connect(host="88.88.170.2",  # your host 
        user="server",       # username
        passwd="sudoonlineid",     # password
        db="OnlineID" # name of the database, commented out since I am creating the DB in the string below
            )  
 
# Create a Cursor object to execute queries.
    cur = db.cursor()
    query = "SELECT user_id from information WHERE email =%s;"
    cur.execute(query, (email))
# filter and return result  
    result = str(cur.fetchone()[0])
    return(result)
