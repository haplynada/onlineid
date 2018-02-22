'''
Created on 22. feb. 2018

Test implementation of multiprocessing using several ports 

@author: Tor Larssen Sekse
'''

import multiprocessing as mp
from database_handling.connect import Connect
from connection_handling.data_handling_userclass import listen_connection

if __name__ == '__main__':
    mp.freeze_support()
    p1 = mp.Process(target=listen_connection, args=(22025,))
    p2 = mp.Process(target=listen_connection, args=(22026,))

    p1.start()
    p2.start()
