from flask import Flask, request
import xml.etree.ElementTree as ET

app = Flask(__name__)


@app.route("/upload", methods=['POST'])
def upload():
    '''
    Reads the XML from the incoming request.
    Parse it and return.
    '''
    xml_data = request.data  # Getting XML data from the incoming request 
    root = ET.fromstring(xml_data)  # Parsing XML data
    return f"Parsed XML: {ET.tostring(root).decode()}"  # Returning parsed XML data
  

if __name__ == "__main__":
    app.run(debug=True)