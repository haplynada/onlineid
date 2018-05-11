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



def receive_data(queue, authenticated_logins): 
    """
    get socket connection objects from queue, wraps them in an SSL layer
    and recieves data, and then sends that data on to data processing
    
    Args: 
        queue: queue containing active socket connections
        authenticated_logins: managed dict containing (token:login string)
    Returns: 
        None
    """  
    print(mp.current_process())#Printing the name of processes when they start
    while True:#mainloop

        sock = queue.get()#gets socket from queue
        print(sock.getpeername())#testprint
        try: #exception handling for SSLError(connection not wrapping properly)
            connstream =context.wrap_socket(sock, server_side=True)
        except ssl.SSLError as e:#prints error to console and closes connection
            print(e)
            connstream.close()
            break
        
        data=connstream.read()#reads data sent to server
        while data:#while server receives data
            #handles data and closes the connection when done
            if not handle_data(connstream, data, authenticated_logins):
                connstream.close()
                break
            data=connstream.read()#reads data sent to server


def listen(port=22025):
    """
        listen, is the function that runs the socket server towards the outside world
        it will set up a listen on the provided port, accept connections and
        put those connections in the mp.queue to be handled by the worker 
        processes. 
        
        Listen does not transmit anything back to the source, nor receive
        any kind of confirmation that the workers are done. 
       Args: 
            port: what port the server listens on
        Returns: 
            None
    """
    #socket setup and settings
    sock = socket.socket()
    host = socket.gethostname()
    port = port
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind((host, port))
    
    sock.listen(10)
    while True:
        newsocket,fromaddr =sock.accept()#accepting connection
        
        queue.put(newsocket)#adding connection to processing queue



if __name__ == '__main__':
    mp.freeze_support()#for windows support
    
    #creating dictionary for login authentication
    manager = mp.Manager()
    authenticated_logins = manager.dict()
    
    #determines the number of cores on the cpu -1(1 for listener the rest for pool)
    cpu_count = psutil.cpu_count(logical=False) 
    
    #sets up the queue
    queue = mp.Queue(50)
    
    #starting worker process pool
    pool = mp.Pool(cpu_count, receive_data,(queue, authenticated_logins,))
    
    listen()#starts the server listening
    
    