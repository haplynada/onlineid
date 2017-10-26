'''
Created on 19. okt. 2017

@author: Tor Larssen Sekse
'''
import socket, ssl

sender = socket.socket()
host = socket.gethostname()
sender_ssl = ssl.wrap_socket(sender)

sender_ssl.connect((host, 22025))

print(sender_ssl.getpeername())


sender_ssl.write("login|Hans@hansen.dk|K234Jdfhen".encode(encoding='utf_8'))

sender_ssl.close()

