'''
Created on 11. apr. 2018

@author: Tor Larssen Sekse
'''

import multiprocessing as mp
import psutil
import socket
import ssl
from _socket import SOL_SOCKET, SO_REUSEADDR
from connection_handling.data_handling_userclass import handle_data

mp.allow_connection_pickling()#allows putting sockets in a multiprocessing queue

#SSL Settings
context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile ="server.pem")
context.options = ssl.OP_NO_TLSv1
context.set_ciphers('EECDH+AESGCM:EDH+AESGCM:AES256+EECDH:AES256+EDH')

#creating dictionary for login authentication
authenticated_logins = {}

def receive_data(queue): 
    """
    receive data taks inn a connection, and reads data from
    the connection until there is data present. When it detects data it will
    start the data processing. 
    
    Args: 
        connstream: connection object
    Returns: 
        None
    """  

    while True:
        print(mp.current_process())
        print(authenticated_logins)
        sock = queue.get()
        print(sock.getpeername())
        try: 
            connstream =context.wrap_socket(sock, server_side=True)
        except ssl.SSLError as e:#prints error to console and closes
            print(e)
            connstream.close()
            break
        print(connstream.cipher())
        data=connstream.read()
        while data:
            if not handle_data(connstream, data, authenticated_logins):
                connstream.close()
                break
            data=connstream.read()


def listen(port=22025):
    """
   
    """
    sock = socket.socket()
    host = socket.gethostname()
    port = port
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind((host, port))
    
    
    
    sock.listen(10)
    while True:
        #accepting connection
        newsocket,fromaddr =sock.accept()
        
        #print("putting" + str(newsocket.getpeername()))#print for testing
        
        queue.put(newsocket)#adding connection to processing queue
        
        




if __name__ == '__main__':
    #allows sending sockets between processes
    
    #determines the number of cores on the cpu -1(1 for listener the rest for pool)
    cpu_count = psutil.cpu_count(logical=False) 
    
    #sets up the queue
    queue = mp.Queue(50)
    
    
    mp.freeze_support()#for windows support
    
    #starting worker process pool
    pool = mp.Pool(cpu_count, receive_data,(queue,))
    
    listen()#starts the server listening
    
    