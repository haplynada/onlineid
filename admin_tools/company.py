'''
Created on 8. feb. 2018

@author: Tor Larssen Sekse, Bjarke Larsen
'''

from user_handling.Company import Company
from database_handling.connect import Connect

def create_company():
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
    

    
def approve_company(company):
    company.approve()

def disapprove_company(company):
    company.disapprove()

def admin_company():
    while True:

        print("\nCompany management:")
        print("1. Create a company")
        print("2. Display all unapproved companies")
        print("3. Display all companies")
        print("4. Perform action on company id")
        print("Q. Go back")

        selection = input("")

        if selection == "1":
            create_company()

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


if __name__ == "__main__":
    while True:
        admin_company()