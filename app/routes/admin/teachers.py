from flask import Blueprint, render_template, request, redirect, url_for
from app.models import Teacher
from app.extensions import db

teacher_bp = Blueprint("teacher_admin", __name__)


@teacher_bp.route("/admin/teachers")
def teachers():

    teachers = Teacher.query.all()

    return render_template("admin/teachers.html", teachers=teachers)


@teacher_bp.route("/admin/add-teacher", methods=["POST"])
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

    return redirect(url_for("teacher_admin.teachers"))
    
    
@teacher_bp.route("/admin/update-teacher/<int:id>", methods=["POST"])
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
    return redirect(url_for("teacher_admin.teachers"))    
    
@teacher_bp.route("/admin/delete-teacher/<int:id>", methods=["POST"])
def delete_teacher(id):
    teacher = Teacher.query.get_or_404(id)
    db.session.delete(teacher)
    db.session.commit()
    return redirect(url_for("teacher_admin.teachers"))
    