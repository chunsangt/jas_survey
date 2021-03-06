from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment
from config import config

bootstrap = Bootstrap()
db = SQLAlchemy()
moment = Moment()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    moment.init_app(app)
    bootstrap.init_app(app)
    db.init_app(app)

    # 注册前台蓝本
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # 注册后台蓝本
    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')

    return app