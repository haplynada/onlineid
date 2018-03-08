'''
Created on 8. feb. 2018

runs the admin tools menu

@author: Tor Larssen Sekse, Bjarke Larsen


Create user
Look up users on email
Search for any given user information


'''
from old.company import admin_company
from old.user import admin_user
from old.test_section import test_menu

if __name__ == "__main__":

    while True:
        print("Welcome to the admin menu\n"
              "1. User administration\n"
              "2. Company administration\n"
              "3. Test section\n"
              "Q. Quit program")

        user = input("")

        if user == "1":
            admin_user()
        elif user == "2":
            admin_company()
        elif user == "3":
            test_menu()
        elif user == "q" or user == "Q":
            break