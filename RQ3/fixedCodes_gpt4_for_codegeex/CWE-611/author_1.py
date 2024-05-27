from flask import Flask, request
from lxml import etree
from lxml.etree import parse, XMLParser

app = Flask(__name__)

def checkPassword(userid, password):
    # Add your password verification logic here
    if userid == "admin" and password == "123456":
        return True
    else:
        return False


@app.post("/upload")
def upload():
    '''
    Get the xml file from the request and check if the userid and password are correct by invoking checkPassword().
    '''
    # Get the xml file from the request
    xml_data = request.files["file"]
    # Parse xml file
    parser = XMLParser(resolve_entities=False)
    tree = parse(xml_data, parser)
    root = tree.getroot()
    # Get userid and password
    userid = root.find("userid").text
    password = root.find("password").text
    # Validate password
    if checkPassword(userid, password):
        return "Password Correct"
    else:
        return "Password Incorrect"

if __name__ == "__main__":
    app.run(port=5000)