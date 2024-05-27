from flask import Flask, request
from werkzeug.utils import secure_filename
import defusedxml.ElementTree as ET

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    if 'xml_file' not in request.files:
        return 'No file part in the request', 400
    xml_file = request.files['xml_file']
    if xml_file.filename == '':
        return 'No selected file', 400

    # Require the filename to be secure to prevent CWE-643
    xml_filename = secure_filename(xml_file.filename)

    try:
        # Use defusedxml.ElementTree.parse to prevent CWE-20
        xml_tree = ET.parse(xml_file)

        xml_string = ET.tostring(xml_tree.getroot(), encoding='utf-8', method='xml')

        return xml_string
    except ET.ParseError as e:
        # handling XML parsing errors
        return 'Invalid XML file, error occurred.', 400

if __name__ == '__main__':
    app.run(debug=False)