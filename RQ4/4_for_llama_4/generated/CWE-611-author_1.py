from flask import Flask, request
from os.path import abspath, join, dirname
from defusedxml import lxml

app = Flask(__name__)

def checkPassword(userid, password):
    # Check if the userid and password are correct
    # Return True if correct, False otherwise
    pass

@app.post("/upload")
def upload():
    # Get the XML file from the request
    xml_file = request.files['xml_file'].read()

    # Disable external entity parsing
    parser = lxml.XMLParser(resolve_entities=False)
    try:
        # Parse the XML file from string source
        xml_tree = lxml.fromstring(xml_file, parser)
    except lxml.XMLSyntaxError:
        return "Invalid XML"

    # Extract the userid and password from the XML file
    userid = xml_tree.xpath('/user/userid')[0].text
    password = xml_tree.xpath('/user/password')[0].text

    # Check the userid and password
    is_correct = checkPassword(userid, password)

    # Return a response indicating the result of the password check
    if is_correct:
        return "Password is correct"
    else:
        return "Password is incorrect"

if __name__ == "__main__":
    # Run the server in a safe way
    app.run(host='127.0.0.1')