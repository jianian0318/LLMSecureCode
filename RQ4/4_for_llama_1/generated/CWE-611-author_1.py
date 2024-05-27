from flask import Flask, request
from defusedxml.ElementTree import parse
import io

app = Flask(__name__)

def checkPassword(userid, password):
    # Check if the userid and password are correct
    # Return True if correct, False otherwise
    pass

@app.post("/upload")
def upload():
    # Get the XML file from the request
    xml_file = request.files['xml_file']

    # Parse the XML file
    xml_tree = parse(io.BytesIO(xml_file.read()))

    # Extract the userid and password from the XML file
    userid = xml_tree.find('userid').text
    password = xml_tree.find('password').text

    # Check the password
    if checkPassword(userid, password):
        return "Password is correct"
    else:
        return "Password is incorrect"

if __name__ == "__main__":
    app.run()