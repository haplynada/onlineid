'''
Created on 23. nov. 2017

@author: Tor Larssen Sekse
'''
from test.ConnectClass import Connect

cur = Connect
user_id = "1"
birthday = "2017-01-01"

def change_birthday(user_id, birthday):
    query = "UPDATE information SET birthday=%s WHERE user_id=%s"
    Connect.query(query, birthday)
    print("Changed country of user_id", user_id, "to", birthday)
    

change_birthday(user_id, birthday)