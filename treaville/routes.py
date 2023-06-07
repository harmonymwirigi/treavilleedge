from flask import render_template, redirect, url_for, request, session
from treaville import app, db, bcrypt, mail
import flask_bcrypt
import base64
from flask_mail import Mail, Message
from flask_login import login_user, login_required, current_user, logout_user
from treaville.model import Client,Transporter, Vehicle, Bookingcargo, Bookingconstraction,Bookingpassenger
from treaville.form import Clientform,Transporterform, Login, Vehicleform, BookingConstractionform,BookingPassengerform, BookingCargoform
from datetime import datetime

def render_file(data):
    render_file = base64.b64encode(data).decode('ascii')
    return render_file

@app.route("/")
def home():
    return render_template('index.html')


@app.route('/transpoter')
def transpoter():
    return render_template("transporter.html")

@app.route('/signup', methods=['GET','POST'])
def transportersignup():
    Lform = Login()
    Tform = Transporterform()
    if Tform.validate_on_submit():
        hashed_passwed = flask_bcrypt.generate_password_hash(Tform.login_password.data).decode('utf-8')
        transpoter = Transporter(full_name = Tform.full_name.data, 
                                 company_name = Tform.company_name.data,
                                   Id_number = Tform.Id_number.data, 
                                   email_adress = Tform.email_adress.data,
                                     login_password = hashed_passwed, 
                                     owner_mobile = Tform.owner_mobile.data,
                                       alt_mobile = Tform.alt_mobile.data)
        db.session.add(transpoter)
        db.session.commit()
        return redirect(url_for('transportersignup'))
    return render_template("transportersignup.html", form = Tform, Lform = Lform)

@app.route("/clientsignup", methods=['GET','POST'])
def clientsignup():
    Lform = Login()
    Cform = Clientform()
    if Cform.validate_on_submit():
        hashed_passwed = flask_bcrypt.generate_password_hash(Cform.password.data).decode('utf-8')
        client = Client(full_name = Cform.full_name.data, company_name = Cform.company_name.data, id_number = Cform.id_number.data,email = Cform.email.data,
                        aop = Cform.aop.data, city = Cform.city.data, password = hashed_passwed,mobile_number = Cform.mobile_number.data, 
                        alt_mobile_number = Cform.alt_mobile_number.data)
        db.session.add(client)
        db.session.commit()
        return redirect(url_for('clientsignup'))
    return render_template('clientsignup.html', Cform = Cform, Lform = Lform)

@app.route("/login", methods=['POST', 'GET'])
def login():
    Tform = Transporterform()
    Lform = Login()
    if Lform.validate_on_submit():
        transporter = Transporter.query.filter_by(email_adress = Lform.email.data).first()
        client = Client.query.filter_by(email = Lform.email.data).first()
        if transporter and bcrypt.check_password_hash(transporter.login_password, Lform.password.data):
            session['user_type'] = 'transporter'
            login_user(transporter)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('dashboard'))
        if client and bcrypt.check_password_hash(client.password, Lform.password.data):
            session['user_type'] = 'client'
            login_user(client)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('booking'))
        else:
            return redirect(url_for('clientsignup'))
    return render_template('transportersignup.html', Lform = Lform, form = Tform)

@app.route('/dashboard', methods = ['POST', 'GET'])
@login_required
def dashboard():
    Vform = Vehicleform()
    jobcargo = []
    jobpassenger = []
    jobconstruction = []
    vehicles = Vehicle.query.filter_by(owner = current_user.id).all()
    me = Transporter.query.filter_by(id = current_user.id).first()
    for jobc in Bookingcargo.query.all():
        if jobc in me.requestscargo:
            pass
        else:
            jobcargo.append(jobc)
    for jobp in Bookingpassenger.query.all():
        if jobp in me.requestspassenger:
            pass
        else:
            jobpassenger.append(jobp)
    for jobco in Bookingconstraction.query.all():
        if jobco in me.requestsConstraction:
            pass
        else:
            jobconstruction.append(jobco)
            
    if Vform.validate_on_submit():
        file1 = request.files['license']
        data = file1.read()
        file2 = request.files['logbook']
        data1 = file2.read()
        vehicle = Vehicle(vehicle_type = Vform.vehicle_type.data, driver_name = Vform.driver_name.data,driver_id = Vform.driver_id.data, driver_no = Vform.drivers_no.data,
                          alt_no = Vform.alt_no.data, payment_account = Vform.pay_account.data, account_name =Vform.account_name.data, band_branch_name = Vform.branch_name.data,
                          aop = Vform.aop.data, town = Vform.town.data, log_book = data1, log_book_name = file2.filename, licence = data, licence_name =file1.filename  ,owner = current_user.id)
        db.session.add(vehicle)
        db.session.commit()
        current_user.vehicle.append(vehicle)
        db.session.commit()
        return redirect(url_for('dashboard'))
    return render_template("dashboard.html", Vform = Vform, jobcargo = jobcargo, jobpassenger = jobpassenger, jobconstruction = jobconstruction, vehicles = vehicles)
@app.route('/booking', methods = ['POST', 'GET'])
@login_required
def booking():
    BformC = BookingCargoform()
    BformP = BookingPassengerform()
    BformCo = BookingConstractionform()
    idbc = Bookingcargo.query.all()
    idbp = Bookingpassenger.query.all()
    idbco = Bookingconstraction.query.all()
    time = datetime.utcnow().strftime('%Y%m%d')
    valueC = "TVEBC"+time+str(len(idbc)+1)
    valuep = "TVEBP"+time+str(len(idbp)+1)
    valueCO = "TVEBCO"+time+str(len(idbco)+1)
    if BformC.validate_on_submit():
        job = Bookingcargo(name_of_client = BformC.name_of_client.data,my_id = valueC, email = BformC.email.data, mobile_number = BformC.mobile_number.data, alt_mobile_number = BformC.alt_mobile_number.data, pickup_location = BformC.pickup_location.data,
                      delivery_destination = BformC.delivery_destination.data, vehicle_type = BformC.vehicle_type.data, cargo_type = BformC.cargo_type.data, cargo_wight = BformC.cargo_wight.data,cargo_volume = BformC.cargo_volume.data,offer_amount = BformC.offer_amount.data,my_client = current_user.id)
        db.session.add(job)
        db.session.commit()
        requests = job
        msg_title = "Congratulations, Someone just booked a service"
        sender = "noreply@app.com"
        msg = Message(msg_title, sender=sender, recipients=['harmonymwirigi99@gmail.com'])
        msg_body = "Client information"
        data = {
            'app_name': 'TREAVILLE EDGE',
            'title' : msg_title,
            'body' : msg_body,
            'name': requests.name_of_client,
            'service_id': requests.my_id,
            'email': requests.email,
            'phone_numer': requests.mobile_number,
            'company': requests.company,
            'my_id': requests.my_id,
            'cargo_type': requests.cargo_type,
            'width' : requests.cargo_wight,
            'volume': requests.cargo_volume,
            'vehicle': requests.vehicle_type,
            'pickup':requests.pickup_location,
            'destination': requests.delivery_destination,
            'offer_amount': requests.offer_amount,
            'time': requests.date_made.strftime('%Y%m%d'),
        }
        msg.html = render_template("bookingemail.html", data = data)
        try:
            mail.send(msg)
            return "email sent"
        except Exception as e:
            print(e)
            return "the email was not sent{e}"
        # return redirect(url_for("booking"))
    if BformCo.validate_on_submit():
        job = Bookingconstraction(full_name = BformCo.full_name.data, my_id = valueCO, company_name = BformCo.company_name.data, email=BformCo.email.data, mobile_number = BformCo.mobile_number.data,
                                  alt_number = BformCo.alt_number.data, location = BformCo.location.data, vehicle_type = BformCo.vehicle_type.data,offer_amount = BformCo.offer_amount.data, my_client = current_user.id)
        db.session.add(job)
        db.session.commit()
        print("successdk")
        return redirect(url_for("booking"))
    if BformP.validate_on_submit():
        job = Bookingpassenger(full_name = BformP.full_name.data, company_name = BformP.company_name.data,my_id = valuep, email = BformP.email.data, mobile_number = BformP.mobile_number.data,
                               alt_number = BformP.alt_number.data, pickup_location = BformP.pickup_location.data, Destination = BformP.Destination.data, vehicle_type = BformP.vehicle_type.data,
                               no_of_passenger = BformP.no_of_passenger.data, offer_amount = BformP.offer_amount.data, my_client = current_user.id)
        db.session.add(job)
        db.session.commit()
        print("successde")
        return redirect(url_for("booking"))
    return render_template('booking.html', BformC = BformC, BformCo = BformCo, BformP = BformP)

@app.route("/request/<my_id>", methods=['GET'])
@login_required
def requesta(my_id):
    transpoter = Transporter.query.filter_by(id = current_user.id).first()
    requests = Bookingcargo.query.filter_by(my_id = my_id).first()
    requestP = Bookingpassenger.query.filter_by(my_id = my_id).first()
    requestC = Bookingconstraction.query.filter_by(my_id = my_id).first()
    print(requests)
    if requests:
        # transpoter.requestscargo.append(requests)
        # db.session.commit()
        msg_title = "A transporter is requesting to handle a service"
        sender = "noreply@app.com"
        msg = Message(msg_title, sender=sender, recipients=['harmonymwirigi99@gmail.com'])
        data = {
            'app_name': 'TREAVILLE EDGE',
            'title' : msg_title,
            'name': transpoter.full_name,
            'service_id': requests.my_id,
            'email': transpoter.email_adress,
            'phone_numer': transpoter.owner_mobile,
            'company': requests.company,
            'my_id': requests.my_id,
            'cargo_type': requests.cargo_type,
            'width' : requests.cargo_wight,
            'volume': requests.cargo_volume,
            'vehicle': requests.vehicle_type,
            'pickup':requests.pickup_location,
            'destination': requests.delivery_destination,
            'offer_amount': requests.offer_amount,
            'time': requests.date_made.strftime('%Y%m%d'),
        }
        msg.html = render_template("transporterrequest.html", data = data)
        try:
            mail.send(msg)
            return "email sent"
        except Exception as e:
            print(e)
            return "the email was not sent{e}"
    if requestP:
        transpoter.requestspassenger.append(requestP)
        db.session.commit()
        msg_title = "Congratulations, Someone just booked a service"
        sender = "noreply@app.com"
        msg = Message(msg_title, sender=sender, recipients="harmonymwirigi99@gmail.com")
        msg_body = "Client information"
        data = {
            'app_name': 'TREAVILLE EDGE',
            'title' : msg_title,
            'body' : msg_body,
            
        }
        msg.html = render_template("bookingemail.html", data = data)
        try:
            mail.send(msg)
            return "email sent"
        except Exception as e:
            print(e)
            return "the email was not sent{e}"
    if requestC:
        transpoter.requestsConstraction.append(requestC)
        db.session.commit()
        msg_title = "Congratulations, Someone just booked a service"
        sender = "noreply@app.com"
        msg = Message(msg_title, sender=sender, recipients="harmonymwirigi99@gmail.com")
        msg_body = "Client information"
        data = {
            'app_name': 'TREAVILLE EDGE',
            'title' : msg_title,
            'body' : msg_body,
        }
        msg.html = render_template("bookingemail.html", data = data)
        try:
            mail.send(msg)
            return "email sent"
        except Exception as e:
            print(e)
            return "the email was not sent{e}"
    
    return render_template('test.html')

@app.route("/vehicles")
@login_required
def vehicles():
    vehicles = Vehicle.query.filter_by(owner = current_user.id).all()
    return render_template("edit-vehicle-info.html", vehicles = vehicles)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

