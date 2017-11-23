'''
Created on 5. okt. 2017

@author: Tor Larssen Sekse, Bjarke
'''
from user_handling.authenticate_user import hash_password,generate_salt
from user_handling.input_control import *
from user_handling.input_errors import *
from database_handling.connect import *
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
            raise PasswordError()
    except PasswordError:
        errors += str(PasswordError.error)
        errors += "\n"
        
    try:
        if check_email(email) == True:
            pass
        else:
            raise EmailError()
    except EmailError:
        errors += str(EmailError.error)
        errors += "\n"

    try:
        if check_email_database(email) == True:
            pass
        else:
            raise EmailDatabaseError()
    except EmailDatabaseError:
        errors += str(EmailDatabaseError.error)
        errors += "\n"
        
    try:
        if check_firstname(firstname) ==True:
            pass
        else:
            raise FirstnameError()
    except FirstnameError:
        errors += str(FirstnameError.error)
        errors += "\n"
        
    try:
        if check_lastname(lastname) ==True:
            pass
        else:
            raise LastnameError()
    except LastnameError:
        errors += str(LastnameError.error)
        errors += "\n"
        
    try:
        if check_phonenumber(phone) ==True:
            pass
        else:
            raise PhonenumberError()
    except PhonenumberError:
        errors += str(PhonenumberError.error)
        errors += "\n"
        
    try:
        if check_adress(adress) ==True:
            pass
        else:
            raise AdressError()
    except AdressError:
        errors += str(AdressError.error)
        errors += "\n"
        
    try:
        if check_adressnumber(adressnumber) ==True:
            pass
        else:
            raise AdressnumberError()
    except AdressnumberError:
        errors += str(AdressnumberError.error)
        errors += "\n"
        
    try:
        if check_postcode(postcode) ==True:
            pass
        else:
            raise PostcodeError()
    except PostcodeError:
        errors += str(PostcodeError.error)
        errors += "\n"
        
    try:
        if check_country(country) ==True:
            pass
        else:
            raise CountryError()
    except CountryError:
        errors += str(CountryError.error)
        errors += "\n"
        
    try:
        if check_countrycode(countrycode) ==True:
            pass
        else:
            raise CountrycodeError()
    except CountrycodeError:
        errors += str(CountrycodeError.error)
        errors += "\n"
        
    try:
        if check_birthday(birthday) ==True:
            pass
        else:
            raise BirthdayError()
    except BirthdayError:
        errors += str(BirthdayError.error)
        errors += "\n"
    try:
        if check_age(birthday) ==True:
            pass
        else:
            raise AgeError()
    except AgeError:
        errors += str(AgeError.error)
        errors += "\n"
        
    try:
        if check_gender(gender) ==True:
            pass
        else:
            raise GenderError()
    except GenderError:
        errors += str(GenderError.error)
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
        
