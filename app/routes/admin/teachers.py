from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from app.models import Teacher
from app.extensions import db
from functools import wraps

teacher_bp = Blueprint("teacher_admin", __name__)

# --- Login required decorator ---
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "admin_logged_in" not in session:
            flash("Please login to access this page.", "warning")
            return redirect(url_for("auth.login"))
        return f(*args, **kwargs)
    return decorated_function

# --- List teachers ---
@teacher_bp.route("/admin/teachers")
@login_required
def teachers():
    teachers = Teacher.query.all()
    return render_template("admin/teachers.html", teachers=teachers, active_page="teachers")

# --- Add teacher ---
@teacher_bp.route("/admin/add-teacher", methods=["POST"])
@login_required
def add_teacher():
    name = request.form.get("name")
    email = request.form.get("email")
    mobile = request.form.get("mobile")
    username = request.form.get("username")
    password = request.form.get("password")

    teacher = Teacher(
        name=name,
        email=email,
        mobile=mobile,
        username=username
    )
    teacher.set_password(password)

    db.session.add(teacher)
    db.session.commit()
    flash(f"Teacher {name} added successfully.", "success")
    return redirect(url_for("teacher_admin.teachers"))

# --- Update teacher ---
@teacher_bp.route("/admin/update-teacher/<int:id>", methods=["POST"])
@login_required
def update_teacher(id):
    teacher = Teacher.query.get_or_404(id)
    teacher.name = request.form.get("name")
    teacher.email = request.form.get("email")
    teacher.mobile = request.form.get("mobile")
    teacher.username = request.form.get("username")
    password = request.form.get("password")
    if password:
        teacher.set_password(password)
    db.session.commit()
    flash(f"Teacher {teacher.name} updated successfully.", "success")
    return redirect(url_for("teacher_admin.teachers"))

# --- Delete teacher ---
@teacher_bp.route("/admin/delete-teacher/<int:id>", methods=["POST"])
@login_required
def delete_teacher(id):
    teacher = Teacher.query.get_or_404(id)
    db.session.delete(teacher)
    db.session.commit()
    flash(f"Teacher {teacher.name} deleted successfully.", "success")
    return redirect(url_for("teacher_admin.teachers"))