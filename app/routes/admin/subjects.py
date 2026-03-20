from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from app.extensions import db
from app.models import Subject, Teacher
from functools import wraps

subject_bp = Blueprint("subject_admin", __name__)

# --- Login required decorator ---
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "admin_logged_in" not in session:
            flash("Please login to access this page.", "warning")
            return redirect(url_for("auth.login"))
        return f(*args, **kwargs)
    return decorated_function

# --- List subjects ---
@subject_bp.route("/admin/subjects")
@login_required
def subjects():
    subjects = Subject.query.all()
    teachers = Teacher.query.all()
    return render_template(
        "admin/subjects.html",
        subjects=subjects,
        teachers=teachers,
        active_page="subjects"
    )

# --- Add subject ---
@subject_bp.route("/admin/add-subject", methods=["POST"])
@login_required
def add_subject():
    name = request.form.get("name")
    semester = request.form.get("semester")
    department = request.form.get("department")
    teacher_id = request.form.get("teacher_id")

    subject = Subject(
        name=name,
        semester=semester,
        department=department,
        teacher_id=teacher_id
    )

    db.session.add(subject)
    db.session.commit()
    flash(f"Subject '{name}' assigned successfully.", "success")
    return redirect(url_for("subject_admin.subjects"))

# --- Update subject ---
@subject_bp.route("/admin/update-subject/<int:id>", methods=["POST"])
@login_required
def update_subject(id):
    subject = Subject.query.get_or_404(id)
    subject.name = request.form.get("name")
    subject.semester = request.form.get("semester")
    subject.department = request.form.get("department")
    subject.teacher_id = request.form.get("teacher_id")

    db.session.commit()
    flash(f"Subject '{subject.name}' updated successfully.", "success")
    return redirect(url_for("subject_admin.subjects"))

# --- Delete subject ---
@subject_bp.route("/admin/delete-subject/<int:id>", methods=["POST"])
@login_required
def delete_subject(id):
    subject = Subject.query.get_or_404(id)
    db.session.delete(subject)
    db.session.commit()
    flash(f"Subject '{subject.name}' deleted successfully.", "success")
    return redirect(url_for("subject_admin.subjects"))