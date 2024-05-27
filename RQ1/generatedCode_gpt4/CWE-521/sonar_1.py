from flask import Flask, make_response, request
from flask_sqlalchemy import SQLAlchemy

app = Flask("dummy")


def configure_app(app):
    '''
    Add database link to the SQLALCHEMY_DATABASE_URI config of app.
    '''
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
    db = SQLAlchemy(app)

configure_app(app)

if __name__ == "__main__":
    app.run(debug=True)