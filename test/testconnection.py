'''
Created on 19. okt. 2017

@author: Tor Larssen Sekse
'''
from time import sleep
from _socket import SHUT_RDWR
'''
data used for testing purposes
=b"newuser|sau@sau.no|koktsau42|Sau|Sausen|12398456|2520|Norway|0047|Faareveien|42|2017-01-01|female"
'''
import socket, ssl
import timeit
from random import randint

# testdata
send_data = b"newuser|sau@sau.no|koktsau42|Sau|Sausen|12398456|2520|Norway|0047|Faareveien|42|2004-01-01|female"
send_data2 = b"getdata|sau@sau.no|koktsau42|getfirstname"
send_login = b"login|sau@sau.no|koktsau42| |WDM3DLKT5V5ZTO7W|token"
send_deleteuser = b"deleteuser|sau@sauene.no|koktsau42"
send_getall = b"getalldata|sau@sau.no|koktsau42"
send_edituser = b"edituser|sau@sau.no|koktsau42|editfirstname|Sau"
send_changepassword = b"edituser|sau@sau.no|koktsau42|editpassword|koktsau42"


# testdata end

def connect():
    sender = socket.socket()
    host = socket.gethostname()
    sender_ssl = ssl.wrap_socket(sender)
    
    port=22025
    
         
    sender_ssl.connect(("88.91.35.168", port))

    print(sender_ssl.getpeername())

    sender_ssl.send(send_login)
    print(sender_ssl.recv().decode())
    
    sender_ssl.shutdown(SHUT_RDWR)
    sender_ssl.close()
    
    
    sender = socket.socket()
    host = socket.gethostname()
    sender_ssl = ssl.wrap_socket(sender)
    
    port=22025
    sender_ssl.connect(("88.91.35.168", port))
    
    sender_ssl.send(b"confirm|token")
    print(sender_ssl.recv().decode())

    sender_ssl.close()


print(timeit.timeit(connect, number=1))
