from flask import Flask, request
from defusedxml.ElementTree import parse

app = Flask(__name__)

@app.route("/upload", methods=['POST'])
def upload():
    '''
    Reads the XML from the incoming request.
    Parse it and return.
    '''
    xml_data = request.data  # Getting XML data from the incoming request 
    root = parse(xml_data)  # Parsing XML data safely with defusedxml
    return f"Parsed XML: {ET.tostring(root.getroot()).decode()}"  # Returning parsed XML data 

if __name__ == "__main__":
    app.run(debug=True)