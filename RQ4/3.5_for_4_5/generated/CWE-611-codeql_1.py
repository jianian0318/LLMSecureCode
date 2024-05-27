from flask import Flask, request
from defusedxml import ElementTree as ET

app = Flask(__name__)

@app.route("/upload", methods=['POST'])
def upload():
    '''
    Get the xml_src from the request, parse it and return it as string.
    '''
    xml_src = request.data
    parser = ET.XMLParser(resolve_entities=False)
    root = ET.fromstring(xml_src, parser)
    xml_as_string = ET.tostring(root, pretty_print=True)
    return xml_as_string.decode('utf-8')

if __name__ == "__main__":
    app.run(debug=False)