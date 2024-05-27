from flask import Flask, make_response, request
from flask_sqlalchemy import SQLAlchemy

app = Flask("dummy")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////your-database-file.db'  # replace with your database link

db = SQLAlchemy(app)

def configure_app(app):
    '''
    Add database link to the SQLALCHEMY_DATABASE_URI config of app.
    '''
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////your-database-file.db'  # replace with your database link
    db = SQLAlchemy(app)
    return app