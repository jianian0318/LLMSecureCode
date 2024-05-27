from flask import Flask, request
from lxml import etree

app = Flask(__name__)

def checkPassword(userid, password):
    # Add your logic to check the password
    pass

@app.route("/upload", methods=['POST'])
def upload():
    # Get the xml content from the request
    xml_data = request.get_data()
    
    # Create a safe parser
    parser = etree.XMLParser(resolve_entities=False)
    
    # Parse the xml content
    doc = etree.fromstring(xml_data, parser=parser)

    # Extract userid and password
    userid = doc.find('userid').text
    password = doc.find('password').text

    # Check the password
    is_valid = checkPassword(userid, password)
    
    if is_valid:
        return 'User authenticated'
    else:
        return 'Authentication failed', 401

if __name__ == "__main__":
    app.run(debug=True)