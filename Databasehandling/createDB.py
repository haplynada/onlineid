'''
Created on 12. okt. 2017

@author: Alexander Mackenzie-Low
'''
import pymysql

dbc = pymysql.connect(host="88.88.170.2",  # your host 
        user="server",       # username
        passwd="sudoonlineid",     # password
)

cur = dbc.cursor()

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
                    phone_Countrycode int(11) NOT NULL,
                    phonenumber int(11) NOT NULL,
                    email varchar(50) NOT NULL,
                    email_validation varchar(50) DEFAULT "false",
                    sex ENUM( 'male', 'female', 'other') NOT NULL,
                    hashed_Passwords varchar(64) NOT NULL,
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
 """
# Select data from table using SQL query.
cur.execute(query)

cur.execute("SELECT * FROM information")
 
# print the result    
print(cur.fetchall())