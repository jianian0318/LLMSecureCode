from flask import Flask, request
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.route("/upload", methods=["POST"])
def upload():
    '''
    Reads the XML from the incoming request.
    Parse it and return.
    '''
    # Check if request is JSON
    if request.is_json:
        return "Invalid content type: XML expected", 400  # Return error if request is JSON

    # Check if request has XML data
    if not request.data:
        return "No XML data in the request", 400  # Return error if request has no data

    try:
        # Parse XML data
        root = ET.fromstring(request.data)

        # Process the XML and return the result
        # (Replace the following line with your own code)
        result = "XML processed successfully"

        return result, 200

    except ET.ParseError:
        return "Invalid XML data", 400  # Return error if XML data is invalid

if __name__ == "__main__":
    app.run()