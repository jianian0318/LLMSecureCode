from defusedxml import ElementTree
from flask import Flask, request

app = Flask(__name__)

@app.route("/upload", methods=['POST'])
def upload():
    '''
    Get the xml file from the request, parse it and return it as string.
    '''
    xml_src = request.files['xml_file'].read()  # get the xml file from the request form
    parsed_xml = ElementTree.fromstring(xml_src)  # parse the xml_src using defusedxml.ElementTree.fromstring()
    return ElementTree.tostring(parsed_xml).decode()  # return the parsed xml as string using defusedxml.ElementTree.tostring()

if __name__ == '__main__':
    app.run()