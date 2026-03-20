from flask import Blueprint, render_template, request, session, redirect, url_for
from app.models import Student, Attendance, Subject
from app.extensions import db

teacher_attendance_bp = Blueprint("teacher_attendance", __name__)

@teacher_attendance_bp.route("/teacher/attendance", methods=["GET", "POST"])
def attendance():
    if session.get("role") != "teacher":
        return redirect(url_for("auth.login"))

    subjects = []
    students = []
    department = request.form.get("department")
    semester = request.form.get("semester")
    date = request.form.get("date")
    period = request.form.get("period")
    subject_id = request.form.get("subject_id")

    # Load assigned subjects for this teacher
    teacher_id = session.get("teacher_id")
    subjects = Subject.query.filter_by(teacher_id=teacher_id).all()

    # Load students if form submitted
    if request.method == "POST" and department and semester:
        students = Student.query.filter_by(
            department=department,
            semester=semester
        ).all()

    return render_template(
        "teacher/attendance.html",
        students=students,
        subjects=subjects
    )
    
@teacher_attendance_bp.route("/teacher/save-attendance", methods=["POST"])
def save_attendance():
    if session.get("role") != "teacher":
        return redirect(url_for("auth.login"))

    date = request.form.get("date")
    period = request.form.get("period")
    subject_id = request.form.get("subject_id")

    students = Student.query.filter_by(
        department=request.form.get("department"),
        semester=request.form.get("semester")
    ).all()

    for student in students:
        status = request.form.get(f"status_{student.id}", "Absent")

        # Check duplicate: same student + date + period + subject
        existing = Attendance.query.filter_by(
            student_id=student.id,
            date=date,
            period=period,
            subject_id=subject_id
        ).first()

        if existing:
            existing.status = status  # update existing
        else:
            attendance = Attendance(
                student_id=student.id,
                date=date,
                period=period,
                subject_id=subject_id,
                status=status
            )
            db.session.add(attendance)

    db.session.commit()
    return redirect(url_for("teacher_attendance.attendance"))
    