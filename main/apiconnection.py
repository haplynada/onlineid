'''
Created on 19. okt. 2017

@author: Tor Larssen Sekse
'''
import socket
import ssl
from _socket import SOL_SOCKET, SO_REUSEADDR
from userhandling.authenticateuser import authenticate_user
import userhandling.getuserdata
from userhandling.getuserdata import get_email, get_firstname, get_lastname
from Databasehandling.queries import getuser
from userhandling.newuser import create_user

def handle_data(connstream, data):
    decoded_data =data.decode()
    datalist = decoded_data.split("|")
    
    if datalist[0] == "newuser": #Parses the new user from client and add the new user to the database
        del datalist[0]
        if create_user(datalist[0], datalist[1], datalist[2], datalist[3], datalist[4], datalist[5], datalist[6], datalist[7], datalist[8], datalist[9], datalist[10], datalist[11]) ==True:
            return_data="newuser|True"
            return_data.encode(encoding='utf_8')
            connstream.send(return_data)
        else:
            return_data="newuser|False"
            return_data.encode(encoding='utf_8')
            connstream.send(return_data)
        
    elif datalist[0] == "login": # 
        del datalist[0]
        if authenticate_user(datalist[0], datalist[1]) == True:
            return_data = b"login|True"
            
            connstream.send(return_data)
            return True
        else:
            return False
        print(authenticate_user(datalist[0], datalist[1]))
    
    elif datalist[0] == "edituser":
        del datalist[0]
        
    elif datalist[0] == "getdata":
        del datalist[0]
        
        if datalist[0] == "getfirstname":
            del datalist[0]
            user= getuser(datalist[0])
            return_data = "getdata|firstname|" + str(get_firstname(user))
            return_data.encode(encoding='utf_8')
            connstream.send(return_data)
            return True
        
        elif datalist[0] == "getlastname": 
            del datalist[0]
            user = getuser(datalist[0])
            user = get_lastname(user)
            return_data = "getdata|lastname|" + str(get_lastname(user))
            return_data.encode(encoding='utf_8')
            connstream.send(return_data)
            return True
        elif datalist[0] == "":
            pass
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