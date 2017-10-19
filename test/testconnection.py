'''
Created on 19. okt. 2017

@author: Tor Larssen Sekse
'''
import socket, _ssl

sender = socket.socket()
host = socket.gethostname()

sender.connect((host, 22025))

sender.close()