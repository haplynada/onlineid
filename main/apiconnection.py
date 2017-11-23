'''
Created on 19. okt. 2017

@author: Tor Larssen Sekse
'''
import socket
import ssl
from _socket import SOL_SOCKET, SO_REUSEADDR
from user_handling.authenticate_user import authenticate_user
from user_handling.get_user_data import get_email, get_firstname, get_lastname,\
    get_phonenumber, get_post_code, get_country, get_phone_Country, get_adress,\
    get_adress_number, get_birthday, get_sex
from database_handling.queries import get_user
from user_handling.new_user import create_user
from user_handling.delete_user import delete_user

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
            user= get_user(datalist[0])
            del datalist[0]
            del datalist[0]
            return_data = b"getdata"
            while len(datalist) != 0:
                if datalist[0] == "getfirstname":
                    return_data += b"|getfirstname|" + str(get_firstname(user)).encode()
                
                elif datalist[0] == "getlastname": 
                    return_data = b"|getlastname|" + str(get_lastname(user)).encode()
                
                elif datalist[0] == "getphone": 
                    return_data = b"|getphone|" + str(get_phonenumber(user)).encode()
                
                elif datalist[0] == "getpostcode": 
                    return_data = b"|getpostcode|" + str(get_post_code(user)).encode()
                
                elif datalist[0] == "getcountry": 
                    return_data = b"|getcountry|" + str(get_country(user)).encode()
                
                elif datalist[0] == "getcountrycode": 
                    return_data = b"|getcountrycode|" + str(get_phone_Country(user)).encode()
                
                elif datalist[0] == "getadress": 
                    return_data = b"|getadress|" + str(get_adress(user)).encode()
                
                elif datalist[0] == "getadressnumber": 
                    return_data = b"getadressnumber|" + str(get_adress_number(user)).encode()
                
                elif datalist[0] == "getbirthday": 
                    return_data = b"|getbirthday|" + str(get_birthday(user)).encode()
                
                elif datalist[0] == "getgender": 
                    return_data = b"|getgender|" + str(get_sex(user)).encode()
        
                else:
                    return_data = b"getdata|False|invalidquery"
                del datalist[0]
            connstream.send(return_data)
        else:
            connstream.send(b"getdata|False|invaliduser")
            
    elif datalist[0] == "getalldata":
        del datalist[0]
        if authenticate_user(datalist[0], datalist[1]) == True:
            user = get_user(datalist[0])
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
            user = get_user(datalist[0])
            if delete_user(user) == True:
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