from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField 
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
class Transporterform(FlaskForm):
    full_name = StringField(validators=[DataRequired()])
    company_name = StringField(validators=[DataRequired()])
    Id_number = IntegerField(validators=[DataRequired()])
    email_adress = StringField(validators=[DataRequired(), Email()])
    login_password = PasswordField(validators=[DataRequired()])
    confirm_password = PasswordField(validators=[DataRequired(), EqualTo('login_password')]) 
    owner_mobile =  StringField(validators=[DataRequired()])
    alt_mobile = StringField(validators=[DataRequired()])
    Submit = SubmitField()

    def validate_password(self, password):
        SpecialSym = ['$', '@', '#', '%']
        if not any(char in SpecialSym for char in password.data):
            raise ValidationError('Password should have at least one of the symbols $@#%')

class Login(FlaskForm):
    email = StringField(validators=[DataRequired(), Email()])
    password = PasswordField()
    Submit = SubmitField('SIGN IN')

