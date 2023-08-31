from flask import Blueprint, abort, session
from treaville.model import Bookingcargo
from treaville.model import Transporter, Vehicle, Client
from treaville import db, admin, create_app
from flask_admin.contrib.sqla import ModelView
from flask import  url_for, redirect, request
from flask_security import Security, SQLAlchemyUserDatastore, login_required, current_user
from flask_security.utils import encrypt_password
from flask_admin.contrib import sqla
from flask_admin import BaseView, expose


adm = Blueprint("adm", __name__)
        
    
admin.name = "Admin Panel"

class SecuredModel(ModelView):
    def is_accessible(self):
        if "logged_in" in session:
            return True
        else:
            abort(403)
    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('clients.login', next=request.url))
    
class SecureModel(ModelView):
    def is_accessible(self):
        if "logged_in" in session:
            return True
        else:
            abort(403)
    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('clients.login', next=request.url))
    column_searchable_list = ['alt_mobile']
    column_filters = ['alt_mobile']

class AnalyticsView(BaseView):
    @expose('/')
    def index(self):
        vehicles= Vehicle.query.all()
        return self.render('transpotervehicle.html',  vehicles = vehicles)

admin.add_view(AnalyticsView(name='VERIFY VEHICLE', endpoint='analytics'))


admin.add_view(SecuredModel(Bookingcargo, db.session))
admin.add_view(SecureModel(Transporter, db.session))
admin.add_view(SecuredModel(Vehicle, db.session))
admin.add_view(SecuredModel(Client, db.session))
