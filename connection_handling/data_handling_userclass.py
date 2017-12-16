'''
Created on 14. des. 2017
Dataformats: 
    all data sendt to the server over the secure socket should be in the following formats
Login: 
    To server: login|email|password
    From server: login|boolean

Getdata
    To server: getdata|email|password|(getdatatype ex:getfirstname)|additionaldatatype|...
    From server: getdata|(getdatatype ex:getfirstname)|data|additionalreturndata|...
    Error: getdata|False|reason

Getalldata
    To server: getalldata|email|password
    From server: getalldata|True|firstname|lastname|phone|postcode|country|countrycode|adress|adressnumber|birthday|gender
    Error: 
    getalldata|False|reason

Newuser
    To server: newuser|email|password|firstname|lastname|phone|postcode|country|countrycode|adress|adressnumber|birthday|gender
    From server: newuser|boolean|reason

Edituser
    To server: edituser|email|password|(editdatatype ex:editfirstname)|newdata|additionaleditdatatype|additionalnewdata|...
    From server: edituser|boolean|reason

Deleteuser:
    To server: deleteuser|email|password
    From server: deleteuser|boolean|reason

@author: Tor Larssen Sekse
'''
import socket
import ssl
from _socket import SOL_SOCKET, SO_REUSEADDR
from user_handling.new_user import create_user
from user_handling.User import User

def handle_data(connstream, data):
    """
    Handle data receives a string sent from the client over secure sockets, parses
    the string into keyqords, and calls methods from the User class and other 
    functions, to process the requests from the client. 
    
    Args: 
        Connstream:a secure sockets connection to the client 
        data: a string containing the data received from the client
    Returns: 
        False when done, handle_data sends the result from the data processing 
        back to the client before it returns False. 
    
    """
    #
    decoded_data =data.decode()
    datalist = decoded_data.split("|")
    
    user = User(datalist[1], datalist[2]) #setting up the user object
    
    if datalist[0] == "newuser": #Parses the new user from client and add the new user to the database
        del datalist[0]
        #creates a new user with the provided data
        if create_user(datalist[0], datalist[1], datalist[2], datalist[3], datalist[4], datalist[5], datalist[6], datalist[7], datalist[8], datalist[9], datalist[10], datalist[11]) ==True:
            return_data=b"newuser|True"
            connstream.send(return_data)
        else: #returns errors if user creation failed
            errors = create_user(datalist[0], datalist[1], datalist[2], datalist[3], datalist[4], datalist[5], datalist[6], datalist[7], datalist[8], datalist[9], datalist[10], datalist[11])
            return_data= b"newuser|false|" + str(errors).encode()
            connstream.send(return_data)
        
    elif datalist[0] == "login": # parses a login request from the client 
        if user.authenticate() == True: #authenticates the user
            return_data = b"login|True"
            connstream.send(return_data)
            
        else:
            connstream.send(b"login|False")
    
    elif datalist[0] == "edituser":#parses an edituser request from the client
        return_data = edit_user(user, datalist)
        connstream.send(return_data)
        
    elif datalist[0] == "getdata":#parses a get request from the client
        return_data = get_data(user, datalist)
        connstream.send(return_data) 
            
    elif datalist[0] == "getalldata":#parses a getall request from client
        #authenticates the user and returns all available data to the client
        #if the user is authenticated
        if user.authenticate() == True:
            return_data = b"getalldata|True|" + str(user.get_firstname()).encode() + b"|" \
            + str(user.get_lastname()).encode() + b"|" + str(user.get_phonenumber()).encode() + b"|"\
            + str(user.get_post_code()).encode() + b"|" + str(user.get_country()).encode() + b"|"\
            + str(user.get_phone_country()).encode() + b"|" + str(user.get_adress()).encode() + b"|"\
            + str(user.get_adress_number()).encode() + b"|" + str(user.get_birthday()).encode() + b"|"\
            + str(user.get_gender()).encode()
            connstream.send(return_data)
        else: #returns a error message if the user is not authenticated
            return_data = b"getalldata|False|invaliduser"
            connstream.send(return_data)
            
    elif datalist[0] == "deleteuser":#parses a deleteuser request from client
        if user.authenticate() == True:#authenticates the user
            if user.delete() == True:#deletes all data about the active user from the databse
                return_data = b"deleteuser|True"
                connstream.send(return_data)
            else:
                return_data = b"deleteuser|False"
                connstream.send(return_data)
        else:
            return_data = b"deleteuser|False|invaliduser"
            connstream.send(return_data)

    return False

def get_data(user, datalist):
    """parses client input for a get data call
    
    takes a getdata request from the client and parses out what data is requested
    calls on methods in the user object to return the requested data
        
    Args: 
        user: initilized user object
        datalist: a list containing keywords for the data requested form client
            data format ["email", "password", "get(datavalue)", .....
    
    Returns:
        a byte string with the requested data 
    """
    del datalist[0]
    del datalist[0]
    del datalist[0]
    if user.authenticate()== True: 
        return_data = b"getdata"
        while len(datalist) != 0:
            if datalist[0] == "getfirstname":
                return_data += b"|getfirstname|" + str(user.get_firstname()).encode()
                
            elif datalist[0] == "getlastname": 
                return_data += b"|getlastname|" + str(user.get_lastname()).encode()
                
            elif datalist[0] == "getphone": 
                return_data += b"|getphone|" + str(user.get_phonenumber()).encode()
                
            elif datalist[0] == "getpostcode": 
                return_data += b"|getpostcode|" + str(user.get_post_code()).encode()
                
            elif datalist[0] == "getcountry": 
                return_data += b"|getcountry|" + str(user.get_country()).encode()
                
            elif datalist[0] == "getcountrycode": 
                return_data += b"|getcountrycode|" + str(user.get_phone_country()).encode()
                
            elif datalist[0] == "getaddress": 
                return_data += b"|getaddress|" + str(user.get_adress()).encode()
                
            elif datalist[0] == "getadressnumber": 
                return_data += b"getadressnumber|" + str(user.get_adress_number()).encode()
                
            elif datalist[0] == "getbirthday": 
                return_data += b"|getbirthday|" + str(user.get_birthday()).encode()
                
            elif datalist[0] == "getgender": 
                return_data += b"|getgender|" + str(user.get_gender()).encode()
    
            else:
                return_data += b"getdata|False|invalidquery"
            del datalist[0]
        return return_data
    else:
        return b"getdata|False|invaliduser"
            
def edit_user(user, datalist):
    """parses client input for a edit user call
    
    Takes an edituser request from the client and parses out what data is to be edited
    and calls the corresponding methods in the user object
    
    Args: 
        user: initilized user object
        datalist: a list containing keywords and new data values parsed from the client. 
            data format ["email", "password", "edit(datavalue)", "newdata", .....
    
    Returns:
        a byte string with information about how the editdata processes went. 
            format: b"editdata|False|invaliduser"
                    b"edituser|editfirstname|True"
    """
    del datalist[0]
    del datalist[0]
    del datalist[0]
    if user.authenticate() == True: 
        
        return_data = b"edituser"
        while len(datalist) != 0:#while there is data to process, processes data
            
            if datalist[0] == "editfirstname":
                if user.set_firstname(datalist[1]) == True:
                    return_data += b"|editfirstname|True"
                else:
                    return_data += b"|editfirstname|False"
                
            elif datalist[0] == "editlastname": 
                if user.set_lastname(datalist[1]) == True:
                    return_data += b"|editlastname|True"
                else: 
                    return_data += b"|editlastname|False"
                
            elif datalist[0] == "editphone": 
                if user.set_phonenumber(datalist[1]) == True:
                    return_data += b"|editphone|True"
                else:
                    return_data += b"|editphone|False"
                
            elif datalist[0] == "editpostcode": 
                if user.set_postcode(datalist[1]) == True:
                    return_data += b"|editpostcode|True" 
                else: 
                    return_data += b"|editpostcode|False" 
                
            elif datalist[0] == "editcountry": 
                if user.set_country(datalist[1]) == True:
                    return_data += b"|editcountry|True" 
                else:
                    return_data += b"|editcountry|False" 
                
            elif datalist[0] == "editcountrycode": 
                if user.set_phone_country(datalist[1]) == True:
                    return_data += b"|editcountrycode|True"
                else:
                    return_data += b"|editcountrycode|False"
                
            elif datalist[0] == "editadress": 
                if user.set_adress(datalist[1]) == True:
                    return_data += b"|editadress|True"
                else: 
                    return_data += b"|editadress|False"
                    
            elif datalist[0] == "editadressnumber": 
                if user.set_adress_number(datalist[1]) == True:
                    return_data += b"editadressnumber|True"
                else: 
                    return_data += b"editadressnumber|False"
                
            elif datalist[0] == "editbirthday": 
                if user.set_birthday(datalist[1]) == True:
                    return_data += b"|editbirthday|True"
                else:
                    return_data += b"|editbirthday|False"
                
            elif datalist[0] == "editgender": 
                if user.set_gender(datalist[1]) == True:
                    return_data += b"|editgender|True"
                else: 
                    return_data += b"|editgender|False"
                    
            elif datalist[0] == "editpassword":
                if user.set_password(datalist[1]) == True:
                    return_data += b"|editpassword|True"
                else: 
                    return_data += b"editpassword|False"
        
            else:
                return_data += b"editdata|False|invalidquery"
            del datalist[0]
            del datalist[0]
        return return_data
    else:
        return b"editdata|False|invaliduser"

def receive_data(connstream):   
    data=connstream.read()
    while data:
        if not handle_data(connstream, data):
            break
        data=connstream.read()

def listen_connection():
    
    listener = socket.socket()
    host = socket.gethostname()
    port = 22025
    listener.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    listener.bind((host, port))
    
    listener.listen(10)
    while True:
        newsocket, fromaddr =listener.accept()
        connstream =ssl.wrap_socket(newsocket, server_side=True, certfile="server.pem")
        
        try: 
            receive_data(connstream)
            #Prints the IP and port when a connection is established
            print(str(connstream.getpeername()) + " Connected")
            print(str(connstream.getpeercert()))
            print(connstream.cipher())
            #end of print block for testing
        finally: 
            #prints the IP and port when a connection is closed
            print(str(connstream.getpeername()) + "Disconnected")
            connstream.shutdown(socket.SHUT_RDWR)
            connstream.close()
listen_connection()