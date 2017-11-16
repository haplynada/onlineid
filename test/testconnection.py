'''
Created on 19. okt. 2017

@author: Tor Larssen Sekse
'''
'''
data used for testing purposes
=b"newuser|sau@sau.no|koktsau42|Sau|Sausen|12398456|2520|Norway|0047|Faareveien|42|2017-01-01|female"
'''
import socket, ssl
import timeit

#testdata
send_data =b"newuser|sausau@sau.no|koktsau42|Sau|Sausen|12398456|2520|Norway|0047|Faareveien|42|2004-01-01|female"
send_data2 =b"getdata|sau@sau.no|koktsau42|getgender"
send_login =b"login|sau@sau.no|koktsau42"
send_deleteuser =b"deleteuser|sau@sau.no|koktsau42"
send_getall = b"getalldata|sau@sau.no|koktsau42"
#testdata end

def connect():
    sender = socket.socket()
    host = socket.gethostname()
    sender_ssl = ssl.wrap_socket(sender)

    sender_ssl.connect(("88.88.170.2", 22025))

    print(sender_ssl.getpeername())


    sender_ssl.send(send_data)
    print(sender_ssl.recv().decode())

    sender_ssl.close()

print(timeit.timeit(connect, number = 1))