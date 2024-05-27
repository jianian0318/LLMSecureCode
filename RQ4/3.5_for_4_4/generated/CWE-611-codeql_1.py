from flask import Flask, request
import defusedxml.lxml as lxml

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    # Get the xml content from the request
    xml_src = request.data

    # Parse the xml content with XXE protection
    parser = lxml.XMLParser(resolve_entities=False, no_network=True)
    root = lxml.fromstring(xml_src, parser)

    # Convert the parsed xml content to string
    xml_str = lxml.tostring(root, pretty_print=True)

    # Return the string
    return xml_str