from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from app.models import Student, Teacher
from app.extensions import db

teacher_students_bp = Blueprint("teacher_students", __name__)

# Add student page
@teacher_students_bp.route("/teacher/add-student", methods=["GET", "POST"])
def add_student():
    if session.get("role") != "teacher":
        return redirect(url_for("auth.login"))

    teacher_id = session.get("teacher_id")
    teacher = Teacher.query.get(teacher_id)

    if request.method == "POST":
        name = request.form.get("name")
        roll = request.form.get("roll")
        department = request.form.get("department")
        semester = request.form.get("semester")

        if not name or not roll:
            flash("Name and Roll are required", "danger")
            return redirect(url_for("teacher_students.add_student"))

        # Check duplicate roll in same semester+department
        existing = Student.query.filter_by(roll=roll, semester=semester, department=department).first()
        if existing:
            flash("Student with this Roll already exists", "warning")
            return redirect(url_for("teacher_students.add_student"))

        student = Student(
            name=name,
            roll=roll,
            department=department,
            semester=semester
        )
        db.session.add(student)
        db.session.commit()
        flash("Student added successfully", "success")
        return redirect(url_for("teacher_students.add_student"))

    return render_template("teacher/students.html", teacher=teacher)
    
    
@teacher_students_bp.route("/teacher/view-students")
def view_students():
    if session.get("role") != "teacher":
        return redirect(url_for("auth.login"))

    teacher_id = session.get("teacher_id")
    teacher = Teacher.query.get(teacher_id)
    students = Student.query.order_by(Student.semester, Student.roll).all()
    return render_template("teacher/view_students.html", students=students, teacher=teacher)    
    
@teacher_students_bp.route("/teacher/edit-student/<int:id>")
def edit_student(id):
    if session.get("role") != "teacher":
        return redirect(url_for("auth.login"))
        
    student = Student.query.get_or_404(id)
    return render_template("teacher/edit_student.html", student=student)    

@teacher_students_bp.route("/teacher/update-student/<int:id>", methods=["POST"])
def update_student(id):

    if session.get("role") != "teacher":
        return redirect(url_for("auth.login"))

    student = Student.query.get_or_404(id)

    student.name = request.form.get("name")
    student.roll = request.form.get("roll")

    db.session.commit()

    return redirect(url_for("teacher_students.view_students"))
    
@teacher_students_bp.route("/teacher/delete-student/<int:id>", methods=["POST"])
def delete_student(id):

    if session.get("role") != "teacher":
        return redirect(url_for("auth.login"))

    student = Student.query.get_or_404(id)

    db.session.delete(student)
    db.session.commit()

    return redirect(url_for("teacher_students.view_students"))