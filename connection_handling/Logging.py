'''
Created on 25. jan. 2018

@author: Tor Larssen Sekse
'''
from database_handling.connect import Connect

class Logging(object):
    """
    
    """
    
    def __init__(self):
        """
        
        """
        pass


    def login_attempt(self, user_id, timestamp):
        """
        The login_attempt method uses a provided user_id and timestamps and logs 
        the userid and the time
        
        Args: 
            user_id: int referring to a user_id in the database
            timestamp: timedate object (yyyy-mm-dd-hh-mm-ss)
        Returns: 
            None
        """
        