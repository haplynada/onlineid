'''
Created on 22. feb. 2018

Test implementation of multiprocessing using several ports 

@author: Tor Larssen Sekse
'''

import multiprocessing as mp
from connection_handling.data_handling_userclass import listen_connection
import psutil

ports = [22025,22026,22027,22028,22029,22030,22031,22032]
process_names = ["p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8"]

if __name__ == '__main__':
    #determines the number of cores on the cpu
    cpu_count = psutil.cpu_count(logical=False)
    
    mp.freeze_support()#for windows support
    
    for x in range(0, (cpu_count)):#for each core on the CPU
        #initializes the process with name and port from the lists
        process_names[x] =  mp.Process(target=listen_connection, args=[ports[x],])
        
        process_names[x].start()#starts the process
    
"""
    old code, to be deleted after proper testing!
    p1 = mp.Process(target=listen_connection, args=(22025,))
    p2 = mp.Process(target=listen_connection, args=(22026,))
    p1.start()
    p2.start()
"""