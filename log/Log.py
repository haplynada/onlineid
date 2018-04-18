'''
Created on 25. jan. 2018

@author: Tor Larssen Sekse
'''
from database_handling.connect import Connect
import datetime

class Log(object):
    """
    The log class contains methods for log data, logtimes will be set by 
    the __init__, and then the other functions can be called by the code as 
    needed. 
    
    Contains: 
    login_attempt : for log every time a login is either attempted or completed
    login_site : logs which sites are accessed with a timestamp
    """
    
    def __init__(self):
        """
        init sets up the variables used for log and takes a timestamp to be used
        in the log, the time will be specific down to the second and will ignore 
        milliseconds. 
        """
        self.__user_id = None
        self.__ip_adress = None
        self.__site = None
        self.__email = None
        
        #Settings date and time
        self.__temp = (str(datetime.datetime.now())).split(".")
        self.__temp2 = self.__temp[0].split(" ")
        self.__date = str(self.__temp2[0])
        self.__time = str(self.__temp2[1])
        
        #Housekeeping variables for determining what has been logged and is to be stored in database
        self.__login = False
        self.__new_user = False

    def login_attempt(self, user_id, ip_adress):
        """
        The login_attempt method uses a provided user_id and ip adress and
        adds them to the log variables, will be stored 
        
        Args: 
            user_id: string referring to a user_id in the database
            ip_adress: string containing an IP adress
        Returns: 
            None
        """
        self.__user_id = user_id
        self.__ip_adress = ip_adress
        
        self.__login = True # sets housekeeping
        
        
            
    def login_site(self, sitename):
        """
        The login_site method logs the site date and time of any actions. 
        
        Args: 
            site: string containing a sitename 
        Returns: 
            None
        """
        self.__site = sitename
        
    def new_user(self, email, ip_adress):
        """
        Logs the creations of a new user in the database, uses the email provided
        to get the user id out of the database and links that to the email
        in the log
        
        Args: 
            email: string containing email adress
            ip_adress: string containing ip adress
        Returns: 
            None
        """
        self.__email = email
        self.__ip_adress = ip_adress
        
        with Connect() as db: #connecting to database
            #uses email to get user_id
            query = "SELECT user_id from information WHERE email =%s;"
            db.cur.execute(query, self.__email)
            self.__user_id = str(db.cur.fetchone()[0])
            
        self.__new_user = True #sets housekeeping 
    
    
    def user_deletion(self, user_id, ip_adress):
        """
        logs the deletion of a user, also transfer all information about the user to a 
        deleted_users table in the database. 
        """
        self.__user_id = user_id
        self.__ip_adress = ip_adress
        
        
        with Connect() as db: #connecting to database
            #uses user_id to get all user data from information
            query = "SELECT * from information WHERE user_id =%s;"
            db.cur.execute(query, (self.__user_id))
            self.__data = db.cur.fetchall()[0]
        
            #setting variables to data from information query
            self.__first_name = self.__data[0]
            self.__last_name = self.__data[1]
            self.__adress = self.__data[2]
            self.__adress_number = self.__data[3]
            self.__post_code = self.__data[4]
            self.__country = self.__data[5]
            self.__birthday = str(self.__data[6])
            self.__country_code = self.__data[7]
            self.__phone_number = self.__data[8]
            self.__email = self.__data[9]
            self.__gender = self.__data[10]
            
            #copies the users information into the deleted users table
            query = (" INSERT INTO deleted_users"
                        "(first_name, last_name, adress, adress_number, zip_code, country, birthday, sex, phone_Countrycode, phonenumber, email, user_id) "
                        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
            db.cur.execute(query, (self.__email, self.__first_name, self.__last_name, 
                                    self.__phone_number, self.__adress, self.__adress_number, 
                                    self.__post_code, self.__country, self.__country_code,
                                    self.__birthday, self.__gender, self.__user_id))
            db.conn.commit()
            
            #adds the user deletion to the deletion log
            self.__query = (" INSERT INTO deletion_log"
                                "(user_id, email, ip_adress, date, time,)"
                                "VALUES (%s, %s, %s, %s, %s)")
            self.__data = (self.__user_id, self.__email, self.__ip_adress, self.__date, self.__time)
            db.cur.execute(self.__query, self.__data)
            db.conn.commit()
            

    
    def store_in_database(self):
        """
        Stores all loginfo in the active class instacne to the database. 
        
        Args:
            None
        Returns: 
            None
        """
        with Connect() as db: 
            if self.__login == True: #stores login attempt if one has been attempted
                self.__query = (" INSERT INTO activelog"
                            "(user_id, date, time, ip_adress)"
                            "VALUES (%s, %s, %s, %s)")
                self.__data = (self.__user_id, self.__date, self.__time, self.__ip_adress)
                db.cur.execute(self.__query, self.__data)
                db.conn.commit()
                
            if self.__site != None:#stores site if one was connected
                self.__query = (" INSERT INTO activesitelog"
                            "(site, date, time)"
                            "VALUES (%s, %s, %s)")
                self.__data = (self.__site, self.__date, self.__time)
                db.cur.execute(self.__query, self.__data)
                db.conn.commit()
            
            if self.__new_user == True: #stores new user creation log in database
                self.__query = (" INSERT INTO usercreationlog"
                            "(user_id, email, ip_adress, date, time)"
                            "VALUES (%s, %s, %s, %s, %s)")
                self.__data = (self.__user_id, self.__email, self.__ip_adress,self.__date, self.__time)
                db.cur.execute(self.__query, self.__data)
                db.conn.commit()

            
            
            