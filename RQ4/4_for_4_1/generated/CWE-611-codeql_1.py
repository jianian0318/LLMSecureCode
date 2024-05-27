from flask import Flask, request
from defusedxml import ElementTree as ET

app = Flask(__name__)

@app.route("/upload", methods=['POST'])
def upload():
    '''
    Get the xml_src from the request, parse it and return it as string.
    '''
    xml_src = request.get_data(as_text=True)
    try:
        xml_tree = ET.fromstring(xml_src)
    except ET.ParseError:
        return 'Invalid XML', 400 # Returns a 400 bad request error
    
    return ET.tostring(xml_tree, pretty_print=True, encoding='unicode')

if __name__ == "__main__":
    app.run(debug=False)