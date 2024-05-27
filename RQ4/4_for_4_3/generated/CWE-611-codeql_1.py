from flask import Flask, request
from defusedxml import DefusedXMLParser as DXMLP

app = Flask(__name__)

@app.route("/upload", methods=['POST'])
def upload():
    # Get XML data from request
    xml_src = request.data
    # Parse XML data using defusedxml 
    parsed_xml = DXMLP.parse(xml_src)
    # Get the XML string back for further processing
    xml_string = parsed_xml.toxml()
    
    return xml_string

if __name__ == "__main__":
    # Turn off debug mode
    app.run(debug=False)