'''
Created on 23. nov. 2017

@author: Tor Larssen Sekse
'''
from test.ConnectClass import Connect 
from user_handling.input_control import check_firstname


user_id = "1"
birthday = "2017-01-01"
user = "1"
first_name = "Sau"

with Connect() as db:
    query = "SELECT first_name from information WHERE user_id =%s;"
    db.cur.execute(query, (user_id))
    result = str(db.cur.fetchone()[0])
    print(result)

def change_firstname(user, first_name):
    checker = False
    if check_firstname(first_name) == True:
        with Connect() as db:
            query = "UPDATE information SET first_name=%s WHERE user_id=%s"
            db.cur.execute(query, (first_name, user))
            #filter and return result  
            db.conn.commit()
            checker = True
            return checker
    else:
        return checker
    
print(change_firstname(user, first_name))