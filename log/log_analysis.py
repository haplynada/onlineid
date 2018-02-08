'''
Created on 7. feb. 2018



@author: Tor Larssen Sekse
'''

from database_handling.connect import Connect
import datetime

results = [[None, None, None]]

with Connect() as db:
    query = "SELECT * from activelog;"
    db.cur.execute(query)
    data = db.cur.fetchall()
    
for line in data:
    print(line)
    
    for list in results:
        if list[0] == line[1]:
            list[2] +=1
        else:
            results.append([line[1], line[2][:-3], 1])
        """
        if list[1] == line[2][:-3]:
            print(line[2][:-3])
"""
print(results)