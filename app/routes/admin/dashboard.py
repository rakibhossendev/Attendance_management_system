from flask import Blueprint, render_template, session
from .decorators import admin_required
from app.models import Teacher, Student, Subject

admin_dashboard_bp = Blueprint("admin_dashboard", __name__, url_prefix="/admin")

@admin_dashboard_bp.route("/dashboard")
@admin_required
def admin_dashboard():
    """
    Admin dashboard with counts of teachers, students, subjects
    """
    total_teachers = Teacher.query.count()
    total_students = Student.query.count()
    total_subjects = Subject.query.count()

    return render_template(
        "admin/dashboard.html",
        total_teachers=total_teachers,
        total_students=total_students,
        total_subjects=total_subjects
    )