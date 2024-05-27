from flask import Flask, request
import xml.etree.ElementTree as ET
from defusedxml.ElementTree import parse as defusedxml_parse

app = Flask(__name__)

@app.route("/upload", methods=['POST'])
def upload():
    '''
    Reads the XML from the incoming request.
    Parses it securely using defusedxml.
    If there is a parsing error, returns only an error message without detail of the exception.
    '''
    content = request.data
    try:
        root = defusedxml_parse(content)
        return ET.tostring(root, encoding='unicode'), 200
    except Exception:
        return "Error: Malformed XML.", 400

if __name__ == "__main__":
    app.run(debug=False)