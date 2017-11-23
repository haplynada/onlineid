'''
Created on Nov 2, 2017
 
@author: Bjarke Larsen
'''
import pymysql
from database_handling.connect import connect
 
def delete_user(user_id):
    cur = connect()
    
    # Create query
    query = "DELETE FROM information WHERE user_id = %s;"
    
    #Execute query
    cur.execute(query, (user_id,))
    
    #Accept changes
    cur.commit()
    
    #Close connection
    cur.close()

    return True