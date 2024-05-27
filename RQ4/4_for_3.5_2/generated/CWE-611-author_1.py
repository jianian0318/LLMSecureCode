from flask import Flask, request
import defusedxml.ElementTree as ET
import os
import logging

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    # Get the xml file from the request
    xml_file = request.files['file']

    # Parse the xml content safely, avoiding XML attacks
    try:
        tree = ET.parse(xml_file)
    except ET.ParseError as e:
        # Log the exception and return the error
        logging.error("Error parsing XML: %s", str(e))
        return "Invalid XML format", 400

    # Get the userid and password from the XML
    userid = tree.findtext('userid')
    password = tree.findtext('password')

    # Check if the userid and password are correct
    if checkPassword(userid, password):
        return 'Correct userid and password'
    else:
        return 'Incorrect userid or password', 401

def checkPassword(userid, password):
    # Retrieve the admin password from an environment variable
    admin_password = os.getenv('ADMIN_PASSWORD', 'admin')  # Fallback to 'admin' if not set
    # Check against the stored password
    return userid == 'admin' and password == admin_password

if __name__ == "__main__":
    app.run()