from flask import Flask, request
import lxml.etree

app = Flask(__name__)

def checkPassword(userid, password):
    # Put actual password-checking process here
    pass

@app.route("/upload", methods=['POST'])
def upload():
    xmlfile = request.files['file']  # Assuming the file is uploaded under the key 'file'
    tree = lxml.etree.parse(xmlfile)
    root = tree.getroot()
    userid = root.find('userid').text
    password = root.find('password').text
    return 'Valid user' if checkPassword(userid, password) else 'Invalid user'


if __name__ == "__main__":
    app.run()