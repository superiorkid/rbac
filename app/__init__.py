from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'


def create_app():
  app = Flask(__name__)
  app.config.from_object(Config)

  db.init_app(app)
  migrate.init_app(app, db)
  login_manager.init_app(app)


  from .main import main as main_blueprint
  from .auth import auth as auth_blueprint
  app.register_blueprint(main_blueprint)
  app.register_blueprint(auth_blueprint, url_prefix='/auth')

  return app
