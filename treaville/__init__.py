from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mY sectrET kEY'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///treavill.db'
app.config['MAIL_SERVER'] = "smtp.googlemail.com"
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = "harmonymwirigi99@gmail.com"
app.config['MAIL_PASSWORD'] = 'hpxmffrphmioyipg'
mail = Mail(app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'




from treaville import routes