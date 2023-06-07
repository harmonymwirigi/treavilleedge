from treaville import db, login_manager
from flask_login import UserMixin
from flask import session
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    if 'user_type' in session:
        if session["user_type"] == "client":
            return Client.query.get(int(user_id))
        if session["user_type"] == "transporter":
            return Transporter.query.get(int(user_id))
    
class Transporter(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(20), nullable=False)
    company_name = db.Column(db.String(20), nullable=False)
    Id_number = db.Column(db.String(20), nullable=False)
    email_adress = db.Column(db.String(20), nullable=False, unique = True)
    login_password = db.Column(db.String(20), nullable=False)
    owner_mobile = db.Column(db.String(20), nullable=False)
    alt_mobile = db.Column(db.String(20), nullable=False)
    requestscargo = db.relationship('Bookingcargo', backref = 'cargorequests')
    requestspassenger = db.relationship('Bookingpassenger', backref = 'cargorequests')
    requestsConstraction = db.relationship('Bookingconstraction', backref = 'cargorequests')
    vehicle = db.relationship('Vehicle', backref ='my_vehicle', lazy = True)


class Client(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(20), nullable=False)
    company_name = db.Column(db.String(20), nullable=False)
    id_number = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(20), nullable=False, unique = True)
    aop = db.Column(db.String(20), nullable=False)
    city = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    mobile_number = db.Column(db.String(20), nullable=False)
    alt_mobile_number = db.Column(db.String(20), nullable=False)
    bookingcargo = db.relationship('Bookingcargo', backref ='clientCargo', lazy = True)
    bookingpassenger = db.relationship('Bookingpassenger', backref ='clientPassenger', lazy = True)
    bookingconstruction = db.relationship('Bookingconstraction', backref ='clientConstraction', lazy = True)


class Bookingcargo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    my_id = db.Column(db.String(30), unique = True)
    name_of_client = db.Column(db.String(20), nullable=False)
    company = db.Column(db.String(20))
    email = db.Column(db.String(20), nullable=False)
    mobile_number  = db.Column(db.String(20), nullable=False)
    alt_mobile_number = db.Column(db.String(20))
    pickup_location = db.Column(db.String(20), nullable=False)
    delivery_destination = db.Column(db.String(20), nullable=False)
    vehicle_type = db.Column(db.String(20), nullable=False)
    cargo_type = db.Column(db.String(20), nullable=False)
    cargo_wight = db.Column(db.String(20), nullable=False)
    cargo_volume = db.Column(db.String(20), nullable=False)
    date_made = db.Column(db.DateTime, nullable = False, default = datetime.utcnow())
    offer_amount = db.Column(db.String(20), nullable=False)
    my_client = db.Column(db.Integer, db.ForeignKey('client.id'))
    my_transpoter = db.Column(db.Integer, db.ForeignKey('transporter.id'))

class Bookingpassenger(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    my_id = db.Column(db.String(30), unique = True)
    full_name = db.Column(db.String(20), nullable=False)
    company_name = db.Column(db.String(20))
    email = db.Column(db.String(20), nullable=False)
    mobile_number = db.Column(db.String(20), nullable=False)
    alt_number = db.Column(db.String(20))
    pickup_location = db.Column(db.String(20), nullable=False)
    Destination = db.Column(db.String(20), nullable=False)
    vehicle_type = db.Column(db.String(20), nullable=False)
    no_of_passenger = db.Column(db.String(20), nullable=False)
    date_made = db.Column(db.DateTime, nullable = False, default = datetime.utcnow())
    offer_amount = db.Column(db.String(20), nullable=False)
    my_client = db.Column(db.Integer, db.ForeignKey('client.id'))
    my_transpoter = db.Column(db.Integer, db.ForeignKey('transporter.id'))

class Bookingconstraction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    my_id = db.Column(db.String(30), unique = True)
    full_name = db.Column(db.String(20), nullable=False)
    company_name = db.Column(db.String(20))
    email = db.Column(db.String(20), nullable=False)
    mobile_number = db.Column(db.String(20), nullable=False)
    alt_number = db.Column(db.String(20))
    location = db.Column(db.String(20), nullable=False)
    vehicle_type = db.Column(db.String(20), nullable=False)
    date_made = db.Column(db.DateTime, nullable = False, default = datetime.utcnow())
    offer_amount = db.Column(db.String(20), nullable=False)
    my_client = db.Column(db.Integer, db.ForeignKey('client.id'))
    my_transpoter = db.Column(db.Integer, db.ForeignKey('transporter.id'))


    

class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vehicle_type = db.Column(db.String(20), nullable=False)
    driver_name = db.Column(db.String(20), nullable=False)
    driver_id = db.Column(db.String(20), nullable=False ,unique = True)
    driver_no =db.Column(db.String(20), nullable=False)
    alt_no = db.Column(db.String(20), nullable=False)
    payment_account = db.Column(db.String(20), nullable=False)
    account_name = db.Column(db.String(20), nullable=False)
    band_branch_name = db.Column(db.String(20), nullable=False)
    aop = db.Column(db.String(20), nullable=False)
    town = db.Column(db.String(20), nullable=False)
    log_book = db.Column(db.LargeBinary, nullable = False)
    log_book_name = db.Column(db.String(20), nullable=False)
    licence = db.Column(db.LargeBinary, nullable = False)
    licence_name = db.Column(db.String(20), nullable=False)
    owner = db.Column(db.Integer, db.ForeignKey('transporter.id'))

class Emails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable = False)
    email = db.Column(db.String(40), nullable = False)
    subject = db.Column(db.String(500), nullable = False)
    body = db.Column(db.String(1000), nullable = False)
    

def is_active(self):
    return True
    