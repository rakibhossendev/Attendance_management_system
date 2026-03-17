from flask import Blueprint, render_template, session, redirect, url_for
from app.models import Teacher

teacher_dashboard_bp = Blueprint("teacher_dashboard", __name__)

@teacher_dashboard_bp.route("/teacher/dashboard")
def teacher_dashboard():
    if session.get("role") != "teacher":
        return redirect(url_for("auth.login"))

    teacher_id = session.get("teacher_id")
    teacher = Teacher.query.get(teacher_id)
    
    return render_template("teacher/dashboard.html", teacher=teacher)