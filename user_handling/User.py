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
from user_handling.input_control import *
import bcrypt
from user_handling import authenticate_user
from user_handling import otp_handling
from test.test_OTP import check_otp

class User(object):
    """The user object gathers all data related to the email and password and
    allows it to be returned or manipulated by the data handling functions. 
    
    commit_changes() needs to be called after edits have been done to ensure
    that changes are committed to the database.
    
    """
    
    
    def __init__(self, email, password, otp=None):
        """
        __init__ takes in the users email and password, tries to match the email
        and email in the database, if the email is present in the database it will
        then grab all data related to that user and add it to internal variables
        
        it also contains the housekeeping variables 
        __is_authenticated which is there to make sure that the user is only
            authenticated once, this is to avoid bcrypt slowing down operations
        __change which is there to track whether changes have been made to data
            so we can avoid unneeded commits to the database
        Args: 
            email: a string containing the users email
            password: a string containing the users password
        Returns: 
            will return None if the email is invalid, in cases the is_user variable
            can be used to verify that the user is not present in the database
        """
        #setting variables using input
        self.__email = email
        self.__password = password
        self.__otp = otp
        #housekeeping variables
        self.__is_authenticated = None
        self.__change = False
        
        with Connect() as db: #connecting to database
            #uses email to get user_id
            try: 
                query = "SELECT user_id from information WHERE email =%s;"
                db.cur.execute(query, self.__email)
                self.__user_id = str(db.cur.fetchone()[0])
                self.__is_user = True #the user is in the database
            except TypeError: #if this executes there is no user with email in the database
                self.__is_user = False
                return None
            #uses user_id to get all user data
            query = "SELECT * from information WHERE user_id =%s;"
            db.cur.execute(query, (self.__user_id))
            self.__data = db.cur.fetchall()[0]

            
        #setting variables to data from query
        self.__first_name = self.__data[0]
        self.__last_name = self.__data[1]
        self.__adress = self.__data[2]
        self.__adress_number = self.__data[3]
        self.__post_code = self.__data[4]
        self.__country = self.__data[5]
        self.__birthday = str(self.__data[6])
        self.__country_code = self.__data[7]
        self.__phone_number = self.__data[8]
        self.__gender = self.__data[10]
        self.__hashed_password = self.__data[11]
        self.__has_2fa = self.__data[12]
        self.__2fa_secret = self.__data[13]
        
        
    def print_data(self):
        """
        testmethod to determine correct operation of the init method
        """
        print(type(self.__data))
        print(self.__email)
        print(self.__password)
        print(self.__first_name)
        print(self.__last_name)
        print(self.__gender)
        print(self.__hashed_password)
        print(self.__birthday)


    def is_user(self):
        """is_user returns True if the user is registered, False if not
        
        Args: 
            None
        Returns: 
            True/False depending on whether the user is registered or not
        
        """
        return self.__is_user


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


    def get_has_2fa(self):
        return self.__has_2fa


    def authenticate(self):
        """Authenticates the active instance of user
        
        also sets the private is_authenticated variable so that the authentication
        olny needs to run once, this is to keep bcrypt from slowing down the program
        with repeated authenticate calls. 
    
        Args: 
            self
        
        Returns: 
            True/False depending on whether the user was authenticated or not
    
    """
        if self.__is_authenticated != None:
            return self.__is_authenticated
        else: 
            if bcrypt.checkpw(self.__password.encode(), self.__hashed_password.encode()):
                if self.__has_2fa == True: 
                    if check_otp(self.__2fa_secret, self.__otp) == True:
                        self.__is_authenticated = True
            else:
                self.__is_authenticated = False
            return self.__is_authenticated
        
        
    def set_email(self, email):
        """
        The set data methods calls the input_control functions corresponding 
        to the data type to be changes and then edits that variable in the 
        active instance of the User class, user.commit_changes needs to be 
        called to save any changes to the database!
        
        Args: 
            self: 
            email: new data
        Returns: 
            True/False depending on whether the changes was successful or not
        """
        if check_email(email) == True:
            self.__email = email
            self.__change = True
            return True
        else:
            return False


    def set_firstname(self, firstname):
        """
        The set data methods calls the input_control functions corresponding 
        to the data type to be changes and then edits that variable in the 
        active instance of the User class, user.commit_changes needs to be 
        called to save any changes to the database!
        
        Args: 
            self: 
            firstname: new data
        Returns: 
            True/False depending on whether the changes was successful or not
        """
        if check_firstname(firstname) == True:
            self.__first_name = firstname
            self.__change = True
            return True
        else:
            return False


    def set_lastname(self, lastname):
        """
        The set data methods calls the input_control functions corresponding 
        to the data type to be changes and then edits that variable in the 
        active instance of the User class, user.commit_changes needs to be 
        called to save any changes to the database!
        
        Args: 
            self: 
            lastname: new data
        Returns: 
            True/False depending on whether the changes was successful or not
        """
        if check_lastname(lastname) == True:
            self.__last_name = lastname
            self.__change = True
            return True
        else: 
            return False


    def set_phonenumber(self, phonenumber):
        """
        The set data methods calls the input_control functions corresponding 
        to the data type to be changes and then edits that variable in the 
        active instance of the User class, user.commit_changes needs to be 
        called to save any changes to the database!
        
        Args: 
            self: 
            phonenumber: new data
        Returns: 
            True/False depending on whether the changes was successful or not
        """
        if check_phonenumber(phonenumber) == True:
            self.__phone_number = phonenumber
            self.__change = True
            return True
        else:
            return False


    def set_adress(self, adress):
        """
        The set data methods calls the input_control functions corresponding 
        to the data type to be changes and then edits that variable in the 
        active instance of the User class, user.commit_changes needs to be 
        called to save any changes to the database!
        
        Args: 
            self: 
            adress: new data
        Returns: 
            True/False depending on whether the changes was successful or not
        """
        if check_adress(adress) == True:
            self.__adress = adress
            self.__change = True
            return True
        else: 
            return False


    def set_adress_number(self, adress_number):
        """
        The set data methods calls the input_control functions corresponding 
        to the data type to be changes and then edits that variable in the 
        active instance of the User class, user.commit_changes needs to be 
        called to save any changes to the database!
        
        Args: 
            self: 
            adress_number: new data
        Returns: 
            True/False depending on whether the changes was successful or not
        """
        if check_adressnumber(adress_number) == True:
            self.__adress_number = adress_number
            self.__change = True
            return True
        else: 
            return False


    def set_postcode(self, postcode):
        """
        The set data methods calls the input_control functions corresponding 
        to the data type to be changes and then edits that variable in the 
        active instance of the User class, user.commit_changes needs to be 
        called to save any changes to the database!
        
        Args: 
            self: 
            postcode: new data
        Returns: 
            True/False depending on whether the changes was successful or not
        """
        if check_postcode(postcode) == True:
            self.__post_code = postcode
            self.__change = True
            return True
        else: 
            return False


    def set_country(self, country):
        """
        The set data methods calls the input_control functions corresponding 
        to the data type to be changes and then edits that variable in the 
        active instance of the User class, user.commit_changes needs to be 
        called to save any changes to the database!
        
        Args: 
            self: 
            country: new data
        Returns: 
            True/False depending on whether the changes was successful or not
        """
        if check_country(country) == True:
            self.__country = country
            self.__change = True
            return True
        else: 
            return False


    def set_country_code(self, country_code):
        """
        The set data methods calls the input_control functions corresponding 
        to the data type to be changes and then edits that variable in the 
        active instance of the User class, user.commit_changes needs to be 
        called to save any changes to the database!
        
        Args: 
            self: 
            country_code: new data
        Returns: 
            True/False depending on whether the changes was successful or not
        """
        if check_countrycode(country_code) == True:
            self.__country_code = country_code
            self.__change = True
            return True
        else: 
            return False


    def set_birthday(self, birthday):
        """
        The set data methods calls the input_control functions corresponding 
        to the data type to be changes and then edits that variable in the 
        active instance of the User class, user.commit_changes needs to be 
        called to save any changes to the database!
        
        Args: 
            self: 
            birthday: new data
        Returns: 
            True/False depending on whether the changes was successful or not
        """
        if check_birthday(birthday) == True:
            self.__birthday = birthday
            self.__change = True
            return True
        else: 
            return False


    def set_gender(self, gender):
        """
        The set data methods calls the input_control functions corresponding 
        to the data type to be changes and then edits that variable in the 
        active instance of the User class, user.commit_changes needs to be 
        called to save any changes to the database!
        
        Args: 
            self: 
            gender: new data
        Returns: 
            True/False depending on whether the changes was successful or not
        """
        if check_gender(gender) == True:
            self.__gender = gender
            self.__change = True
            return True
        else: 
            return False


    def set_password(self, password):
        """
        The set data methods calls the input_control functions corresponding 
        to the data type to be changes and then edits that variable in the 
        active instance of the User class, user.commit_changes needs to be 
        called to save any changes to the database!
        When the password is changed, a new salt is also generated for the user
        
        Args: 
            self: 
            email: new data
        Returns: 
            True/False depending on whether the changes was successful or not
        """
        if self.authenticate() == True:
            if check_password(password) == True:
                password_salt = authenticate_user.generate_salt()
                hashed_password = authenticate_user.hash_password(password_salt, password)
                self.__hashed_password = hashed_password
                self.__change = True
                return True
        else:
            return False


    def commit_changes(self):
        """
        This method only executes if any changes have been done to self by the
        user. If changes have been made it will authenticate the user, 
        if the user is authenticated. All variables will be committed to the 
        database as they are. Changes will then be committed. 
        
        Args: 
            None
        Returns: 
            True/False depending on whether data was committed or not
        """
        
        if self.__change == True: #checks for changes
            if self.authenticate() == True: #authenticates user
                with Connect() as db: #connects to the database
                    query = ("UPDATE information SET"
                            " email=%s"
                            ", first_name=%s"
                            ", last_name=%s"
                            ", phoneNumber=%s"
                            ", adress=%s"
                            ", adress_number=%s"
                            ", zip_code=%s"
                            ", country=%s"
                            ", phone_Countrycode=%s"
                            ", birthday=%s"
                            ", sex=%s"
                            ", hashed_passwords=%s" 
                            " WHERE user_id=%s")
                    db.cur.execute(query, (self.__email, self.__first_name, self.__last_name, 
                                           self.__phone_number, self.__adress, self.__adress_number, 
                                           self.__post_code, self.__country, self.__country_code,
                                           self.__birthday, self.__gender, self.__hashed_password,
                                           self.__user_id))
                    db.conn.commit()
                    return True
        else:
            return False


    def delete(self):
        """Deletes the active instance of user from the database. 
            THIS IS NOT REVERSIBLE!
            THE DATA WILL BE GONE FROM THE DATABASE!
        
        Args: 
            None
        Returns: 
            True when the user is deleted
        """
        with Connect() as db: #Connects of the database
            query = "DELETE FROM information WHERE user_id = %s;"
            db.cur.execute(query, (self.__user_id,))
            db.conn.commit()
            return True
    
    

        
        
        