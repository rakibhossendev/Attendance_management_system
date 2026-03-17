from flask import Blueprint, render_template, request, redirect, url_for
from app.extensions import db
from app.models import Subject, Teacher

subject_bp = Blueprint("subject_admin", __name__)


@subject_bp.route("/admin/subjects")
def subjects():

    subjects = Subject.query.all()

    teachers = Teacher.query.all()

    return render_template(
        "admin/subjects.html",
        subjects=subjects,
        teachers=teachers
    )


@subject_bp.route("/admin/add-subject", methods=["POST"])
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

    return redirect(url_for("subject_admin.subjects"))
    
    
@subject_bp.route("/admin/update-subject/<int:id>", methods=["POST"])
def update_subject(id):

    subject = Subject.query.get_or_404(id)

    subject.name = request.form.get("name")
    subject.semester = request.form.get("semester")
    subject.department = request.form.get("department")
    subject.teacher_id = request.form.get("teacher_id")

    db.session.commit()

    return redirect(url_for("subject_admin.subjects"))
    
    
@subject_bp.route("/admin/delete-subject/<int:id>", methods=["POST"])
def delete_subject(id):

    subject = Subject.query.get_or_404(id)

    db.session.delete(subject)
    db.session.commit()

    return redirect(url_for("subject_admin.subjects"))
    