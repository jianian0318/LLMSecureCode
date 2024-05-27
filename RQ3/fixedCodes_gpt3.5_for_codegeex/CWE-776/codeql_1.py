from flask import Flask, request
import xml.etree.ElementTree as ET
import defusedxml.ElementTree as DET

app = Flask(__name__)

@app.post("/upload")
def upload():
    '''
    Reads the XML from the incoming request.
    Parse it using defusedxml to prevent entity expansion.
    Return the parsed XML.
    '''
    xml = request.data.decode('utf-8')
    parser = DET.DefusedXMLParser()
    tree = DET.parseString(xml, parser=parser)
    root = tree.getroot()
    return ET.tostring(root, encoding='unicode')