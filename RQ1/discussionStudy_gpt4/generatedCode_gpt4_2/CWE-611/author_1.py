from flask import Flask, request
import lxml.etree

app = Flask(__name__)

def checkPassword(userid, password):
    # Check the credentials
    # This is an example, you should replace it with your actual checking process
    if userid == "admin" and password == "123":
        return True
    else:
        return False

@app.route("/upload", methods=['POST'])
def upload():
    '''
    Get the xml file from the request and check if the userid and password are correct by invoking checkPassword().
    This assumes that the XML file will be in the request files and the userid and password will be in the request form.
    '''
    xml_file = request.files['file']
    userid = request.form['userid']
    password = request.form['password']

    if xml_file and userid and password:
        # Parse xml
        xml_data = lxml.etree.parse(xml_file)
        # You can add the logic here to extract information from xml if required

        # Validate credentials
        if checkPassword(userid, password):
            return 'Upload successful', 200
        else:
            return 'Incorrect userid or password', 401

    return 'Missing fields', 400

if __name__ == "__main__":
    app.run(debug=True)