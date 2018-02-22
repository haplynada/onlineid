'''
Created on 5. okt. 2017

@author: Tor Larssen Sekse, Bjarke Larsen
'''
validchars_email = set('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.-_ @')
validchars_name = set('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ')
genders = ["Male", "Female", "Other", "male", "female", "other"]
#countries = ["norway", "sweden", "denmark", "iceland", "united states", "england", "great britain", \
             #"germany",]
#countrycodes = ["0047", "0046", "0045", "00354", "0111", "0044", "0049"]

import datetime
import os
import pandas as pd
from datetime import date
from database_handling.connect import Connect


def check_password(password):
    password_length = len(password)
    if password_length >= 8  and (any(char.isdigit() for char in password)) and password_length <=15: 
        return True
    else:
        return False


def check_email(email):
    if set(email).issubset(validchars_email):
        if "@" in email: 
            if "." in email:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

    
def check_firstname(name):
    if set(name).issubset(validchars_name):
        return True
    else:
        return False


def check_lastname(name):
    if set(name).issubset(validchars_name):
        return True
    else:
        return False


def check_phonenumber(phone):
    phone = phone.replace(" ", "")
    phone_length = len(phone)
    if phone_length == 8 and (phone.isdigit()):  
        return True
    else: 
        return False


def check_adress(adress):
    if set(adress).issubset(validchars_email):
        return True
    else:
        return False


def check_adressnumber(adressnumber):
    if adressnumber.isdigit():
        return True
    else:
        return False


def check_postcode(country_provided: str, post_code: str):
    """ Checks the postcode for the given country.

    Looks in a excel-file, with the given country name, and searches for the post-code.
    Finds the excel-file in the standard python directory, for the given client.

    Args:
        country_provided: Used to find the given excel-file, with the country name.
        post_code: Used to look in the given file, and find a comparison.

    Returns:
        Returns True if the provided post-code is found in the excel-file for the given country.
        Else returns False.

    """
    p_dir = os.getcwd()
    country = country_provided.capitalize()
    path = p_dir + "/country_and_zip_code/" + country + ".xlsx"
    df = pd.read_excel(path)

    query = "zip_code == ['"+post_code+"']"
    code = df.query(query).head()
    code_string = str(code)
    zip_code = (code_string.strip(" ")).split(" ")
    try:

        if zip_code[(len(zip_code)-3)] == post_code:
            return True
        else:
            return False
    except IndexError:
        return False


def check_country(country_provided: str):
    """ Checks the given country is supported.

    Looks in a excel-file, with supported countries. If the country provided exists then it returns True.
    Finds the excel-file in the standard python directory, for the given client.

    Args:
        country_provided: Used to search in the excel-file, with supported countries.

    Returns:
        Returns True if the provided country matches one in the excel-file.
        Else returns False.

    """
    p_dir = os.getcwd()
    file_path = p_dir + "/country_and_zip_code/country_codes.xlsx"
    df = pd.read_excel(file_path)

    country_comp = country_provided.capitalize()
    guery_text = "country == ['" + country_comp + "']"
    query = str(guery_text)
    code = df.query(query).head()
    code_string = str(code)
    country = code_string.split(" ")
    try:
        if country[7] == country_comp:
            return True
        else:
            return False
    except IndexError:
        return False


def check_countrycode(country_provided: str, country_code: str):
    """ Checks the country code for the given country.

    Looks in a excel-file, with supported countries. Finds the country and the country code.
    Finds the excel-file in the standard python directory, for the given client.

    Args:
        country_provided: Used to search in the excel-file, with supported countries.
        country_code: Used to compare the provided country code with the one found in the excel-file.

    Returns:
        Returns True if the provided country-code is found in the excel-file.
        Else it returns False.

    """
    p_dir = os.getcwd()
    file_path = p_dir + "/country_and_zip_code/country_codes.xlsx"
    df = pd.read_excel(file_path)
    country_comp = country_provided.capitalize()
    guery_text = "country == ['" + country_comp + "']"
    query = str(guery_text)
    code = df.query(query).head()
    code_string = str(code)
    country_found = code_string.split(" ")
    try:
        country_code_found = country_found[18]
        while len(country_code_found) < 4:
            country_code_found = "0" + country_code_found
        if country_code_found == country_code:
            return True
        else:
            return False
    except IndexError:
        return False


def check_birthday(birthday):
    try:
        if birthday != datetime.datetime.strptime(birthday, "%Y-%m-%d").strftime('%Y-%m-%d'):
            raise ValueError
        return True
    except ValueError:
        return False


def check_age(birthday):
    birthday_datetime = datetime.datetime.strptime(birthday, "%Y-%m-%d")
    today = date.today()
    if 13 <= (today.year - birthday_datetime.year -  ((today.month, today.day) < (birthday_datetime.month, birthday_datetime.day))):
        return True
    else:
        return False


def check_gender(gender):
    if gender in genders:
        return True
    else:
        return False


def check_email_database(email):
    try: 
        with Connect() as db:
            query = "SELECT user_id from information WHERE email =%s;"
            db.cur.execute(query, email)
            result = str(db.cur.fetchone()[0])
            
            return False
    except TypeError:
        return True