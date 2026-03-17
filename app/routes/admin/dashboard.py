# app/routes/admin/dashboard.py
from flask import Blueprint, render_template, session, redirect, url_for

admin_dashboard_bp = Blueprint("admin_dashboard", __name__)

@admin_dashboard_bp.route("/admin/dashboard")
def admin_dashboard():
    if session.get("role") != "admin":
        return redirect(url_for("auth.login"))
    return render_template("admin/dashboard.html")