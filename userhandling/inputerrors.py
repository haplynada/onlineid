'''
Created on 9. okt. 2017

@author: Tor Larssen Sekse
'''

class password_error(Exception):
    error = "invalid password"
    pass

class email_error(Exception):
    error = "invalid email"
    pass

class firstname_error(Exception):
    error = "invalid first name"
    pass

class lastname_error(Exception):
    error = "invalid last name"
    pass

class phonenumber_error(Exception):
    error = "invalid phone number"
    pass

class adress_error(Exception):
    error = "invalid adress"
    pass

class postcode_error(Exception):
    error = "invalid postcode"
    pass

class country_error(Exception):
    error = "invalid country"
    pass

class countrycode_error(Exception):
    error = "invalid country code"
    pass

class birthday_error(Exception):
    error = "invalid birthday"
    pass
