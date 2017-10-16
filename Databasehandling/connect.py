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
                    first_name varchar(50) NOT NULL,
                    last_name varchar(50) NOT NULL,
                    adress varchar(50) NOT NULL,
                    adress_number int(20) NOT NULL,
                    zip_code int(11) NOT NULL,
                    country varchar(50) NOT NULL,
                    birthday date NOT NULL,
                    sex ENUM( 'male', 'female', 'other') NOT NULL,
                    phone_Countrycode int(11) NOT NULL,
                    phonenumber int(11) NOT NULL,
                    email varchar(50) NOT NULL,
                    hashed_Passwords varchar(70) NOT NULL,
                    salt varchar(50) NOT NULL,
                    user_id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY
                                    );

CREATE TABLE IF NOT EXISTS sites (
                                site_Adress VARCHAR(50) NOT NULL,
                                site_id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY                                
                                                    );
                                                    
CREATE TABLE IF NOT EXISTS firstlogon (
                                site_id INT UNSIGNED NOT NULL,
                                user_id INT UNSIGNED NOT NULL,
                                date_reg TIMESTAMP,
                                PRIMARY KEY(site_id, user_id)
                                                    );
                                                    
CREATE TABLE IF NOT EXISTS log (
                                site_id INT UNSIGNED NOT NULL,
                                user_id INT UNSIGNED NOT NULL,
                                date_login TIMESTAMP,
                                ip_adress INT UNSIGNED NOT NULL,
                                PRIMARY KEY(site_id, user_id, date_login)
                                                    );

CREATE TABLE IF NOT EXISTS emailValid (
                                user_id INT UNSIGNED NOT NULL,
                                email_valid ENUM ('true', 'false') NOT NULL,
                                PRIMARY KEY (user_id, email_valid)
                                );
                                
                                                    


 """
# Select data from table using SQL query.
cur.execute(query)

