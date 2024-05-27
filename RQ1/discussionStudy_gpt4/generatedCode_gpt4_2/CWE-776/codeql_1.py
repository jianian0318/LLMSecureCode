from flask import Flask, request
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.route("/upload", methods=['POST'])
def upload():
    '''
    Reads the XML from the incoming request.
    Parse it and return.
    '''
    if request.method == 'POST': 
        try:
            xml_data = request.data  # get the xml data from the request
            root = ET.fromstring(xml_data.decode())  # parse the xml
            return "XML Data received and parsed successfully." 
        except Exception as e:
            return f"Failed to parse xml document: {str(e)}"
    
if __name__ == "__main__":
    app.run(debug=True)