'''
Created on 19. okt. 2017

@author: Tor Larssen Sekse
'''
import socket
import ssl
from _socket import SOL_SOCKET, SO_REUSEADDR
from userhandling.authenticateuser import authenticate_user
from userhandling.getuserdata import get_email, get_firstname, get_lastname,\
    get_phonenumber, get_post_code, get_country, get_phone_Country, get_adress,\
    get_adress_number, get_birthday, get_sex, get_all
from Databasehandling.queries import getuser
from userhandling.newuser import create_user
from userhandling.deleteuser import deleteuser

def handle_data(connstream, data):
    decoded_data =data.decode()
    datalist = decoded_data.split("|")
    
    if datalist[0] == "newuser": #Parses the new user from client and add the new user to the database
        del datalist[0]
        if create_user(datalist[0], datalist[1], datalist[2], datalist[3], datalist[4], datalist[5], datalist[6], datalist[7], datalist[8], datalist[9], datalist[10], datalist[11]) ==True:
            return_data=b"newuser|True"
            connstream.send(return_data)
        else:
            errors = create_user(datalist[0], datalist[1], datalist[2], datalist[3], datalist[4], datalist[5], datalist[6], datalist[7], datalist[8], datalist[9], datalist[10], datalist[11])
            return_data= b"newuser|false|" + str(errors).encode()
            connstream.send(return_data)
        
    elif datalist[0] == "login": # 
        del datalist[0]
        if authenticate_user(datalist[0], datalist[1]) == True:
            return_data = b"login|True"
            
            connstream.send(return_data)
            
        else:
            connstream.send(b"login|False")
    
    elif datalist[0] == "edituser":
        del datalist[0]
        
    elif datalist[0] == "getdata":
        del datalist[0]
        if authenticate_user(datalist[0], datalist[1]): 
            user= getuser(datalist[0])
            if datalist[2] == "getfirstname":
                return_data = b"getdata|getfirstname|" + str(get_firstname(user)).encode()
                connstream.send(return_data)
                
            elif datalist[2] == "getlastname": 
                return_data = b"getdata|getlastname|" + str(get_lastname(user)).encode()
                connstream.send(return_data)
                
            elif datalist[2] == "getphone": 
                return_data = b"getdata|getphone|" + str(get_phonenumber(user)).encode()
                connstream.send(return_data)
                
            elif datalist[2] == "getpostcode": 
                return_data = b"getdata|getpostcode|" + str(get_post_code(user)).encode()
                connstream.send(return_data)
                
            elif datalist[2] == "getcountry": 
                return_data = b"getdata|getcouintry|" + str(get_country(user)).encode()
                connstream.send(return_data)
                
            elif datalist[2] == "getcountrycode": 
                return_data = b"getdata|getcountrycode|" + str(get_phone_Country(user)).encode()
                connstream.send(return_data)
                
            elif datalist[2] == "getadress": 
                return_data = b"getdata|getadress|" + str(get_adress(user)).encode()
                connstream.send(return_data)
                
            elif datalist[2] == "getadressnumber": 
                return_data = b"getdata|getadressnumber|" + str(get_adress_number(user)).encode()
                connstream.send(return_data)
                
            elif datalist[2] == "getbirthday": 
                return_data = b"getdata|getbirthday|" + str(get_birthday(user)).encode()
                connstream.send(return_data)
                
            elif datalist[2] == "getgender": 
                return_data = b"getdata|getgender|" + str(get_sex(user)).encode()
                connstream.send(return_data)
        
            else:
                return_data = b"getdata|False|invalidquery"
                connstream.send(return_data)
        else:
            connstream.send(b"getdata|False|invaliduser")
            
    elif datalist[0] == "getalldata":
        del datalist[0]
        if authenticate_user(datalist[0], datalist[1]) == True:
            user = getuser(datalist[0])
            return_data = b"getalldata|True|" + str(get_firstname(user)).encode() + b"|" \
            + str(get_lastname(user)).encode() + b"|" + str(get_phonenumber(user)).encode() + b"|"\
            + str(get_post_code(user)).encode() + b"|" + str(get_country(user)).encode() + b"|"\
            + str(get_phone_Country(user)).encode() + b"|" + str(get_adress(user)).encode() + b"|"\
            + str(get_adress_number(user)).encode() + b"|" + str(get_birthday(user)).encode() + b"|"\
            + str(get_sex(user)).encode()
            connstream.send(return_data)
        else: 
            return_data = b"getalldata|False|invaliduser"
            connstream.send(return_data)
            
    elif datalist[0] == "deleteuser":
        del datalist[0]
        if authenticate_user(datalist[0], datalist[1]):
            user = getuser(datalist[0])
            if deleteuser(user) == True:
                return_data = b"deleteuser|True"
                connstream.send(return_data)
            else:
                return_data = b"deleteuser|False"
                connstream.send(return_data)
        else:
            return_data = b"deleteuser|False|invaliduser"
            connstream.send(return_data)

    else:
        print("fuck")
        print(datalist)
    return False

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
        finally: 
            connstream.shutdown(socket.SHUT_RDWR)
            connstream.close()
listen_connection()