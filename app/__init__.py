from flask import Flask
from .extensions import db
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    
    from .routes.auth.auth import auth_bp
    app.register_blueprint(auth_bp)
    from .routes.admin.teachers import teacher_bp
    app.register_blueprint(teacher_bp)

    with app.app_context():
        db.create_all()
    return app