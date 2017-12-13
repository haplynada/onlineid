'''
Created on 12. okt. 2017
The functions contained here connects with the handle_data function in remote_connection. 
These functions contain data parsing and function calls.

@author: Tor Larssen Sekse
'''
from user_handling.change_user_data import change_firstname, change_lastname,\
    change_phonenumber, change_post_code, change_country, change_countrycode,\
    change_adress, change_adress_number, change_birthday, change_gender, change_password
from user_handling.get_user_data import get_user_id
from user_handling.authenticate_user import authenticate_user

def edit_user(datalist):
    """parses client input for a edit user call
    
    Takes an edituser request from the client and parses out what data is to be edited
    and calls the corresponding functions to edit the data in the database
    
    Args: 
        datalist: a list containing keywords and new data values parsed from the client. 
            data format ["email", "password", "edit(datavalue)", "newdata", .....
    
    Returns:
        a byte string with information about how the editdata processes went. 
            format: b"editdata|False|invaliduser"
                    b"edituser|editfirstname|True"
    """
    if authenticate_user(datalist[0], datalist[1]) == True: 
        user_id= get_user_id(datalist[0])
        del datalist[0]
        del datalist[0]
        return_data = b"edituser"
        while len(datalist) != 0:
            
            if datalist[0] == "editfirstname":
                if change_firstname(user_id, datalist[1]) == True:
                    return_data += b"|editfirstname|True"
                else:
                    return_data += b"|editfirstname|False"
                
            elif datalist[0] == "editlastname": 
                if change_lastname(user_id, datalist[1]) == True:
                    return_data += b"|editlastname|True"
                else: 
                    return_data += b"|editlastname|False"
                
            elif datalist[0] == "editphone": 
                if change_phonenumber(user_id, datalist[1]) == True:
                    return_data += b"|editphone|True"
                else:
                    return_data += b"|editphone|False"
                
            elif datalist[0] == "editpostcode": 
                if change_post_code(user_id, datalist[1]) == True:
                    return_data += b"|editpostcode|True" 
                else: 
                    return_data += b"|editpostcode|False" 
                
            elif datalist[0] == "editcountry": 
                if change_country(user_id, datalist[1]) == True:
                    return_data += b"|editcountry|True" 
                else:
                    return_data += b"|editcountry|False" 
                
            elif datalist[0] == "editcountrycode": 
                if change_countrycode(user_id, datalist[1]) == True:
                    return_data += b"|editcountrycode|True"
                else:
                    return_data += b"|editcountrycode|False"
                
            elif datalist[0] == "editadress": 
                if change_adress(user_id, datalist[1]) == True:
                    return_data += b"|editadress|True"
                else: 
                    return_data += b"|editadress|False"
                    
            elif datalist[0] == "editadressnumber": 
                if change_adress_number(user_id, datalist[1]) == True:
                    return_data += b"editadressnumber|True"
                else: 
                    return_data += b"editadressnumber|False"
                
            elif datalist[0] == "editbirthday": 
                if change_birthday(user_id, datalist[1]) == True:
                    return_data += b"|editbirthday|True"
                else:
                    return_data += b"|editbirthday|False"
                
            elif datalist[0] == "editgender": 
                if change_gender(user_id, datalist[1]) == True:
                    return_data += b"|editgender|True"
                else: 
                    return_data += b"|editgender|False"
                    
            elif datalist[0] == "editpassword":
                if change_password(user_id, datalist[1]) == True:
                    return_data += b"|editpassword|True"
                else: 
                    return_data += b"editpassword|False"
        
            else:
                return_data += b"editdata|False|invalidquery"
            del datalist[0]
            del datalist[0]
        return return_data
    else:
        return b"editdata|False|invaliduser"