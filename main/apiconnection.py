'''
Created on 19. okt. 2017

@author: Tor Larssen Sekse
'''
import socket
import ssl
from _socket import SOL_SOCKET, SO_REUSEADDR

def deal_with_data(connstream, data):
    print(data)
    return False

def do_stuff(connstream):
    data=connstream.read()
    while data:
        if not deal_with_data(connstream, data):
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
            do_stuff(connstream)
        finally: 
            connstream.shutdown(socket.SHUT_RDWR)
            connstream.close()
listen_connection()