'''
Created on 5. okt. 2017

@author: Alexander Mackenzie
'''
import pymysql
 
db = pymysql.connect(host="127.0.0.1",  # your host 
                     user="root",       # username
                     passwd="Alexander12#",     # password
                     #db="OnlineID" # name of the database, commented out since I am creating the DB in the string below
                     )   
 
# Create a Cursor object to execute queries.
cur = db.cursor()
query = """CREATE DATABASE IF NOT EXISTS OnlineId;

USE OnlineId;

CREATE TABLE IF NOT EXISTS information (
                                    id int(11) NOT NULL AUTO_INCREMENT,
                                    first_name varchar(50) NOT NULL,
                    last_name varchar(50) NOT NULL,
                    adress varchar(50) NOT NULL,
                    adress_number varchar(50) NOT NULL,
                    zip_code int(11) NOT NULL,
                    country varchar(50) NOT NULL,
                    birthday date NOT NULL,
                    phone_Countrycode int(11) NOT NULL,
                    phonenumber int(11) NOT NULL,
                    email varchar(50) NOT NULL,
                    email_validation varchar(50) NOT NULL,
                    hashed_Passwords varchar(50) NOT NULL,
                    salt varchar(50) NOT NULL,
                    PRIMARY KEY(id)
                                    );

CREATE TABLE IF NOT EXISTS sites (
                                site_ID int(11) NOT NULL AUTO_INCREMENT,
                                site_Adress VARCHAR(50) NOT NULL,
                                PRIMARY KEY(site_ID)
                                                    );
                                                    
CREATE TABLE IF NOT EXISTS connecter (
                                site_ID int(11) NOT NULL,
                                id int(11) NOT NULL,
                                date_reg datetime NOT NULL,
                                PRIMARY KEY(site_ID)
                                                    );
                                                    
CREATE TABLE IF NOT EXISTS log (
                                site_ID int(11) NOT NULL,
                                id int(11) NOT NULL,
                                date_login DATETIME NOT NULL,
                                ip_adress int unsigned NOT NULL,
                                PRIMARY KEY(site_ID)
                                                    );
                                                    

INSERT INTO information (first_name, last_name, adress, adress_number, zip_code, country, birthday, phone_Countrycode, phonenumber, email, email_validation, hashed_Passwords, salt)
                                VALUES ('Ola', 'Nordmann', 'Kongensgate', 1, 1337, 'Norway', '1995-10-12', 47, 12345678, 'ola.nordmann@kakeland.no', 'false', 'hashedpassword', 'saltandpepper');

INSERT INTO sites (site_adress)
    VALUES ('Google.com'),
           ('Komplett.no');

INSERT INTO connecter (site_ID, id, date_reg)
    VALUES (1,1,'2017-10-05 15:32:31'),
           (2,1,'2017-10-05 15:35:15'); 
 """
# Select data from table using SQL query.
cur.execute(query)

cur.execute("SELECT * FROM information")
 
# print the result    
print(cur.fetchall())
