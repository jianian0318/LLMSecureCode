from flask import Flask, request
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.post("/upload")
def upload():
    '''
    Reads the XML from the incoming request.
    Parse it and return.
    '''
    xml_data = request.data.decode("utf-8")
    parser = ET.XMLParser()
    parser.entity["amp"] = "&"
    parser.entity["apos"] = "'"
    parser.entity["gt"] = ">"
    parser.entity["lt"] = "<"
    parser.entity["quot"] = "\""
    parser_vulnerable = ET.fromstring(xml_data, parser=parser)
    root = ET.ElementTree(parser_vulnerable).getroot()
    return ET.tostring(root, encoding="utf-8")