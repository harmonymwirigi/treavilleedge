from flask import Blueprint
from flask import render_template, redirect, url_for, request, session
from treaville import db, bcrypt
import flask_bcrypt
from flask_login import login_user, logout_user
from treaville.model import Client,Transporter
from treaville.client.form import Clientform, Login
from treaville.transpoter.form import Transporterform


clients = Blueprint('clients', __name__)

@clients.route("/clientsignup", methods=['GET','POST'])
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
        return redirect(url_for('clients.clientsignup'))
    return render_template('clientsignup.html', Cform = Cform, Lform = Lform)

@clients.route("/login", methods=['POST', 'GET'])
def login():
    Tform = Transporterform()
    Lform = Login()
    if Lform.validate_on_submit():
        transporter = Transporter.query.filter_by(email_adress = Lform.email.data).first()
        client = Client.query.filter_by(email = Lform.email.data).first()
        if transporter and bcrypt.check_password_hash(transporter.login_password, Lform.password.data):
            session['user_type'] = 'transporter'
            if transporter.pending:
                return render_template('test.html')
            login_user(transporter)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('transpot.dashboard'))
        if client and bcrypt.check_password_hash(client.password, Lform.password.data):
            session['user_type'] = 'client'
            login_user(client)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('book.booking'))
        if Lform.email.data == "admin@gmail.com" and Lform.password.data == "Admin":
            session['logged_in'] = True
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect("/admin")
        else:
            return redirect(url_for('clients.clientsignup'))
    return render_template('transportersignup.html', Lform = Lform, form = Tform)


@clients.route('/logout')
def logout():
    logout_user()
    session.clear()
    return redirect(url_for('main.home'))