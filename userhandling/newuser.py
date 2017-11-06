'''
Created on 5. okt. 2017

@author: Tor Larssen Sekse, Bjarke
'''
from passwordhandling.passwordsecurity import generate_salt, hash_password
from userhandling.inputcontrol import *
from userhandling.inputerrors import *
from Databasehandling.connect import *
import pymysql

class storage_error(Exception):
    pass


def create_user(email, password, firstname, lastname, phone, postcode, country, countrycode, adress, adressnumber, birthday, gender):
    checker = False
    passwordsalt = generate_salt()
    hashedpassword =""
    errors = ""
    try:
        if check_password(password) == True:
            hashedpassword = hash_password(passwordsalt, password)
            pass
        else:
            raise password_error()
    except password_error:
        errors += str(password_error.error)
        errors += "\n"
        
    try:
        if check_email(email) == True:
            pass
        else:
            raise email_error()
    except email_error:
        errors += str(email_error.error)
        errors += "\n"

    try:
        if check_email_database(email) == True:
            pass
        else:
            raise email_database_error()
    except email_database_error:
        errors += str(email_database_error.error)
        errors += "\n"
        
    try:
        if check_firstname(firstname) ==True:
            pass
        else:
            raise firstname_error()
    except firstname_error:
        errors += str(firstname_error.error)
        errors += "\n"
        
    try:
        if check_lastname(lastname) ==True:
            pass
        else:
            raise lastname_error()
    except lastname_error:
        errors += str(lastname_error.error)
        errors += "\n"
        
    try:
        if check_phonenumber(phone) ==True:
            pass
        else:
            raise phonenumber_error()
    except phonenumber_error:
        errors += str(phonenumber_error.error)
        errors += "\n"
        
    try:
        if check_adress(adress) ==True:
            pass
        else:
            raise adress_error()
    except adress_error:
        errors += str(adress_error.error)
        errors += "\n"
        
    try:
        if check_adressnumber(adressnumber) ==True:
            pass
        else:
            raise adressnumber_error()
    except adressnumber_error:
        errors += str(adressnumber_error.error)
        errors += "\n"
        
    try:
        if check_postcode(postcode) ==True:
            pass
        else:
            raise postcode_error()
    except postcode_error:
        errors += str(postcode_error.error)
        errors += "\n"
        
    try:
        if check_country(country) ==True:
            pass
        else:
            raise country_error()
    except country_error:
        errors += str(country_error.error)
        errors += "\n"
        
    try:
        if check_countrycode(countrycode) ==True:
            pass
        else:
            raise countrycode_error()
    except countrycode_error:
        errors += str(countrycode_error.error)
        errors += "\n"
    try:
        if check_birthday(birthday) ==True:
            pass
        else:
            raise birthday_error()
    except birthday_error:
        errors += str(birthday_error.error)
        errors += "\n"
    try:
        if check_gender(gender) ==True:
            pass
        else:
            raise gender_error()
    except gender_error:
        errors += str(gender_error.error)
        errors += "\n"


    if errors == "":
        try: 
            
            db = pymysql.connect(host="88.88.170.2",  # your host 
                     user="server",       # username
                     passwd="sudoonlineid",     # password
                     db="OnlineID" # name of the database, commented out since I am creating the DB in the string below
                     )   
 
            # Create a Cursor object to execute queries.
            cur = db.cursor()

            add_user = ("INSERT INTO information "
               "(first_name, last_name, adress, adress_number, zip_code, country, birthday, sex, phone_Countrycode, phonenumber, email, hashed_Passwords, salt) "
               "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")

            data_user = (firstname, lastname, adress, adressnumber, postcode, country, birthday, gender, countrycode, phone, email, hashedpassword, passwordsalt)
            
            cur.execute(add_user, data_user)

            db.commit()

            db.close()
            
            checker = True
            return checker
        
        except storage_error:
            #error handling for database storage/user creation here
            pass
    else:
        return checker, errors
        
