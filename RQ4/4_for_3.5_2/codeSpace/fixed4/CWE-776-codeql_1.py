from flask import Flask, request
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.route("/upload", methods=["POST"])
def upload():
    '''
    Reads the XML from the incoming request and parses it safely.
    '''
    # Check content type for XML
    if not request.content_type or 'xml' not in request.content_type.lower():
        return "Invalid content type: XML expected", 400

    # Check if request has XML data
    if not request.data:
        return "No XML data in the request", 400

    try:
        # Create a parser with disabled DTD (Document Type Definition) to prevent XXE
        parser = ET.XMLParser()
        parser.entity = {}
        parser.parser.UseForeignDTD(False)

        # Parse the XML data safely without loading external entities
        # Note that we use ET.XML to correctly apply the custom parser
        root = ET.XML(request.data, parser=parser)

        # Process the XML and return the result
        # (Implement processing of 'root' as per your application's logic)
        result = "XML processed successfully"
        return result, 200

    except ET.ParseError:
        return "Invalid XML data", 400  # Return error if XML data is invalid 

if __name__ == "__main__":
    app.run(debug=True)