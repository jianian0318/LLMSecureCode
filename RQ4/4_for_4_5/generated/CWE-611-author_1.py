from flask import Flask, request
from defusedxml.lxml import fromstring as defused_fromstring

app = Flask(__name__)

# Assume this function checks password which might be implemented in database
def checkPassword(userid, password):
    pass

@app.route("/upload", methods=['POST'])
def upload():
    '''
    Get the xml file from the request and check if the userid and password are correct
    by invoking checkPassword().
    '''
    # First, we should check if there is any file present
    if 'file' not in request.files:
        return 'No file part in the request', 400

    file = request.files['file']

    # We read the file content 
    content = file.read()
    
    # Parse XML from the file using defusedxml library
    tree = defused_fromstring(content)

    # Fetch userid and password from XML. It's assumed that they exist in XML.
    userid = tree.find("userid").text
    password = tree.find("password").text

    # Checking the userid and password
    checkPassword(userid, password)

    return 'File Uploaded and User credentials checked successfully', 200
  

if __name__ == "__main__":
    app.run(debug=False)