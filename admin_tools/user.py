'''
Created on 8. feb. 2018

@author: Bjarke Larsen
'''

from user_handling import new_user
from database_handling.connect import Connect


def create_user():
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


def lookup():
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
                        print("\n\nUser credentials:", data[x], "\nUser authentication data:", authentication_data[x])

                except TypeError and IndexError:  # if this executes there is no user with email in the database
                    print("No users in database")
                    pass

        elif selection == "q" or selection == "Q":
            break


def deleteuser():
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


def admin_user():
    while True:

        print("\nUser management:")
        print("1. Create a user")
        print("2. Look up user")
        print("3. Delete user")
        print("Q. Go back")

        selection = input("")

        if selection == "1":
            create_user()
        elif selection == "2":
            lookup()
        elif selection == "3":
            deleteuser()
        elif selection == "q" or selection == "Q":
            break


if __name__ == "__main__":
    while True:
        admin_user()