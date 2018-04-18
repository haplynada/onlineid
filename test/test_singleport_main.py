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

mp.allow_connection_pickling()

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
        
        newsocket = queue.get()
        print(newsocket.getpeername())
        connstream =ssl.wrap_socket(newsocket, server_side=True, certfile="server.pem")
        print(connstream.getpeercert())
        data=connstream.read()
        while data:
            if not handle_data(connstream, data):
                break
            data=connstream.read()


def listen(port=22025):
    """
   
    """
    listener = socket.socket()
    host = socket.gethostname()
    port = port
    listener.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    listener.bind((host, port))
    
    
    
    listener.listen(10)
    while True:
        #accepting connection
        newsocket, fromaddr =listener.accept()
        
        print("putting" + str(newsocket.getpeername()))
        
        queue.put(newsocket)#adding connection to processing queue
        print(queue)




if __name__ == '__main__':
    #allows sending sockets between processes
    
    #determines the number of cores on the cpu
    cpu_count = psutil.cpu_count(logical=False) -1
    
    #sets up the queue
    queue = mp.Queue(50)
    
    
    mp.freeze_support()#for windows support
    
    pool = mp.Pool(cpu_count, receive_data,(queue,))
    
    
    print(queue)
    listen()
    
    