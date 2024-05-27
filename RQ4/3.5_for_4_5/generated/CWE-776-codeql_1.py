from flask import Flask, request
import xml.etree.ElementTree as ET
import logging

app = Flask(__name__)

@app.post("/upload")
def upload():
    '''
    Reads the XML from the incoming request.
    Parse it and return.
    '''

    # Get XML data sent with the post request
    xml_data = request.get_data().decode()

    # Set limits on XML parsing to prevent entity expansion
    parser = ET.XMLParser(target=ET.ElementTree(), resolve_entities=False, forbid_dtd=True)
    tree = ET.ElementTree()

    # Parse the XML data
    try:
        tree.parse(source=xml_data, parser=parser)
    except ET.ParseError:
        logging.error("Invalid XML format")
        return {'message': 'Invalid XML format'}

    # Do what you want with tree...
    
    # return response
    return {'message': 'XML Upload Successful'}

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    app.run(debug=False)