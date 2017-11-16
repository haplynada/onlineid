'''
Created on 9. okt. 2017

@author: Tor Larssen Sekse
'''

class PasswordError(Exception):
    error = "invalid password"
    pass

class EmailError(Exception):
    error = "invalid email"
    pass
class EmailDatabaseError(Exception):
    error = "email already in database"
    pass

class FirstnameError(Exception):
    error = "invalid first name"
    pass

class LastnameError(Exception):
    error = "invalid last name"
    pass

class PhonenumberError(Exception):
    error = "invalid phone number"
    pass

class AdressError(Exception):
    error = "invalid adress"
    pass

class AdressnumberError(Exception):
    error = "Invalid adress number"
    pass

class PostcodeError(Exception):
    error = "invalid postcode"
    pass

class CountryError(Exception):
    error = "invalid country"
    pass

class CountrycodeError(Exception):
    error = "invalid country code"
    pass

class BirthdayError(Exception):
    error = "invalid birthday"
    pass

class AgeError(Exception):
    error = "User not yet 13 years old"

class GenderError(Exception):
    error = "invalid gender"
    pass
