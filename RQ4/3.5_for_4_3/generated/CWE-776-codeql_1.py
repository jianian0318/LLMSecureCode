from flask import Flask, request
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.route("/upload", methods=['POST'])
def upload():
    '''
    Reads the XML from the incoming request.
    Parse it and return.
    '''
    xml_data = request.data.decode()
    parser = ET.XMLParser()

    # Disable External Entity Expansion
    parser.entity["xxe"] = "no"
    parser.entity["file"] = "no"
    parser.entity["network"] = "no"
    parser.entity["path"] = "no"
    parser.entity["port"] = "no"
    parser.entity["%"] = "no"

    root = ET.fromstring(xml_data, parser=parser)
    
    return f"Successfully parsed XML: {ET.tostring(root).decode()}"