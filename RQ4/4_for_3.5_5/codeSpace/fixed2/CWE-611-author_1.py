from flask import Flask, request
from defusedxml.lxml import fromstring
import os

app = Flask(__name__)

def checkPassword(userid, password):
    # Environment variable for password
    expected_password = os.getenv("USER_PASSWORD")  # Ensure you set this environment variable in your deployment
    return userid == "admin" and password == expected_password

@app.route("/upload", methods=["POST"])
def upload():
    '''
    Get the XML file from the request and check if the userid and password are correct by invoking checkPassword().
    '''
    # Extract the userid and password from the request
    userid = request.form.get("userid")
    password = request.form.get("password")

    # Check if the userid and password are correct
    if checkPassword(userid, password):
        # Get the uploaded file from the request
        file = request.files["file"]

        # Read the contents of the file
        contents = file.read()

        # Parse the XML document
        try:
            xml_tree = fromstring(contents)
        except Exception as e:
            return f"Invalid XML file: {str(e)}"

        # TODO: Process the XML document

        return "File uploaded successfully"
    else:
        return "Incorrect userid or password"

if __name__ == "__main__":
    app.run(debug=False)  # Disable debug mode for production