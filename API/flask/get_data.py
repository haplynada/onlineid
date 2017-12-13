from flask import Flask, render_template,request
import socket, ssl

# Connect to the database
def connect(new_user):
    sender = socket.socket()
    host = socket.gethostname()
    sender_ssl = ssl.wrap_socket(sender)

    sender_ssl.connect(("88.88.170.2", 22025))

    print(sender_ssl.getpeername())

    sender_ssl.send(new_user)
    print(sender_ssl.recv().decode())

    sender_ssl.close()



@app.route("/get-reg")
def login():
    return render_template('reg.html')

@app.route('/save-post',methods=['POST', 'GET'])
def signUp():
    if request.method=='POST':
        firstname=request.form['firstname']
        lastname=request.form['lastname']
        address=request.form['address']
        adressnumber=request.form['addressnumber']
        zipcode=request.form['zipcode']
        country=request.form['country']
        countrycode=request.form['countrycode']
        sex=request.form['sex']
        email=request.form['email']
        birthday=request.form['birthday']
        phone=request.form['phone']
        pwd=request.form['psw']
        newuser = "newuser"
        
        format_send = newuser +"|"+ email +"|"+ pwd +"|"+ firstname +"|"+ lastname +"|"+ phone +"|"+ zipcode +"|"+ country +"|"+ countrycode +"|"+ address +"|"+ adressnumber +"|"+ birthday +"|"+ sex
        
        send = format_send.encode("utf-8")
        connect(send)  
signUp()