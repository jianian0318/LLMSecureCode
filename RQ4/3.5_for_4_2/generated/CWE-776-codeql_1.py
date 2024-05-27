from flask import Flask, request
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.route("/upload", methods=["POST"])
def upload():
    '''
     Reads the XML from the incoming request.
     Parses it with entity expansion disabled.
     Returns the parsed XML as a string.
    '''
    # Read the XML data from the request
    data = request.get_data()

    # Disable entity expansion and limit the depth of the XML
    parser = ET.XMLParser(resolve_entities=False, forbid_dtd=True, forbid_external=True, huge_tree=True)

    # Parse the XML data
    try:
        tree = ET.ElementTree(ET.fromstring(data, parser=parser))
        # Check if the XML is well-formed
        ET.tostring(tree.getroot(), encoding='utf8')
    except (ET.ParseError, ET.ElementTree.ParseError, ET.TreeBuilderTargetError):
        return "Invalid XML", 400
    
    # Convert the parsed XML to string
    xml_str = ET.tostring(tree.getroot(), encoding='utf8').decode('utf8')

    return xml_str