from flask import Flask, request
from lxml import etree

app = Flask(__name__)

def checkPassword(userid, password):
    if userid == "admin" and password == "123456":
        return True
    else:
        return False

@app.route('/upload', methods=['POST'])
def upload():
    xml_data = request.files["file"]
    parser = etree.XMLParser(no_network=True)
    root = etree.fromstring(xml_data.read(), parser)
    userid = root.findtext("userid")
    password = root.findtext("password")
  
    if checkPassword(userid, password):
        return "密码正确"
    else:
        return "密码错误"

if __name__ == "__main__":
    app.run()