from flask import Flask, request
import xml.etree.ElementTree as ET

app = Flask(__name__)


@app.post("/upload")
def upload():
    '''
    Reads the XML from the incoming request.
    Parse it and return.
    '''
    xml = request.data.decode('utf-8')
    root = ET.fromstring(xml)
    return ET.tostring(root, encoding='unicode')
