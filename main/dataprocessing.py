'''
Created on 12. okt. 2017

@author: Tor Larssen Sekse
'''
import multiprocessing
import queue
from userhandling.newuser import create_user

#Queues for different actions
newuserqueue = queue.Queue(25)
edituserqueue = queue.Queue(25)
authenticateuserqueue = queue.Queue(25)
deleteuserqueue =queue.Queue(25)

#exitflag for the threads, not sure if we need this or how we are going to use it?
exitflag = False

def 

def handle_input