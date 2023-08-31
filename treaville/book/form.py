from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, IntegerField 
from wtforms.validators import DataRequired, Email

class BookingCargoform(FlaskForm):
    name_of_client = StringField(validators=[DataRequired()])
    company = StringField()
    email = StringField('Email Address', validators=[DataRequired(), Email()])
    mobile_number= StringField(validators=[DataRequired()])
    alt_mobile_number = StringField()
    pickup_location = SelectField(validators=[DataRequired()], choices=[("Nairobi","Nairobi"),("Meru","Meru"),("Mombasa","Mombasa"),("Kisumu","Kisumu"),("Nakuru","Nakuru"),
                    ("Eldoret","Eldoret"),("Machakos","Machakos"),("Kisii","Kisii"),("Mumias","Mumias"), ("Thika","Thika"),
                    ("Nyeri","Nyeri"),("Malindi","Malindi"),("Kakamega", "Kakamega"),("Kendu Bay","Kendu Bay"),( "Lodwar", "Lodwar"),
                    ("Athi River", "Athi River"),("Kilifi","Kilifi"),("Sotik","Sotik"),("Garissa","Garissa"),("Kitale","Kitale"),
                    ("Bungoma","Bungoma"),("Isiolo","Isiolo"),("Wajir","Wajir"),("Embu", "Embu"),("Voi","Voi"),( "Homa Bay", "Homa Bay"),
                    ("Nanyuki","Nanyuki"), ("Busia","Busia"),("Mandera","Mandera"),("Kericho", "Kericho"),( "Kitui", "Kitui"),
                    ("Maralal","Maralal"),("Lamu","Lamu"),("Kapsabet","Kapsabet"), ("Marsabit","Marsabit"), ("Hola","Hola"),
                    ("Kiambu","Kiambu"),("Kabarnet", "Kabarnet"),("Migori","Migori"),("Kerugoya","Kerugoya"),("Iten","Iten"),
                    ("Nyamira","Nyamira"), ("Murang’a","Murang’a"), ("Sotik Post","Sotik Post"), ("Siaya","Siaya"),("Kapenguria","Kapenguria"),
                    ("Wote","Wote"),("Mwatate","Mwatate"),("Kajiado","Kajiado"),("Ol Kalou","Ol Kalou"),("Narok","Narok"),
                    ("Kwale","Kwale"), ("Rumuruti","Rumuruti")])
    delivery_destination  = SelectField(validators=[DataRequired()], choices=[("Nairobi","Nairobi"),("Meru","Meru"),("Mombasa","Mombasa"),("Kisumu","Kisumu"),("Nakuru","Nakuru"),
                    ("Eldoret","Eldoret"),("Machakos","Machakos"),("Kisii","Kisii"),("Mumias","Mumias"), ("Thika","Thika"),
                    ("Nyeri","Nyeri"),("Malindi","Malindi"),("Kakamega", "Kakamega"),("Kendu Bay","Kendu Bay"),( "Lodwar", "Lodwar"),
                    ("Athi River", "Athi River"),("Kilifi","Kilifi"),("Sotik","Sotik"),("Garissa","Garissa"),("Kitale","Kitale"),
                    ("Bungoma","Bungoma"),("Isiolo","Isiolo"),("Wajir","Wajir"),("Embu", "Embu"),("Voi","Voi"),( "Homa Bay", "Homa Bay"),
                    ("Nanyuki","Nanyuki"), ("Busia","Busia"),("Mandera","Mandera"),("Kericho", "Kericho"),( "Kitui", "Kitui"),
                    ("Maralal","Maralal"),("Lamu","Lamu"),("Kapsabet","Kapsabet"), ("Marsabit","Marsabit"), ("Hola","Hola"),
                    ("Kiambu","Kiambu"),("Kabarnet", "Kabarnet"),("Migori","Migori"),("Kerugoya","Kerugoya"),("Iten","Iten"),
                    ("Nyamira","Nyamira"), ("Murang’a","Murang’a"), ("Sotik Post","Sotik Post"), ("Siaya","Siaya"),("Kapenguria","Kapenguria"),
                    ("Wote","Wote"),("Mwatate","Mwatate"),("Kajiado","Kajiado"),("Ol Kalou","Ol Kalou"),("Narok","Narok"),
                    ("Kwale","Kwale"), ("Rumuruti","Rumuruti")])
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
    cargo_type = StringField(validators=[DataRequired()])
    cargo_wight = IntegerField(validators=[DataRequired()])
    cargo_volume = IntegerField(validators=[DataRequired()])
    offer_amount = IntegerField(validators=[DataRequired()])
    submit = SubmitField("REGUEST")

class BookingPassengerform(FlaskForm):
    full_name = StringField(validators=[DataRequired()])
    company_name = StringField()
    email = StringField('Email Address', validators=[DataRequired(), Email()])
    mobile_number = StringField(validators=[DataRequired()])
    alt_number = StringField(validators=[DataRequired()])
    pickup_location = SelectField(validators=[DataRequired()], choices=[("Nairobi","Nairobi"),("Meru","Meru"),("Mombasa","Mombasa"),("Kisumu","Kisumu"),("Nakuru","Nakuru"),
                    ("Eldoret","Eldoret"),("Machakos","Machakos"),("Kisii","Kisii"),("Mumias","Mumias"), ("Thika","Thika"),
                    ("Nyeri","Nyeri"),("Malindi","Malindi"),("Kakamega", "Kakamega"),("Kendu Bay","Kendu Bay"),( "Lodwar", "Lodwar"),
                    ("Athi River", "Athi River"),("Kilifi","Kilifi"),("Sotik","Sotik"),("Garissa","Garissa"),("Kitale","Kitale"),
                    ("Bungoma","Bungoma"),("Isiolo","Isiolo"),("Wajir","Wajir"),("Embu", "Embu"),("Voi","Voi"),( "Homa Bay", "Homa Bay"),
                    ("Nanyuki","Nanyuki"), ("Busia","Busia"),("Mandera","Mandera"),("Kericho", "Kericho"),( "Kitui", "Kitui"),
                    ("Maralal","Maralal"),("Lamu","Lamu"),("Kapsabet","Kapsabet"), ("Marsabit","Marsabit"), ("Hola","Hola"),
                    ("Kiambu","Kiambu"),("Kabarnet", "Kabarnet"),("Migori","Migori"),("Kerugoya","Kerugoya"),("Iten","Iten"),
                    ("Nyamira","Nyamira"), ("Murang’a","Murang’a"), ("Sotik Post","Sotik Post"), ("Siaya","Siaya"),("Kapenguria","Kapenguria"),
                    ("Wote","Wote"),("Mwatate","Mwatate"),("Kajiado","Kajiado"),("Ol Kalou","Ol Kalou"),("Narok","Narok"),
                    ("Kwale","Kwale"), ("Rumuruti","Rumuruti")])
    Destination = SelectField(validators=[DataRequired()], choices=[("Nairobi","Nairobi"),("Meru","Meru"),("Mombasa","Mombasa"),("Kisumu","Kisumu"),("Nakuru","Nakuru"),
                    ("Eldoret","Eldoret"),("Machakos","Machakos"),("Kisii","Kisii"),("Mumias","Mumias"), ("Thika","Thika"),
                    ("Nyeri","Nyeri"),("Malindi","Malindi"),("Kakamega", "Kakamega"),("Kendu Bay","Kendu Bay"),( "Lodwar", "Lodwar"),
                    ("Athi River", "Athi River"),("Kilifi","Kilifi"),("Sotik","Sotik"),("Garissa","Garissa"),("Kitale","Kitale"),
                    ("Bungoma","Bungoma"),("Isiolo","Isiolo"),("Wajir","Wajir"),("Embu", "Embu"),("Voi","Voi"),( "Homa Bay", "Homa Bay"),
                    ("Nanyuki","Nanyuki"), ("Busia","Busia"),("Mandera","Mandera"),("Kericho", "Kericho"),( "Kitui", "Kitui"),
                    ("Maralal","Maralal"),("Lamu","Lamu"),("Kapsabet","Kapsabet"), ("Marsabit","Marsabit"), ("Hola","Hola"),
                    ("Kiambu","Kiambu"),("Kabarnet", "Kabarnet"),("Migori","Migori"),("Kerugoya","Kerugoya"),("Iten","Iten"),
                    ("Nyamira","Nyamira"), ("Murang’a","Murang’a"), ("Sotik Post","Sotik Post"), ("Siaya","Siaya"),("Kapenguria","Kapenguria"),
                    ("Wote","Wote"),("Mwatate","Mwatate"),("Kajiado","Kajiado"),("Ol Kalou","Ol Kalou"),("Narok","Narok"),
                    ("Kwale","Kwale"), ("Rumuruti","Rumuruti")])
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
    no_of_passenger = StringField(validators=[DataRequired()])
    offer_amount = StringField(validators=[DataRequired()])
    submit = SubmitField("REGUEST")

class BookingConstractionform(FlaskForm):
    full_name = StringField(validators=[DataRequired()])
    company_name = StringField()
    email = StringField('Email Address', validators=[DataRequired(), Email()])
    mobile_number = StringField(validators=[DataRequired()])
    alt_number = StringField(validators=[DataRequired()])
    location = SelectField(validators=[DataRequired()], choices=[("Nairobi","Nairobi"),("Meru","Meru"),("Mombasa","Mombasa"),("Kisumu","Kisumu"),("Nakuru","Nakuru"),
                    ("Eldoret","Eldoret"),("Machakos","Machakos"),("Kisii","Kisii"),("Mumias","Mumias"), ("Thika","Thika"),
                    ("Nyeri","Nyeri"),("Malindi","Malindi"),("Kakamega", "Kakamega"),("Kendu Bay","Kendu Bay"),( "Lodwar", "Lodwar"),
                    ("Athi River", "Athi River"),("Kilifi","Kilifi"),("Sotik","Sotik"),("Garissa","Garissa"),("Kitale","Kitale"),
                    ("Bungoma","Bungoma"),("Isiolo","Isiolo"),("Wajir","Wajir"),("Embu", "Embu"),("Voi","Voi"),( "Homa Bay", "Homa Bay"),
                    ("Nanyuki","Nanyuki"), ("Busia","Busia"),("Mandera","Mandera"),("Kericho", "Kericho"),( "Kitui", "Kitui"),
                    ("Maralal","Maralal"),("Lamu","Lamu"),("Kapsabet","Kapsabet"), ("Marsabit","Marsabit"), ("Hola","Hola"),
                    ("Kiambu","Kiambu"),("Kabarnet", "Kabarnet"),("Migori","Migori"),("Kerugoya","Kerugoya"),("Iten","Iten"),
                    ("Nyamira","Nyamira"), ("Murang’a","Murang’a"), ("Sotik Post","Sotik Post"), ("Siaya","Siaya"),("Kapenguria","Kapenguria"),
                    ("Wote","Wote"),("Mwatate","Mwatate"),("Kajiado","Kajiado"),("Ol Kalou","Ol Kalou"),("Narok","Narok"),
                    ("Kwale","Kwale"), ("Rumuruti","Rumuruti")])
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
    offer_amount = StringField(validators=[DataRequired()])
    submit = SubmitField("REQUEST")
