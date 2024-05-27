    from flask import Flask, request
    import lxml.etree

    app = Flask(__name__)

    @app.post("/upload")
    def upload():
        pass
    