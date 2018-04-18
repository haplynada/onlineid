'''
Created on 12. okt. 2017

@author: Alexander Mackenzie-Low, Bjarke Larsen, Tor Larssen Sekse
'''
import pymysql
from database_handling.connect import *

def create_database():
    """ Setup the database.
        Creates a Connect object, and establish a connection to the server. Then the database is created with MySQL.
    """
    with Connect() as db:

        query = """CREATE DATABASE IF NOT EXISTS OnlineID;
    
                    USE OnlineID; 
    
    
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
                                        sex ENUM( 'male', 'female', 'other') NOT NULL,
                                        user_id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY
                                                        );
                    
                    CREATE TABLE IF NOT EXISTS authentication (
                                        hashed_Passwords varchar(64) NOT NULL,
                                        has_2fa varchar(5) NOT NULL,
                                        2fa_secret varchar(32),
                                        user_id INT UNSIGNED NOT NULL,
                                        PRIMARY KEY(user_id)
                                                        );
                                                        
                    CREATE TABLE IF NOT EXISTS emailvalid (
                                                    email_validation varchar(50) DEFAULT "false",
                                                    user_id INT UNSIGNED NOT NULL,
                                                    PRIMARY KEY(user_id, email_validation)
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
    
                    CREATE TABLE IF NOT EXISTS activelog (
                                                    user_id INT UNSIGNED NOT NULL,
                                                    date varchar(50) NOT NULL,
                                                    time varchar(50) NOT NULL, 
                                                    ip_adress varchar(16)  NOT NULL
                                                                        );    
                    CREATE TABLE IF NOT EXISTS activesitelog (
                                                    site varchar(50) NOT NULL, 
                                                    date varchar(50) NOT NULL,
                                                    time varchar(50) NOT NULL
                                                                        );
                    CREATE TABLE IF NOT EXISTS usercreationlog (
                                                    user_id varchar(50) NOT NULL, 
                                                    email varchar(50) NOT NULL,
                                                    ip_adress varchar(16) NOT NULL,
                                                    date varchar(50) NOT NULL,
                                                    time varchar(50) NOT NULL
                                                                        );
                                                                        
                    CREATE TABLE IF NOT EXISTS company (
                                                    company_id varchar(50),
                                                    approved varchar(8),
                                                    company_name varchar(50) NOT NULL, 
                                                    email varchar(50) NOT NULL,
                                                    contact_person varchar(50) NOT NULL,
                                                    phone varchar(16) NOT NULL, 
                                                    country varchar(50) NOT NULL,
                                                    adress varchar(50) NOT NULL, 
                                                    adress_number varchar(50) NOT NULL
                                                                        );
                                                                        
                    CREATE TABLE IF NOT EXISTS deleted_users (
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
                                        sex ENUM( 'male', 'female', 'other') NOT NULL,
                                        user_id INT UNSIGNED NOT NULL PRIMARY KEY
                                                        );
                    
                    CREATE TABLE IF NOT EXISTS deletion_log (
                                        user_id varchar(50) NOT NULL, 
                                        email varchar(50) NOT NULL,
                                        ip_adress varchar(16) NOT NULL,
                                        date varchar(50) NOT NULL,
                                        time varchar(50) NOT NULL
                                                        );
                     """

        # Execute the query
        db.cur.execute(query)
        db.conn.commit()

if __name__ == "__main__":
    create_database()