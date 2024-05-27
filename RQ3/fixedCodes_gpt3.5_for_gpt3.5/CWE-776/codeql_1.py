from flask import Flask, request
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.post("/upload")
def upload():
    '''
    Reads the XML from the incoming request.
    Parse it with entity expansion disabled and return.
    '''
    xml_data = request.data
    parser = ET.XMLParser()
    parser.entity["amp"] = "&amp;"
    parser.entity["lt"] = "&lt;"
    parser.entity["gt"] = "&gt;"
    parser.entity["quot"] = "&quot;"
    parser.entity["apos"] = "&apos;"
    root = ET.fromstring(xml_data, parser=parser)
    return ET.tostring(root)