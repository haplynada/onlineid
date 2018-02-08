'''
Created on 8. feb. 2018

runs the admin tools menu

@author: Tor Larssen Sekse, Bjarke Larsen


Create user
Look up users on email
Search for any given user information


'''
from admin_tools.company import admin_company
from admin_tools.user import admin_user








if __name__ == "__main__":
    while True:
        print("Welcome to the admin menu")
        print("1. User administration\n"
              "2. Company administration\n"
              "Q. Quit program")
        user = input("\nChoice: ")

        if user == "1":
            admin_user()
        elif user == "2":
            admin_company()