'''
Created on Oct 16, 2017

@author: bjarke
'''
import pymysql

db = pymysql.connect(host="127.0.0.1",  # your host 
                     user="root",       # username
                     passwd="root",     # password
                     db="OnlineID" # name of the database, commented out since I am creating the DB in the string below
                     )   
 
# Create a Cursor object to execute queries.
cur = db.cursor()


cur.execute("INSERT INTO information VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", 'Trump', 'Trump', 'Trumpstreet', raw_input("adressnumber: "), raw_input("postcode: "), raw_input("country: "), raw_input("birthday: "), raw_input("gender: "),raw_input("countrycode: "), raw_input("phone: "), raw_input("email: "), 'false', 'hashedpassword', 'saltandpepper')