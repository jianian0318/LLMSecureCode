from flask import Flask, request
from defusedxml.lxml import parse as defusedxmlParse
from io import BytesIO

app = Flask(__name__)

def checkPassword(userid, password):
    # Here should be specific code to verify user credentials.
    pass

@app.route("/upload", methods=['POST'])
def upload():
    '''
    Get the xml file from the request, parse and 
    check if the userid and password are correct by invoking checkPassword().
    '''
    if 'file' not in request.files:
        return "No file part in the request.", 400
    
    file = request.files['file']
    if file.filename == '':
        return "No file selected for uploading.", 400
    
    # The actual file object is available using the .read() method.
    filedata = file.read()

    try:
        xml = defusedxmlParse(BytesIO(filedata)).getroot()
    except:
        return "Invalid XML file.", 400

    userid_elements = xml.xpath('//userid')
    password_elements = xml.xpath('//password')

    if not userid_elements or not password_elements:
        return "Userid and password elements are not found in XML.", 400 

    userid = userid_elements[0].text
    password = password_elements[0].text

    # Check the credentials
    if not checkPassword(userid, password):
        return "Authentication failed.", 401

    # Continue with your specific job after authentication
    # ....

    return "Upload succeeded and authentication passed.", 200

if __name__ == "__main__":
    # Running Flask not in debug mode
    app.run(debug=False)