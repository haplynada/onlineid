'''
Created on 13. des. 2017

@author: Tor Larssen Sekse
'''

from user_handling.get_user_data import get_all, get_firstname
from user_handling.User import User
import timeit
import time



def create_object():
    user = User("sau@sau.no", "koktsau43")
    if user.is_user():
        user.print_data()
        print("time: " + str(timeit.timeit(user.authenticate, number=1)))
    if user.authenticate():
        print("yay")
        print(timeit.timeit(user.authenticate, number=1))
        print(user.authenticate())
        print(timeit.timeit(user.authenticate, number=1))
        print(timeit.timeit(user.authenticate, number=1))
        user.set_adress_number("42")
        user.set_password("koktsau43")
        print(timeit.timeit(user.commit_changes, number = 1))
    else:
        print("user not registered")

print("total time" + str(timeit.timeit(create_object, number=1)))
"""
if user.is_user():
    user.print_data()
    print(timeit.timeit(user.authenticate, number=1))
    if user.authenticate():
        print("yay")
    print(timeit.timeit(user.authenticate, number=1))
    print(user.authenticate())
    print(timeit.timeit(user.authenticate, number=1))
    print(timeit.timeit(user.authenticate, number=1))
    user.set_adress_number("42")
    print(timeit.timeit(user.commit_changes, number = 1))
else:
    print("user not registered")
"""
