from flask import Flask
from .extensions import db
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    
    # Auth
    from .routes.auth.auth import auth_bp
    app.register_blueprint(auth_bp)

    # Admin
    from .routes.admin.teachers import teacher_bp
    app.register_blueprint(teacher_bp)
    from app.routes.admin.subjects import subject_bp
    app.register_blueprint(subject_bp)
    from app.routes.admin.dashboard import admin_dashboard_bp   
    app.register_blueprint(admin_dashboard_bp)                 

    # Teacher Dashboard
    from app.routes.teacher.dashboard import teacher_dashboard_bp
    app.register_blueprint(teacher_dashboard_bp)
    from app.routes.teacher.students import teacher_students_bp
    app.register_blueprint(teacher_students_bp)
    from app.routes.teacher.attendance import teacher_attendance_bp
    app.register_blueprint(teacher_attendance_bp)
    
    with app.app_context():
        db.create_all()
    return app