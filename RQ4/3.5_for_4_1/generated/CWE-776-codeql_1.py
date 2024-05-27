from flask import Flask, request
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.post("/upload")
def upload():
    '''
    Reads the XML from the incoming request.
    Parse it and return.
    '''
    # Get XML data from the request
    xml_data = request.data

    # Parse XML data with XMLParser
    parser = ET.XMLParser(resolve_entities=False, forbid_dtd=True)

    # Set a limit on the maximum number of elements and attributes allowed in the XML document
    parser.parser.UseForeignDTD(False)
    parser.parser.CollectElementNodeData()
    parser.entity['%'] = '%'

    # Parse the XML data using the configured parser
    try:
        root = ET.fromstring(xml_data, parser=parser)
    except ET.ParseError as e:
        return str(e)

    # Let's say we want to return a specific value from the XML.
    # You need to replace 'yourElement' with the actual element name in your XML
    # that you want to extract data from.
    element_val = root.find('yourElement').text

    return element_val