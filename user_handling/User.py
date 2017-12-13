'''
Created on 13. des. 2017

        __first_name
        __last_name
        __adress
        __adress_number
        __post_code
        __country
        __country_code
        __birthday
        __gender
        __hashed_password

@author: Tor Larssen Sekse
'''
from database_handling.connect import Connect
from user_handling.get_user_data import get_user_id, get_all

class User(object):
    """
    
    """

    
    def __init__(self, email, password):
        """
        
        """
        self.__email = email
        self.__password = password
        with Connect() as db: 
            #uses email to get user_id
            query = "SELECT user_id from information WHERE email =%s;"
            db.cur.execute(query, self.__email)
            self.__user_id = str(db.cur.fetchone()[0])
            #uses user_id to get all user data
            query = "SELECT * from information WHERE user_id =%s;"
            db.cur.execute(query, (self.__user_id))
            self.__data = str(db.cur.fetchall()[0])
            
        self.__first_name = self.__data[0]
        self.__last_name = self.__data[1]
        self.__adress = self.__data[2]
        self.__adress_number = self.__data[3]
        self.__post_code = self.__data[4]
        self.__country = self.__data[5]
        self.__birthday = str(self.__data[6])
        self.__country_code = self.__data[7]
        self.__phone_number = self.__data[8]
        self.__gender = self.__data[11]
        self.__hashed_password = self.__data[12]
        
    def print_data(self):
        print(type(self.__data))
        print(self.__email)
        print(self.__password)
        print(self.__first_name)
        print(self.__last_name)
        
    def get_firstname(self):
        return self.__first_name
    
    def get_lastname(self):
        return self.__last_name
    
    def get_adress(self):
        return self.__adress
    
    def get_adress_number(self):
        return self.__adress_number
    
    def get_post_code(self):
        return self.__post_code
    
    def get_country(self):
        return self.__country
    
    def get_birthday(self):
        return self.__birthday
    
    def get_gender(self):
        return self.__gender
    
    def get_phone_country(self):
        return self.__country_code
    
    def get_phonenumber(self):
        return self.__phone_number
    
    def get_hashed_password(self):
        return self.__hashed_password
    
    def get_email(self):
        return self.__email
    
    
    
    
    
    

        
        
        