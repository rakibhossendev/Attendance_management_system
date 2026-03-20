from flask import Blueprint, render_template, request, redirect, url_for, session
from werkzeug.security import check_password_hash
from app.models import Teacher

auth_bp = Blueprint("auth", __name__)

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin"  # production এ hash ব্যবহার করা উচিত

@auth_bp.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Admin login
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session["role"] = "admin"
            return redirect(url_for("admin_dashboard.admin_dashboard"))

        # Teacher login
        teacher = Teacher.query.filter_by(username=username).first()
        if teacher and teacher.check_password(password):
            session["role"] = "teacher"
            session["teacher_id"] = teacher.id
            return redirect(url_for("teacher_dashboard.teacher_dashboard"))

        return render_template("auth/login.html", error="Invalid username or password")

    return render_template("auth/login.html")


@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("auth.login"))