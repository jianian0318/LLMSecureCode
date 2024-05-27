from defusedxml import lxml as defused_lxml
from flask import request

@app.route('/upload', methods=['POST'])
def upload():
    if 'xml_src' in request.files:
        xml_file = request.files['xml_src']
        xml_data = xml_file.read()
        xml_tree = defused_lxml.fromstring(xml_data)
        return defused_lxml.tostring(xml_tree, encoding='unicode')
    else:
        return 'No file uploaded'