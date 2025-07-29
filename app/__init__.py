from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__,
                template_folder='../templates',
                static_folder='../static'
                )

    app.config['SECRET_KEY'] = 'secretkey123'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///workplaceandworkers.db'

    db.init_app(app)

    from .routes import main
    app.register_blueprint(main)
    with app.app_context():
        db.create_all()

    return app