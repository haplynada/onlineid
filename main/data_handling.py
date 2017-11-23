'''
Created on 12. okt. 2017
The functions contained here connects with the handle_data function in remote_connection. 
These functions contain data parsing and function calls.

@author: Tor Larssen Sekse
'''
from user_handling.change_user_data import change_firstname

def edit_user(datalist):
    """parses client input for a edit user call
    
    Takes an edituser request from the client and parses out what data is to be edited
    and calls the corresponding functions to edit the data in the database
    
    Args: 
        datalist: a list containing keywords and new data values parsed from the client. 
            data format ["email", "password", "edit(datavalue)", "newdata", .....
    
    Returns:
        
    """
      if authenticate_user(datalist[0], datalist[1]) == True: 
            user= get_user(datalist[0])
            del datalist[0]
            del datalist[0]
            return_data = b"edituser"
            while len(datalist) != 0:
                if datalist[0] == "editfirstname":
                    if change_firstname(user, datalist[1]) == True:
                        return_data += b"|editfirstname|True"
                    else:
                         return_data += b"|editfirstname|False"
                
                elif datalist[0] == "editlastname": 
                    return_data += b"|editlastname|True|"
                
                elif datalist[0] == "editphone": 
                    return_data += b"|editphone|True|"
                
                elif datalist[0] == "editpostcode": 
                    return_data += b"|editpostcode|True|" 
                
                elif datalist[0] == "editcountry": 
                    return_data += b"|editcountry|True|" 
                
                elif datalist[0] == "editcountrycode": 
                    return_data += b"|editcountrycode|"
                
                elif datalist[0] == "editadress": 
                    return_data += b"|editadress|"
                
                elif datalist[0] == "editadressnumber": 
                    return_data += b"editadressnumber|"
                
                elif datalist[0] == "editbirthday": 
                    return_data += b"|editbirthday|"
                
                elif datalist[0] == "editgender": 
                    return_data += b"|editgender|"
        
                else:
                    return_data += b"editdata|False|invalidquery"
                del datalist[0]
            connstream.send(return_data)
        else:
            connstream.send(b"editdata|False|invaliduser")