from flask import render_template, redirect, url_for, request, session
from treaville import app, db, bcrypt
import flask_bcrypt
import base64
from flask_login import login_user, login_required, current_user, logout_user
from treaville.model import Client,Transporter, Vehicle, BookingCargo, BookingConstraction,BookingPassenger
from treaville.form import Clientform,Transporterform, Login, Vehicleform, BookingConstractionform,BookingPassengerform, BookingCargoform

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
            return redirect(url_for('login'))
    return render_template('transportersignup.html', Lform = Lform, form = Tform)

@app.route('/dashboard', methods = ['POST', 'GET'])
@login_required
def dashboard():
    Vform = Vehicleform()
    jobcargo = BookingCargo.query.all()
    print(jobcargo)
    jobpassenger = BookingPassenger.query.all()
    jobconstruction = BookingConstraction.query.all()
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
    return render_template("dashboard.html", Vform = Vform, jobcargo = jobcargo, jobpassenger = jobpassenger, jobconstruction = jobconstruction)
@app.route('/booking', methods = ['POST', 'GET'])
@login_required
def booking():
    BformC = BookingCargoform()
    BformP = BookingPassengerform()
    BformCo = BookingConstractionform()
    transpoters = Transporter.query.all()
    if BformC.validate_on_submit():
        job = BookingCargo(name_of_client = BformC.name_of_client.data, email = BformC.email.data, mobile_number = BformC.mobile_number.data, alt_mobile_number = BformC.alt_mobile_number.data, pickup_location = BformC.pickup_location.data,
                      delivery_destination = BformC.delivery_destination.data, vehicle_type = BformC.vehicle_type.data, cargo_type = BformC.cargo_type.data, cargo_wight = BformC.cargo_wight.data,cargo_volume = BformC.cargo_volume.data,offer_amount = BformC.offer_amount.data,my_client = current_user.id)
        db.session.add(job)
        db.session.commit()
        for transporter in transpoters:
            transporter.bookingjobcargo.append(job)
            db.session.commit()
        print("success")
        return redirect(url_for("booking"))
    if BformCo.validate_on_submit():
        job = BookingConstraction(full_name = BformCo.full_name.data, company_name = BformCo.company_name.data, email=BformCo.email.data, mobile_number = BformCo.mobile_number.data,
                                  alt_number = BformCo.alt_number.data, location = BformCo.location.data, vehicle_type = BformCo.vehicle_type.data,offer_amount = BformCo.offer_amount.data, my_client = current_user.id)
        db.session.add(job)
        db.session.commit()
        for transporter in transpoters:
            transporter.bookingjobconstruction.append(job)
            db.session.commit()
        print("successdk")
        return redirect(url_for("booking"))
    if BformP.validate_on_submit():
        job = BookingPassenger(full_name = BformP.full_name.data, company_name = BformP.company_name.data, email = BformP.email.data, mobile_number = BformP.mobile_number.data,
                               alt_number = BformP.alt_number.data, pickup_location = BformP.pickup_location.data, Destination = BformP.Destination.data, vehicle_type = BformP.vehicle_type.data,
                               no_of_passenger = BformP.no_of_passenger.data, offer_amount = BformP.offer_amount.data, my_client = current_user.id)
        db.session.add(job)
        db.session.commit()
        for transporter in transpoters:
            transporter.bookingjobpassenger.append(job)
            db.session.commit()
        print("successde")
        return redirect(url_for("booking"))
    return render_template('booking.html', BformC = BformC, BformCo = BformCo, BformP = BformP)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))
