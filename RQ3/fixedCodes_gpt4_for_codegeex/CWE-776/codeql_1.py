from flask import Flask, request
from defusedxml.ElementTree import parse

app = Flask(__name__)

@app.post("/upload")
def upload():
    '''
    Reads the XML from the incoming request.
    Parse it securely and return.
    '''
    xml = parse(request.stream)
    root = xml.getroot()
    return ET.tostring(root, encoding='unicode')