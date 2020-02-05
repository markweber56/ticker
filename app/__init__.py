from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment
import os
from flask_assets import Environment
# look into flask-assets
from .config import config

print('config from import: ',config['local'])
bootstrap = Bootstrap()
moment = Moment()
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    print('config of configname: ',config[config_name])
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    moment.init_app(app)
    db.init_app(app)

    from app.ticker import ticker as ticker_blueprint
    app.register_blueprint(ticker_blueprint)
    return app
