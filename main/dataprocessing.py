'''
Created on 12. okt. 2017

@author: Tor Larssen Sekse
'''
import threading
import queue
from userhandling.newuser import create_user

#Queues for different actions
newuserqueue = queue.Queue(25)
edituserqueue = queue.Queue(25)
authenticateuserqueue = queue.Queue(25)
deleteuserqueue =queue.Queue(25)

#exitflag for the threads, not sure if we need this or how we are going to use it?
exitflag = False


class new_user_thread(threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
    def run(self):
        create_user

class edit_user_thread(threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
    def run(self):
        

class authenticate_user_thread(threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
    def run(self):
           

class delete_user_thread(threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
    def run(self):
        

def handle_input