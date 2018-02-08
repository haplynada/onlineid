'''
Created on 8. feb. 2018

@author: Tor Larssen Sekse
'''

from user_handling.Company import Company

def create_company():
    print("Welcome to create a company")
    
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