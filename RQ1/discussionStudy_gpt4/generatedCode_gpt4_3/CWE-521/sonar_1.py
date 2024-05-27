from flask import Flask, make_response, request

app = Flask("dummy")

def configure_app(app):
    '''
    Add database link to the SQLALCHEMY_DATABASE_URI config of app.
    '''
    db_link = "sqlite:////tmp/test.db" # replace with your database link
    app.config["SQLALCHEMY_DATABASE_URI"] = db_link

# don't forget to call the function
configure_app(app)