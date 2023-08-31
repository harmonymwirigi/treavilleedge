from flask import Blueprint
from flask import render_template, redirect, url_for, request, session, send_file
from treaville import db, bcrypt, mail
import flask_bcrypt
from flask_mail import Message
from flask_login import login_user, login_required, current_user, logout_user
from treaville.model import Client,Transporter, Vehicle, Bookingcargo, Bookingconstraction,Bookingpassenger
from treaville.transpoter.form import Transporterform, Login
from treaville.vehicle.form import  Vehicleform
from io import BytesIO


transpot = Blueprint('transpot', __name__)

@transpot.route('/transpoter')
def transpoter():
    return render_template("transporter.html")

@transpot.route('/signup', methods=['GET','POST'])
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
        return redirect(url_for('transpot.transportersignup'))
    return render_template("transportersignup.html", form = Tform, Lform = Lform)


@transpot.route("/login", methods=['POST', 'GET'])
def login():
    Tform = Transporterform()
    Lform = Login()
    if Lform.validate_on_submit():
        transporter = Transporter.query.filter_by(email_adress = Lform.email.data).first()
        client = Client.query.filter_by(email = Lform.email.data).first()
        if transporter and bcrypt.check_password_hash(transporter.login_password, Lform.password.data):
            session['user_type'] = 'transporter'
            login_user(transporter)
            if transporter.pending:
                return render_template('test.html')
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('transporter.dashboard'))
        if client and bcrypt.check_password_hash(client.password, Lform.password.data):
            session['user_type'] = 'client'
            login_user(client)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('book.booking'))
        else:
            return redirect(url_for('clients.clientsignup'))
    return render_template('transportersignup.html', Lform = Lform, form = Tform)

@transpot.route('/aprroved/<int:id>', methods = ['POST', 'GET'])
def approve_vehicle(id):
    vehicle = Vehicle.query.filter_by(id = id).first()
    vehicle.approved = True
    db.session.commit()
    return redirect('/admin/analytics/')


@transpot.route('/dashboard', methods = ['POST', 'GET'])
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
        return redirect(url_for('transpot.dashboard'))
    return render_template("dashboard.html", Vform = Vform, jobcargo = jobcargo, jobpassenger = jobpassenger, jobconstruction = jobconstruction, vehicles = vehicles)




@transpot.route("/request/<my_id>", methods=['GET'])
@login_required
def requesta(my_id):
    transpoter = Transporter.query.filter_by(id = current_user.id).first()
    requests = Bookingcargo.query.filter_by(my_id = my_id).first()
    requestP = Bookingpassenger.query.filter_by(my_id = my_id).first()
    requestC = Bookingconstraction.query.filter_by(my_id = my_id).first()
    print(requests)
    if requests:
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
            if mail.send(msg):
                transpoter.requestscargo.append(requests)
                db.session.commit()
                return redirect(url_for('transpot.dashboard'))
        except Exception as e:
            print(e)
            return "the email was not sent{e}"
    if requestP:
        transpoter.requestspassenger.append(requestP)
        db.session.commit()
        msg_title = "Congratulations, Someone just booked a service"
        sender = "noreply@app.com"
        msg = Message(msg_title, sender=sender, recipients=['harmonymwirigi99@gmail.com'])
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
        msg = Message(msg_title, sender=sender, recipients=['harmonymwirigi99@gmail.com'])
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
    
    return redirect(url_for('transpot.dashboard'))

@transpot.route("/download/<id>")
@login_required
def download(id):
    licence = Vehicle.query.filter_by(id=id).first()
    return send_file(BytesIO(licence.log_book), download_name=licence.licence_name, as_attachment=True)

@transpot.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.home'))