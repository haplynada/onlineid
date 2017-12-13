'''
Created on 13. des. 2017

@author: Tor Larssen Sekse
'''

from user_handling.get_user_data import get_all, get_firstname
from user_handling.User import User
import timeit


user = User("sau@sau.no", "koktsau42")

if user.is_user():
    user.print_data()
    print(timeit.timeit(user.authenticate, number=1))
    if user.authenticate():
        print("yay")
    print(timeit.timeit(user.authenticate, number=1))
    print(user.authenticate())
    print(timeit.timeit(user.authenticate, number=1))
    print(timeit.timeit(user.authenticate, number=1))
    user.set_adress_number("43")
    user.commit_changes() 
else:
    print("user not registered")

