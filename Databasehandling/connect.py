'''
Created on 5. okt. 2017

@author: Alexander Mackenzie
'''
import pymysql
 
db = pymysql.connect(host="127.0.0.1",  # your host 
                     user="root",       # username
                     passwd="root",     # password
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
                                                    


 """
# Select data from table using SQL query.
cur.execute(query)

