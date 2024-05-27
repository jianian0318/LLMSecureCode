from flask import Flask, request
from defusedxml.lxml import parse

app = Flask(__name__)

def checkPassword(userid, password):
    # Dummy checkPassword function definition 
    # Replace this with actual logic to check user credentials
    return True

@app.route("/upload", methods=['POST'])
def upload():
    '''
    Get the xml file from the request and check if the userid and password are correct by invoking checkPassword().
    '''
    file = request.files.get('xmlfile')
    if not file:
        return "No xml file in request", 400
    try:
        tree = parse(file)
        root = tree.getroot()
        userid = root.find('userid').text
        password = root.find('password').text
        if checkPassword(userid, password):
            return "Access granted", 200
        else:
            return "Invalid userid or password", 401
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=False)