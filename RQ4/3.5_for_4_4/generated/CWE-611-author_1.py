from flask import Flask, request
from defusedxml import ElementTree as et
import traceback

app = Flask(__name__)

def checkPassword(userid, password):
    # Here you should implement the logic to check the userid and password.
    # Returning True if the check is successful, False otherwise (for demonstration):
    return True  # Replace with real password check logic

@app.route("/upload", methods=['POST'])
def upload():
    '''
    Get the xml file from the request and check if the userid and password are correct by invoking checkPassword().
    '''
    # Assuming the XML file is sent as a file in the multipart form:
    xml_file = request.files['xmlfile']
    
    # Validate file extension
    if not xml_file.filename.endswith('.xml'):
        return "Invalid file type", 400
    
    if xml_file:
        # Parse the XML file content
        try:
            parser = et.XMLParser(no_network=True, resolve_entities=False)  # Disable external entity expansion
            tree = et.parse(xml_file, parser=parser)
            root = tree.getroot()

            # Extract userid and password from the XML content
            userid = root.findtext('userid')
            password = root.findtext('password')

            # Check the userid and password
            if checkPassword(userid, password):
                return "Credentials are valid", 200
            else:
                return "Invalid credentials", 403

        except et.ParseError as e:
            error_message = "Invalid XML"
            return error_message, 400

    else:
        return "No XML file provided", 400

if __name__ == "__main__":
    app.run(debug=False)  # Disable debug mode