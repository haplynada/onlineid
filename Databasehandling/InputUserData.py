'''
Created on Oct 16, 2017

@author: bjarke
'''
from userhandling.newuser import * #import a users input
from Databasehandling.connect import * #connects to the database
import pymysql
from userhandling.newuser import create_user
from userhandling.inputerrors import firstname_error


db = pymysql.connect(host="127.0.0.1",  # your host 
                     user="root",       # username
                     passwd="root",     # password
                     db="OnlineID" # name of the database, commented out since I am creating the DB in the string below
                     )   
 
# Create a Cursor object to execute queries.
cur = db.cursor()

first_name = create_user(firstname)
last_name = create_user(lastname)
adress = create_user(adress)
zip_code = create_user(postcode)
country = create_user(country)
birthday = create_user(birthday)
phone_Countrycode = create_user(countrycode)
phonenumber = create_user(phone)
email = create_user(email)
sex = create_user(gender)

user = ['first_name', 'last_name', 'adress', adress_number, zip_code, 'country', 'birthday', phone_Countrycode, phonenuber, 'email', 'sex']

cur.execute("""INSERT INTO information VALUES (user)""".format(*))
