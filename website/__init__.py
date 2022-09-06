from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'mqkjfmkrzokznk16545612151djbsjdj@!!?105ee5d2d2d5f'

    from .views import views

    app.register_blueprint(views, url_prefix='/')

    #create_database(app)
    return app


def create_database(app):
    #if not path.exists('website/' + DB_NAME):
    #    db.create_all(app=app)
    #    print('Created Database!')
    pass
