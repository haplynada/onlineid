'''
Created on 5. okt. 2017

@author: Alexander Mackenzie/ Tor Larssen Sekse
'''
import pymysql

class Connect(object):
    """ Establish a connection to a MySQL database using pyMySQL. 
    The data required to connect is written in the __init__ as of now. 
    (move to an input prompt when starting the server in the future)
    
    Connect takes no arguments and returns nothing on init. 
    
    It's set up to be used in the following way: 
        with Connect() as db: 
    This way it will both connect and disconnect properly form the database. 
    
    """
    
    def __init__(self):
        """
        Establishes a connection to the database and creates a cursor. 
        
        Args: 
            self
        Returns: 
            none
        """
        self.conn = pymysql.connect(host="88.88.170.2",  # your host 
        user="server",       # username
        passwd="sudoonlineid",     # password
        db="OnlineID" # name of the database, commented out since I am creating the DB in the string below
        )
        self.cur = self.conn.cursor() #creates a cursor in the databse
        
    def __enter__(self):
        """
        Returns an active connection to the databse. 
        """
        return Connect()
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Closes active connections
        """
        if self.conn:
            self.conn.close()
            
    def close(self):
        """
        For manually closing connections. 
        (should not be used)
        """
        if self.conn:
            self.conn.close()


