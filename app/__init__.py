import bcrypt
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

db = SQLAlchemy()
bcrypt = Bcrypt()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config['SECRET_KEY'] = 'pedro'

    db.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)
    

    from app.controllers import auth_controller, main_controller
    app.register_blueprint(auth_controller.bp)
    app.register_blueprint(main_controller.bp)

    return app
