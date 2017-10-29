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

def handle_data(connstream, data):
    decoded_data =data.decode()
    datalist = decoded_data.split("|")
    if datalist[0] == "newuser":
        del datalist[0]
        print(datalist)
    elif datalist[0] == "login":
        del datalist[0]
        if authenticate_user(datalist[0], datalist[1]) == True:
            return_data = "login|True"
            return_data.encode(encoding='utf_8')
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
        elif datalist[0] == ""
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