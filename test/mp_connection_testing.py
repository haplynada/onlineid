'''
Created on 22. feb. 2018

@author: Tor Larssen Sekse
'''

import multiprocessing as mp
import socket, ssl
import timeit

# testdata
send_data = b"newuser|sau@sau.no|koktsau42|Sau|Sausen|12398456|2520|Norway|0047|Faareveien|42|2004-01-01|female"
send_data2 = b"getdata|sau@sau.no|koktsau42|getfirstname"
send_login = b"login|sau@sau.no|koktsau42| |WDM3DLKT5V5ZTO7W"
send_deleteuser = b"deleteuser|sau@sauene.no|koktsau42"
send_getall = b"getalldata|sau@sau.no|koktsau42"
send_edituser = b"edituser|sau@sau.no|koktsau42|editfirstname|Sau"
send_changepassword = b"edituser|sau@sau.no|koktsau42|editpassword|koktsau42"


# testdata end

def connect(data, port=22025):
    sender = socket.socket()
    host = socket.gethostname()
    sender_ssl = ssl.wrap_socket(sender)

    sender_ssl.connect(("88.91.35.168", port))

    print(sender_ssl.getpeername())

    sender_ssl.send(data)
    print(sender_ssl.recv().decode())

    sender_ssl.close()
    
if __name__ == '__main__':
    mp.freeze_support()
    p1 = mp.Process(target=connect, args=(send_data, 22025))
    p2 = mp.Process(target=connect, args=(send_login,22026))
    
    p1.start()
    p2.start()
    p1.join()
    p2.join()