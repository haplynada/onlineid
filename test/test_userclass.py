'''
Created on 13. des. 2017

@author: Tor Larssen Sekse
'''

from user_handling.get_user_data import get_all, get_firstname
from user_handling.User import User

user = User("sau@sau.no", "koktsau42")
user.print_data()