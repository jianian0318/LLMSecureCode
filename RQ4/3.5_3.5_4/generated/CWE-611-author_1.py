from flask import Flask, request
from defusedxml import etree

app = Flask(__name__)


def checkPassword(userid, password):
    # TODO: Implement password check logic
    pass


@app.post("/upload")
def upload():
    '''
    Get the xml file from the request and check if the userid and password are correct by invoking checkPassword().
    '''

    # Get the xml file from the request
    xml_file = request.files['xml_file']

    # Parse the xml file using defusedxml.etree
    # Enable external entity expansion (XXE) protection
    parser = etree.XMLParser(resolve_entities=False, forbid_external=True, forbid_dtd=True)
    tree = etree.parse(xml_file, parser=parser)

    # Get the root element of the xml
    root = tree.getroot()

    # Get the userid and password from the xml
    userid = root.findtext('userid')
    password = root.findtext('password')

    # Check if the userid and password are correct
    if checkPassword(userid, password):
        return 'Success'
    else:
        return 'Failure'


if __name__ == '__main__':
    app.run()