from flask import Blueprint, render_template

teacher_bp = Blueprint("teacher_admin", __name__)

@teacher_bp.route("/admin/teachers")
def teachers():
    return render_template("admin/teachers.html")