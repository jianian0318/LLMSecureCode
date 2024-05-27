from flask import Flask, request
from defusedxml import lxml

app = Flask(__name__)

def checkPassword(userid, password):
    # Actual password checking code here
    pass

@app.route("/upload", methods=['POST'])
def upload():
    '''
    Get the xml file from the request and check if the userid and password are correct by invoking checkPassword().
    '''
    # Fetch the xml file from request
    xml_file = request.files.get('file')
    if xml_file:
        # Safe parsing avoiding XXE using defusedxml
        tree = lxml.parse(xml_file)

        # Get userid and password from parsed xml file
        userid, password = tree.find('userid').text, tree.find('password').text

        # Check if provided userid and password are valid
        valid = checkPassword(userid, password)

        return 'Valid Password!' if valid else 'Invalid Password!'
    else:
        return "No xml file found in request!", 400

if __name__ == "__main__":
    # Removing debug mode to avoid exposure of Werkzeug debugger and possible arbitrary code execution
    app.run(debug=False)