from flask import Flask, request
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.route("/upload", methods=['POST'])
def upload():
    '''
    Reads the XML from the incoming request.
    Parse it and return.
    '''
    xml_data = request.data
    if xml_data:
        root = ET.fromstring(xml_data)
        return str(ET.tostring(root))
    else:
        return "No xml data provided"

if __name__ == "__main__":
    app.run()