'''
Created on 8. feb. 2018

runs the admin tools menu

@author: Tor Larssen Sekse
'''
from admin_tools.company import create_company
from user_handling.Company import Company
from database_handling.connect import Connect


if __name__ == "__main__":
    while True:
        print("Welcome to the admin menu")
    
        print("1. Create a company")
        print("2. Display all unapproved companys")
        print("3. Display all companys")
        print("4. perform action on company id")
        print("'q' for exit")
    
        selection = input("")
    
        if selection == "1":
            create_company()
        
        if selection == "2":
            with Connect() as db: 
                try: 
                    query = "SELECT company_id from company WHERE approved =%s;"
                    db.cur.execute(query, "False")
                    companys = str(db.cur.fetchall())
                    print(companys)
                except TypeError: #if this executes there is no unapproved companys
                    print("All companys are approved")
        
        if selection == "3":
            with Connect() as db: 
                query = "SELECT * from company;"
                db.cur.execute(query)
                companys = str(db.cur.fetchall())
                list = companys.split(")")
                for item in list:
                    print(item)
        
        if selection == "4":
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
                if underselection == "q":
                    break
                 
                
        if selection == "q":
            break
        