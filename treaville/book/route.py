from flask import Blueprint
from flask import Blueprint, render_template, redirect, url_for
from treaville import db, mail
from flask_mail import Message
from flask_login import  login_required, current_user
from treaville.model import  Bookingcargo, Bookingconstraction,Bookingpassenger
from treaville.book.form import BookingConstractionform,BookingPassengerform, BookingCargoform
from datetime import datetime

book = Blueprint('book', __name__)

@book.route('/booking', methods = ['POST', 'GET'])
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
            'time': time,
        }
        msg.html = render_template("bookingemail.html", data = data)
        try:
            if mail.send(msg):
                db.session.add(job)
                db.session.commit()
                return redirect(url_for('book.booking'))
        except Exception as e:
            print(e)
            return "the email was not sent{e}"
        # return redirect(url_for("booking"))
    if BformCo.validate_on_submit():
        job = Bookingconstraction(full_name = BformCo.full_name.data, my_id = valueCO, company_name = BformCo.company_name.data, email=BformCo.email.data, mobile_number = BformCo.mobile_number.data,
                                  alt_number = BformCo.alt_number.data, location = BformCo.location.data, vehicle_type = BformCo.vehicle_type.data,offer_amount = BformCo.offer_amount.data, my_client = current_user.id)
        db.session.add(job)
        db.session.commit()
        return redirect(url_for("book.booking"))
    if BformP.validate_on_submit():
        job = Bookingpassenger(full_name = BformP.full_name.data, company_name = BformP.company_name.data,my_id = valuep, email = BformP.email.data, mobile_number = BformP.mobile_number.data,
                               alt_number = BformP.alt_number.data, pickup_location = BformP.pickup_location.data, Destination = BformP.Destination.data, vehicle_type = BformP.vehicle_type.data,
                               no_of_passenger = BformP.no_of_passenger.data, offer_amount = BformP.offer_amount.data, my_client = current_user.id)
        db.session.add(job)
        db.session.commit()
        print("successde")
        return redirect(url_for("book.booking"))
    return render_template('booking.html', BformC = BformC, BformCo = BformCo, BformP = BformP)