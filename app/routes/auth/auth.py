from flask import Blueprint, render_template, request, redirect, url_for
from app.models import Admin
from app.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/", methods=["GET", "POST"])
def login():

    admin = Admin.query.filter_by(username="admin").first()

    if not admin:
        new_admin = Admin(username="admin")
        new_admin.password = generate_password_hash("admin")
        db.session.add(new_admin)
        db.session.commit()

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        admin = Admin.query.filter_by(username=username).first()

        if admin and check_password_hash(admin.password, password):
            return render_template("admin/dashboard.html")

    return render_template("auth/login.html")