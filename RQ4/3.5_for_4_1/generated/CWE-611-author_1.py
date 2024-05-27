from flask import Flask, request
from defusedxml import etree

app = Flask(__name__)

def checkPassword(userid, password):
    pass  # To be implemented according to usage context

@app.route('/upload', methods=['POST'])
def upload():
    '''
    Get the xml file from the request and check if the userid and password are correct by invoking checkPassword().
    '''
    # Get the file from the post request
    file = request.files['file']

    # Verify file extension
    if not file.filename.endswith('.xml'):
        return 'Invalid file type'

    # Use defusedxml to parse the xml file with XMLParser
    parser = etree.XMLParser(
        no_network=True,  # Disable network access
        load_dtd=False,   # Disable DTD loading
        resolve_entities=False  # Disable entity resolving
    )
    tree = etree.parse(file.stream, parser)  # Use file.stream to parse the file instead of file

    # Get the user id and password from the xml file
    root = tree.getroot()
    userid = root.findtext('userid')
    password = root.findtext('password')

    # Invoke checkPassword with userid and password
    return checkPassword(userid, password)