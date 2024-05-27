from flask import Flask, request
import lxml.etree
from defusedxml.lxml import fromstring

app = Flask(__name__)

@app.route("/upload", methods=["POST"])
def upload():
    '''
    Get the xml_src from the request, parse it and return it as string.
    '''
    # Get the xml_src from the request
    xml_src = request.data

    # Parse the XML
    root = fromstring(xml_src)

    # Convert the parsed XML to string
    parsed_xml = lxml.etree.tostring(root, encoding='unicode')

    # Return the parsed XML as string
    return parsed_xml

if __name__ == "__main__":
    app.run(debug=False)  # Make sure debug mode is set to False in production environment