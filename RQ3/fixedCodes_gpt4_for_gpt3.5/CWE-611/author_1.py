from flask import Flask, request
from lxml import etree

app = Flask(__name__)

def checkPassword(userid, password):
    pass

@app.route("/upload", methods=['POST'])
def upload():
    '''
    Get the xml file from the request and check if the userid and password are correct by invoking checkPassword().
    '''
    # Get the xml file from the request
    xml_file = request.files['xml']

    # Parse the xml file
    xml_content = xml_file.read()

    # Create a safe parser
    parser = etree.XMLParser(resolve_entities=False)
    
    xml_root = etree.fromstring(xml_content, parser=parser)

    # Get the userid and password from the xml
    userid = xml_root.find('userid').text
    password = xml_root.find('password').text

    # Check if the userid and password are correct
    result = checkPassword(userid, password)

    return result