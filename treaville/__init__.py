from flask import Flask
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_mail import Mail
from treaville.config import Config


mail = Mail()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'clients.login'
bcrypt = Bcrypt()
admin = Admin()





def create_app(config_class = Config):
    app = Flask(__name__) 
    app.config.from_object(Config)
    mail.init_app(app)
    db.init_app(app)
    bcrypt.init_app(app)
    admin.init_app(app)
    login_manager.init_app(app)
    
    from treaville.client.routes import clients
    from treaville.main.routes import main
    from treaville.transpoter.routes import transpot
    from treaville.vehicle.route import vehicless
    from treaville.book.route import book
    from treaville.admin import adm

    app.register_blueprint(book)
    app.register_blueprint(clients)
    app.register_blueprint(main)
    app.register_blueprint(transpot)
    app.register_blueprint(vehicless)
    app.register_blueprint(adm)

    with app.app_context():
        db.create_all()

    return app