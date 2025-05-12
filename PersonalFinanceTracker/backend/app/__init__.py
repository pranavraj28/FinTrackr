from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your-secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    db.init_app(app)
    login_manager.init_app(app)
    CORS(app)

    from .routes.auth import auth_bp
    from .routes.finance import finance_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(finance_bp)

    return app