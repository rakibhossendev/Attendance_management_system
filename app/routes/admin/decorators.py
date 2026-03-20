from functools import wraps
from flask import session, redirect, url_for, flash

def admin_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if session.get("role") != "admin":
            flash("Admin login required!", "warning")
            return redirect(url_for("auth.login"))
        return f(*args, **kwargs)
    return decorated

def teacher_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if session.get("role") != "teacher":
            flash("Teacher login required!", "warning")
            return redirect(url_for("auth.login"))
        return f(*args, **kwargs)
    return decorated