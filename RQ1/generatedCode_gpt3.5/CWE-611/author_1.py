from flask import Flask, request
import lxml.etree

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
    xml_root = lxml.etree.fromstring(xml_content)

    # Get the userid and password from the xml
    userid = xml_root.find('userid').text
    password = xml_root.find('password').text

    # Check if the userid and password are correct
    result = checkPassword(userid, password)

    return result