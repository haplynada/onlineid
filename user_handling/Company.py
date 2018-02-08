'''
Created on 8. feb. 2018

@author: Tor Larssen Sekse
'''
from database_handling.connect import Connect
import pyotp

class Company(object):
    """
    
    """

    
    def __init__(self, company_id=None):
        """
        company id should be provided unless you are creating a new company!
        
        Args: 
            company_id:string containing the 16 char company id
        Returns: 
            None if the provided company id does not match one in the database
        """
        #class variables
        self.__company_id = company_id
        self.__is_company = False
        self.__approved = False
        
        #gets all company data from the database if a company id is present
        #if the provided company id is false it will set the is_company variable to False
        if self.__company_id != None:
            try: 
                with Connect() as db: #gets data from the database
                    query = "SELECT * from company WHERE company_id =%s;"
                    db.cur.execute(query, (self.__company_id))
                    self.__data = db.cur.fetchall()[0]
                self.__is_company = True
            except TypeError:#exception to handle if the company id is not in the database
                self.__is_company = False
                return None
            except IndexError:#exception to handle if the company id is not in the database
                self.__is_company = False
                return None
            #sets class variables according to data fomr the database
            self.__approved = self.__data[1]
            self.__company_name = self.__data[2]
            self.__email = self.__data[3]
            self.__contact_person = self.__data[4]
            self.__phone = self.__data[5]
            self.__country = self.__data[6]
            self.__adress = self.__data[7]
            self.__adress_number = self.__data[8]
            
    def get_company_id(self):
        """
        
        """
        return self.__company_id
    
    
    def get_approved(self):
        """
        
        """
        return self.__approved
    
    
    def get_company_name(self):
        """
        
        """
        return self.__company_name
    
    
    def get_email(self):
        """
        
        """
        return self.__email
    
    
    def get_contanct_person(self):
        """
        
        """
        return self.__contact_person
    
    
    def get_phone(self):
        """
        
        """
        return self.__phone
    
    
    def get_country(self):
        """
        
        """
        return self.__country
    
    
    def get_adress(self):
        """
        
        """
        return self.__adress
    
    def get_adress_number(self):
        """
        
        """
        return self.__adress_number
                
    
    def create(self, company_name, email, contact_person, phone, country, adress, adress_number):
        """
        create takes relevant company information as parameters and then stores that 
        information in the database. This method also  generates a company id.
        
        Args: 
            company_name:
            email:
            contact_person:
            phone: 
            country: 
            adress: 
            adress_number: 
        Returns: 
            True
        """
        self.__company_id = pyotp.random_base32()
        with Connect() as db: #checks whether the generated id is unique
            pass
        
        with Connect() as db: #saves infor to database
            self.__query = (" INSERT INTO company"
                            "(company_id, approved, company_name, email, contact_person, phone, country, adress, adress_number)"
                            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
            self.__data = (self.__company_id, "False", company_name, email, contact_person, phone, country, adress, adress_number)
            db.cur.execute(self.__query, self.__data)
            db.conn.commit()
        self.__is_company = True
        return True
            
    def approve(self):
        """
        This method approves an existing company in the database. If the company
        already have approval it does nothing.
        
        Args: 
            None
        Returns: 
            None
        """
        with Connect() as db: #Connects to db and does changes
            query = ("UPDATE company SET"
                            " approved=%s"
                            " WHERE company_id=%s")
            db.cur.execute(query, ("True", self.__company_id))
            db.conn.commit()
            self.__approved = True
        
        
    def disapprove(self):
        """
        This method disapproved an existing company in the database. If the company
        does not have approval, it does nothing
        
        Args: 
            None
        Returns: 
            None
        """
        with Connect() as db: #Connects to db and does changes
            query = ("UPDATE company SET"
                            " approved=%s"
                            " WHERE company_id=%s")
            db.cur.execute(query, ("False", self.__company_id))
            db.conn.commit()
            self.__approved = False
            
            
    def delete(self):
        """
        This method deletes the current instance of company form the database
        
        Args:
            None
        Returns: 
            True when the company is deleted
        """
        with Connect() as db: #Connects of the database
            query = "DELETE FROM company WHERE company_id = %s;"
            db.cur.execute(query, (self.__company_id,))
            db.conn.commit()
        return True