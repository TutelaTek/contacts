from flask import Blueprint, request

import mysql.connector

contact = Blueprint('contact', __name__)


db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "RunningMan2001!",
    database ="contactlist"
)



mycursor = db.cursor()


@contact.route('/contacts', methods=['GET'])
def viewContacts():

  
      

    mycursor.execute('''SELECT * FROM contacts''')
    data = mycursor.fetchall()
    if len(data) < 1:
        return "no data"

    return str(data[0:5])

    






@contact.route('/create-contact', methods=['Post'])
def createContact():

    fname = request.form.get('fname')
    lname = request.form.get('lname')
    phone = request.form.get('phone')
    email = request.form.get('email')  

    try:
        mycursor.execute("INSERT INTO  contacts (firstName, lastName, phone, email) VALUES (%s, %s, %s, %s);", (fname, lname, phone, email))
        db.commit()
    except:
        return 'error'


    return 'contact created'





@contact.route('/edit-contact', methods=['PUT'])
def editContact():

    fname = request.form.get('fname')
    lname = request.form.get('lname')
    phone = request.form.get('phone')
    email = request.form.get('email') 
    id = request.form.get('id')
    
    try:
        mycursor.execute("UPDATE contacts SET firstName = %s, lastName = %s, phone = %s, email = %s WHERE id = %s;", (fname, lname, phone, email, id))
        db.commit()
    except:
        return 'error'
    


    return 'contact updated'









@contact.route('/delete-contact', methods=['DELETE'])
def deleteContact():

    contactID = request.form.get('id')
    print(contactID)
    int(contactID)
    mycursor.execute("DELETE FROM contacts WHERE id = %s;", (contactID,))
    db.commit()
    


    return 'contact deleted'
