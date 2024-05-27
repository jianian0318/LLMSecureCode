from flask import Flask, request
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import ParseError

app = Flask(__name__)
app.config['DEBUG'] = False

@app.route("/upload", methods=['POST'])
def upload():
    '''
    Reads the XML from the incoming request.
    Parse it and return.
    '''
    xml_data = request.data.decode('utf-8')  # get XML data from the incoming request

    # Limit the size of the XML to prevent denial-of-service attacks
    max_xml_size = 100000  # Maximum allowed size for XML file

    if len(xml_data) > max_xml_size:
        return 'XML size exceeded maximum limit'

    try:
        # Parse the XML
        root = ET.fromstring(xml_data)
    except ET.ParseError:
        return 'Invalid XML data'

    return 'Successful upload!'

if __name__ == '__main__':
    app.run()