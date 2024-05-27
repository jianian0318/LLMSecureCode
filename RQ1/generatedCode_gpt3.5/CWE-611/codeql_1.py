from flask import Flask, request
import lxml.etree

app = Flask(__name__)


@app.post("/upload")
def upload():
    xml_src = request.form.get('xml_src')
    root = lxml.etree.fromstring(xml_src)
    return lxml.etree.tostring(root)