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


add_user = ("INSERT INTO information "
               "(first_name, last_name, adress, adress_number, zip_code, country, birthday, sex, phone_Countrycode, phonenumber, email, email_validation, hashed_Passwords, salt) "
               "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")

data_user = ('Alex', 'Larsen', 'Trumpstreet', 9, 0001, 'USA', '1945-06-04', 'female', 1, 00000001, 'mr.president@usa.com', 'true', 'hashedpassword', 'saltandpepper')

cur.execute(add_user, data_user)

db.commit()

db.close()
