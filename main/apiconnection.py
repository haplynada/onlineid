'''
Created on 19. okt. 2017

@author: Tor Larssen Sekse
'''
import socket
import ssl
from _socket import SOL_SOCKET, SO_REUSEADDR
from userhandling.authenticateuser import authenticate_user

def handle_data(connstream, data):
    decoded_data =data.decode()
    datalist = decoded_data.split("|")
    if datalist[0] == "newuser":
        del datalist[0]
        print(datalist)
    elif datalist[0] == "login":
        del datalist[0]
        print(authenticate_user(datalist[0], datalist[1]))
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