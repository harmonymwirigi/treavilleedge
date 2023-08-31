from flask import Blueprint, render_template
from flask_login import login_required, current_user
from treaville.model import Vehicle

vehicless = Blueprint('vehicless', __name__)

@vehicless.route("/vehicles")
@login_required
def vehicles():
    vehicles = Vehicle.query.filter_by(owner = current_user.id).all()
    return render_template("edit-vehicle-info.html", vehicles = vehicles)

