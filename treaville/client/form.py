from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email
class Clientform(FlaskForm):
    full_name = StringField(validators=[DataRequired()])
    company_name = StringField(validators=[DataRequired()])
    id_number =StringField(validators=[DataRequired()])
    email = StringField('Email Address', validators=[DataRequired(), Email()])
    aop = StringField(validators=[DataRequired()])
    city = StringField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])
    mobile_number = StringField(validators=[DataRequired()])
    alt_mobile_number = StringField(validators=[DataRequired()])
    submit = SubmitField('SIGN IN')

class Login(FlaskForm):
    email = StringField(validators=[DataRequired(), Email()])
    password = PasswordField()
    Submit = SubmitField('SIGN IN')
