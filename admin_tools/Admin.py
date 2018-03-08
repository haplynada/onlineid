'''
Created on 8. March 2018

@author: Bjarke Larsen, Tor Larssen Sekse
'''

import pymysql
from user_handling import new_user
from user_handling.User import User
from user_handling.Company import Company
from database_handling.connect import Connect
from test.test_OTP import menu as otp_menu


class Admin(object):
    """

    """

    def __init__(self, user, password):
        self.__user = user
        self.__password = password

        self.conn = pymysql.connect(host="88.88.170.2",  # your host
                                    user="server",  # username
                                    passwd="sudoonlineid",  # password
                                    db="admin"
                                    # name of the database, commented out since I am creating the DB in the string below
                                    )
        self.cur = self.conn.cursor()  # creates a cursor in the databse
        query = "select password from admins where user_name =%s;"
        self.cur.execute(query, user)
        stored_password = str(self.cur.fetchone()[0])

        if self.__password == stored_password:
            self.__main_menu()


    def __main_menu(self):
        while True:
            print("\n ADMIN TOOL\n"
              "1. User administration\n"
              "2. Company administration\n"
              "3. Test section\n"
              "Q. Quit program")

            user = input("")

            if user == "1":
                self.__admin_user()
            elif user == "2":
                self.__admin_company()
            elif user == "3":
                self.__test_menu()
            elif user == "q" or user == "Q":
                quit()


    def __admin_user(self):
        while True:

            print("\nUser management:\n"
                  "1. Create a user\n"
                  "2. Look up user\n"
                  "3. Edit user\n"
                  "4. Delete user\n"
                  "Q. Go back\n")

            selection = input("")

            if selection == "1":
                self.__create_user()
            elif selection == "2":
                self.__lookup_user()
            elif selection == "3":
                self.__edit_user()
            elif selection == "4":
                self.__delete_user()
            elif selection == "q" or selection == "Q":
                break


    def __create_user(self):
        print("\n Create user")
        email = input("Enter email: ")
        password = input("Enter password (numbers and letters): ")
        firstname = input("Enter firstname: ")
        lastname = input("Enter lastname: ")
        phone = input("Enter phonenumber: ")
        postcode = input("Enter postcode: ")
        country = input("Enter country ")
        countrycode = input("Enter country code (must be 4-digit): ")
        address = input("Enter address (without number): ")
        addressnumber = input("Enter address number: ")
        birthday = input("Enter birthday (year-month-date): ")
        gender = input("Enter gender: ")

        print(new_user.create_user(email, password, firstname, lastname, phone, postcode, country, countrycode, address,
                                   addressnumber, birthday, gender))


    def __lookup_user(self):
        while True:
            print("\nLookup user\n"
                  "1. User-id\n"
                  "2. Email\n"
                  "3. Firstname\n"
                  "4. Lastname\n"
                  "5. All users\n"
                  "Q. Go back")

            selection = input("")

            if selection == "1":
                user_id = input("Enter user_id: ")
                with Connect() as db:  # connecting to database
                    try:
                        query = "SELECT * from information WHERE user_id =%s;"
                        db.cur.execute(query, (user_id))
                        data = db.cur.fetchall()[0]
                        # uses user_id to get all information from authentication
                        query = "SELECT * from authentication WHERE user_id =%s;"
                        db.cur.execute(query, (user_id))
                        authentication_data = db.cur.fetchall()[0]
                        print("\n\nUser credentials:", data, "\nUser authentication data:", authentication_data)
                    except TypeError and IndexError:  # if this executes there is no user with user-id in the database
                        print("No user with that user-id")
                        pass

            elif selection == "2":
                email = input("Enter email: ")
                with Connect() as db:  # connecting to database
                    try:
                        query = "SELECT user_id from information WHERE email =%s;"
                        db.cur.execute(query, email)
                        user_id = db.cur.fetchall()
                        for x in range(len(user_id)):
                            query = "SELECT * from information WHERE user_id =%s;"
                            db.cur.execute(query, user_id[x])
                            data = db.cur.fetchall()
                            query = "SELECT * from authentication WHERE user_id =%s;"
                            db.cur.execute(query, user_id[x])
                            authentication_data = db.cur.fetchall()
                            for x in range(len(data)):
                                print("\n\nUser credentials:", data[x], "\nUser authentication data:",
                                      authentication_data[x])
                    except TypeError and IndexError:  # if this executes there is no user with email in the database
                        print("No user with that email")
                        pass

            elif selection == "3":
                firstname = input("Enter firstname: ")
                with Connect() as db:  # connecting to database
                    try:
                        query = "SELECT user_id from information WHERE first_name =%s;"
                        db.cur.execute(query, firstname)
                        user_id = db.cur.fetchall()
                        for x in range(len(user_id)):
                            query = "SELECT * from information WHERE user_id =%s;"
                            db.cur.execute(query, user_id[x])
                            data = db.cur.fetchall()
                            query = "SELECT * from authentication WHERE user_id =%s;"
                            db.cur.execute(query, user_id[x])
                            authentication_data = db.cur.fetchall()
                            for x in range(len(data)):
                                print("\n\nUser credentials:", data[x], "\nUser authentication data:",
                                      authentication_data[x])
                    except TypeError and IndexError:  # if this executes there is no user with email in the database
                        print("No user with that firstname")
                        pass

            elif selection == "4":
                lastname = input("Enter lastname: ")
                with Connect() as db:  # connecting to database
                    try:
                        query = "SELECT user_id from information WHERE last_name =%s;"
                        db.cur.execute(query, lastname)
                        user_id = db.cur.fetchall()
                        for x in range(len(user_id)):
                            query = "SELECT * from information WHERE user_id =%s;"
                            db.cur.execute(query, user_id[x])
                            data = db.cur.fetchall()
                            query = "SELECT * from authentication WHERE user_id =%s;"
                            db.cur.execute(query, user_id[x])
                            authentication_data = db.cur.fetchall()
                            for x in range(len(data)):
                                print("\n\nUser credentials:", data[x], "\nUser authentication data:",
                                      authentication_data[x])
                    except TypeError and IndexError:  # if this executes there is no user with email in the database
                        print("No user with that lastname")
                        pass

            elif selection == "5":
                with Connect() as db:  # connecting to database
                    try:
                        query = "SELECT * from information;"
                        db.cur.execute(query)
                        data = db.cur.fetchall()
                        query = "SELECT * from authentication;"
                        db.cur.execute(query)
                        authentication_data = db.cur.fetchall()
                        for x in range(len(data)):
                            print("\n\nUser credentials:", data[x], "\nUser authentication data:",
                                  authentication_data[x])

                    except TypeError and IndexError:  # if this executes there is no user with email in the database
                        print("No users in database")
                        pass

            elif selection == "q" or selection == "Q":
                break


    def __edit_user(self):
        print("\nEdit user")
        email = input("Enter email: ")
        password = input("Enter password")
        user = User(email, password)
        while True:
            if user.is_user() == True:
                print("\nWhat would you like to edit? - remember to commit changes!!!:\n"
                      "1. email\n"
                      "2. firstname\n"
                      "3. lastname\n"
                      "4. password\n"
                      "5. phonenumber\n"
                      "6. adress\n"
                      "7. adress number\n"
                      "8. country\n"
                      "9. postcode\n"
                      "10. country code\n"
                      "11. birthday\n"
                      "12. gender\n"
                      "13. Commit changes\n"
                      "Q. Go back - any changes does not get committed\n")
                choice = input("")
                if choice == "1":
                    new_value = input("Enter new value: ")
                    set_new_value = user.set_email(new_value)
                    if set_new_value == True:
                        print("Value changed to", new_value)
                    else:
                        print("New value not valid")
                        continue
                elif choice == "2":
                    new_value = input("Enter new value: ")
                    set_new_value = user.set_firstname(new_value)
                    if set_new_value == True:
                        print("Value changed to", new_value)
                    else:
                        print("New value not valid")
                        continue
                elif choice == "2":
                    new_value = input("Enter new value: ")
                    set_new_value = user.set_firstname(new_value)
                    if set_new_value == True:
                        print("Value changed to", new_value)
                    else:
                        print("New value not valid")
                        continue
                elif choice == "3":
                    new_value = input("Enter new value: ")
                    set_new_value = user.set_lastname(new_value)
                    if set_new_value == True:
                        print("Value changed to", new_value)
                    else:
                        print("New value not valid")
                        continue
                elif choice == "4":
                    new_value = input("Enter new value: ")
                    set_new_value = user.set_password(new_value)
                    if set_new_value == True:
                        print("Value changed to", new_value)
                    else:
                        print("New value not valid")
                        continue
                elif choice == "5":
                    new_value = input("Enter new value: ")
                    set_new_value = user.set_phonenumber(new_value)
                    if set_new_value == True:
                        print("Value changed to", new_value)
                    else:
                        print("New value not valid")
                        continue
                elif choice == "6":
                    new_value = input("Enter new value: ")
                    set_new_value = user.set_adress(new_value)
                    if set_new_value == True:
                        print("Value changed to", new_value)
                    else:
                        print("New value not valid")
                        continue
                elif choice == "7":
                    new_value = input("Enter new value: ")
                    set_new_value = user.set_adress_number(new_value)
                    if set_new_value == True:
                        print("Value changed to", new_value)
                    else:
                        print("New value not valid")
                        continue
                elif choice == "8":
                    new_value = input("Enter new value: ")
                    set_new_value = user.set_country(new_value)
                    if set_new_value == True:
                        print("Value changed to", new_value)
                    else:
                        print("New value not valid")
                        continue
                elif choice == "9":
                    new_value = input("Enter new value: ")
                    country = user.get_country()
                    set_new_value = user.set_postcode(country, new_value)
                    if set_new_value == True:
                        print("Value changed to", new_value)
                    else:
                        print("New value not valid")
                        continue
                elif choice == "10":
                    new_value = input("Enter new value: ")
                    country = user.get_country()
                    set_new_value = user.set_country_code(country, new_value)
                    if set_new_value == True:
                        print("Value changed to", new_value)
                    else:
                        print("New value not valid")
                        continue
                elif choice == "11":
                    new_value = input("Enter new value: ")
                    set_new_value = user.set_birthday(new_value)
                    if set_new_value == True:
                        print("Value changed to", new_value)
                    else:
                        print("New value not valid")
                        continue
                elif choice == "12":
                    new_value = input("Enter new value: ")
                    set_new_value = user.set_gender(new_value)
                    if set_new_value == True:
                        print("Value changed to", new_value)
                    else:
                        print("New value not valid")
                        continue
                elif choice == "13":
                    commit = user.commit_changes()
                    if commit == True:
                        print("Changes have been committed")
                        break
                    else:
                        print("Changes have not been committed")
                        break
                elif choice == "q" or choice == "Q":
                    break
            else:
                print("Invalid user or password")
                break


    def __delete_user(self):
        print("Delete user\n"
              "Enter user-id:")
        user_id = input("")
        with Connect() as db:  # Connects of the database
            query = "DELETE FROM information WHERE user_id = %s;"
            db.cur.execute(query, user_id)
            db.conn.commit()

            query = "DELETE FROM authentication WHERE user_id = %s;"
            db.cur.execute(query, user_id)
            db.conn.commit()
            print("User", user_id, "deleted")


    def __admin_company(self):
        while True:

            print("\nCompany management:"
                  "\n1. Create a company"
                  "\n2. Display all unapproved companies"
                  "\n3. Display all companies"
                  "\n4. Perform action on company id"
                  "\nQ. Go back")
            selection = input("")

            if selection == "1":
                self.__create_company()

            elif selection == "2":
                with Connect() as db:
                    try:
                        query = "SELECT company_id from company WHERE approved =%s;"
                        db.cur.execute(query, "False")
                        companys = str(db.cur.fetchall())
                        print(companys)
                    except TypeError:  # if this executes there is no unapproved companies
                        print("All companies are approved")

            elif selection == "3":
                with Connect() as db:
                    query = "SELECT * from company;"
                    db.cur.execute(query)
                    companies = str(db.cur.fetchall())
                    list = companies.split(")")
                    for item in list:
                        print(item)

            elif selection == "4":
                company_id = input("Please enter company id: ")
                company = Company(company_id)
                while True:
                    print("1. Approve")
                    print("2. Disapprove")
                    print("3. Delete")
                    print("4. Display company information")
                    print("q to quit")
                    underselection = input("")
                    if underselection == "1":
                        company.approve()
                    if underselection == "2":
                        company.disapprove()
                    if underselection == "3":
                        company.delete()
                    if underselection == "4":
                        company_data = [company.get_company_id(), company.get_approved(),
                                        company.get_company_name(), company.get_email(),
                                        company.get_contanct_person(), company.get_phone(),
                                        company.get_country(), company.get_adress(),
                                        company.get_adress_number()]
                        print(company_data)
                    if underselection == "q" or underselection == "Q":
                        break

            elif selection == "q" or selection == "Q":
                break


    def __create_company(self):
        print("\nCreate company")

        company_name = input("Enter company name: ")
        email = input("Enter company email: ")
        contact_person = input("Enter company contact person: ")
        phone = input("Enter company phone number: ")
        country = input("Enter company country: ")
        adress = input("Enter company adress: ")
        adress_number = input("Enter company adress_number: ")

        new_company = Company()
        new_company.create(company_name, email, contact_person, phone, country, adress, adress_number)


    def __approve_company(company):
        company.approve()


    def __disapprove_company(company):
        company.disapprove()


    def __delete_company(company):
        company.delete()


    def __test_menu(self):
        while True:

            print("\nTest section:\n"
                  "1. Test OTP\n"
                  "Q. Go back")
            selection = input("")

            if selection == "1":
                otp_menu()
            elif selection == "2":
                pass
            elif selection == "3":
                pass
            elif selection == "q" or selection == "Q":
                break


if __name__ == "__main__":

    while True:
        print("Admin tool login")
        user_name = input("Enter username:")
        password = input("Enter password")

        try:
            Admin(user_name, password)
        except TypeError:
            print("\nWrong username or password\n")
