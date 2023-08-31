from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SelectField, SubmitField, IntegerField 
from wtforms.validators import DataRequired

class Vehicleform(FlaskForm):
    vehicle_type = SelectField(validators=[DataRequired()], choices=[("Vehicle Type:", "Vehicle Type:"),("Motor Bike", "Motor Bike"),
                                                                     ("Van", "Van"), ("PickUp", "PickUp"),("Truck 3T", "Truck 3T"),
                                                                     ("Truck 5T","Truck 5T"), ("Truck 7T","Truck 7T"), ("Truck 10T","Truck 10T"),
                                                                       ("Truck 15T", "Truck 15T"), ("Trailer 28T","Trailer 28T"),("Flat Bed","Flat Bed"),
                                                                         ("Tour Van","Tour Van"), ("Tour Landcruiser","Tour Landcruiser"), 
                                                                         ("Prado Landcruiser","Prado Landcruiser"), ("Rav4 SUV", "Rav4 SUV"),
                                                                           ("Mini Bus","Mini Bus"),("Tipper Truck 20T","Tipper Truck 20T"), 
                                                                           ("Excavator","Excavator"), ("Compactor","Compactor" ),
                                                                             ("Grader","Grader"), ("Bulldozer", "Bulldozer"), ("Wheel Loaders","Wheel Loaders"),
                                                                               ("Crane","Crane"), ("Forklift","Forklift")])
    driver_name = StringField(validators=[DataRequired()])
    driver_id = StringField(validators=[DataRequired()])
    drivers_no  = StringField(validators=[DataRequired()])
    alt_no = StringField(validators=[DataRequired()])
    pay_account = StringField(validators=[DataRequired()])
    account_name = StringField(validators=[DataRequired()])
    branch_name = StringField(validators=[DataRequired()])
    aop = StringField(validators=[DataRequired()])
    town = StringField(validators=[DataRequired()])
    logbook = FileField("Upload Logbook(Pdf only)", validators = [FileAllowed(['pdf'])])
    license = FileField("Upload License(Pdf or Image File):", validators = [FileAllowed(['docx', 'png', 'jpg', 'pdf', 'mp4'])])
    submit = SubmitField()
