'''
Created on Oct 19, 2017

@author: Bjarke Larsen
'''
from user_handling.get_user_data import get_all, get_firstname, get_lastname, get_adress,\
    get_adress_number, get_post_code, get_country, get_birthday, get_sex,\
    get_phone_Country, get_phonenumber, get_email, get_hashed_Password,\
    get_salt

user_id = 1



try:
    print("First name is:", (get_firstname(user_id)))
    print("Last name is:", (get_lastname(user_id)))
    print("Adress is:", (get_adress(user_id)))
    print("Adress-number is:", (get_adress_number(user_id)))
    print("Zip-Code is:", (get_post_code(user_id)))
    print("Country is:", (get_country(user_id)))
    print("Birthday is:", (get_birthday(user_id)))
    print("Sex is:", (get_sex(user_id)))
    print("Country code is:", (get_phone_Country(user_id)))
    print("Phone-number is:", (get_phonenumber(user_id)))
    print("Email is:", (get_email(user_id)))
    print("Hashed password is:", (get_hashed_Password(user_id)))
    print("Salt is:", (get_salt(user_id)))
    print("all info;", (get_all(user_id)))
except SyntaxError:
    print("yay")
