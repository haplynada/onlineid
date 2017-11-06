'''
Created on Nov 2, 2017
 
@author: Bjarke Larsen
'''
import pymysql
 
def deleteuser(user_id):
   
    db = pymysql.connect(host="88.88.170.2",  # your host
         user="server",       # username
         passwd="sudoonlineid",     # password
         db="OnlineID" # name of the database, commented out since I am creating the DB in the string below
         )  
 
    # Create a Cursor object to execute queries.
    cur = db.cursor()
    
    # Create query
    query = "DELETE FROM information WHERE user_id = %s;"
    
    #Execute query
    cur.execute(query, (user_id,))
    
    #Accept changes
    db.commit()
    
    #Close connection
    cur.close()
    db.close()
    return True