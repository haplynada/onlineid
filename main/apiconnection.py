'''
Created on 19. okt. 2017

@author: Tor Larssen Sekse
'''
import socket, _ssl

def listen_connection():
    listener = socket.socket()
    host = socket.gethostname()
    port = 22025
    listener.bind((host, port))
    
    listener.listen(10)
    while True:
        c, addr = listener.accept()
        print(addr)
        c.send("thank you for connecting")
        c.close
        
listen_connection()