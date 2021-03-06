'''
Created on 5. okt. 2017
authenticate user contains all functions involved in authenticating the user on the server
and the functions involved with handling passwords
@author: Tor Larssen Sekse
'''



import bcrypt


def authenticate_user(email, password):
    """Authenticates the provided email and password with the database
    
    uses the email address to get the userid from the database, then get the hashed password
    from the database and sends those to the authenticate_password function
    
    Args: 
        email: a string containing the users email address
        password: plain text password as a string, as submitted by the user
        
    Returns: 
        True/False depending on whether the user was authenticated or not
    
    """
    user = get_user_id(email)
    hashed_password = get_hashed_Password(user)
    checker = authenticate_password(hashed_password, password)
    return checker

def generate_salt():
    """ generates a random salt
    
    Calls bcrypt to generate a random salt for use in hashing the password
    
    Args: 
        None
        
    Returns: 
        random salt as a string
    """
    salt = bcrypt.gensalt()
    return salt


def authenticate_password(hashed_password, password):
    """authenticates provided password against provided hashed_password
    
    Args: 
        hashed_password: a string containing a hashed password retrieved from the database
        password: string containing submitted password
        
    Returns: 
        True/False depending on whether the user was authenticated or not
    
    """
    checker = False
    if bcrypt.checkpw(password.encode(), hashed_password.encode()):
        checker = True
    else:
        checker = False
    return checker

def hash_password(salt, password):
    """hashes passwords
    
    uses bcrypt to call hashpw to hash password and salt for storage in database 
    
    Args: 
        salt: random generated salt as a string used for making brute 
            forcing the hashed_password harder
        password:a string containing a password as entered by the user
        
    Returns: 
        string containing a hashed_password ready to be stored in the database
    
    """
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password


