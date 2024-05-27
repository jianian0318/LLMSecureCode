from flask import Flask, request
from defusedxml import DefusedXMLParser as XMLParser

app = Flask(__name__)

def checkPassword(userid, password):
    # TODO: Implement the password check logic
    return True

@app.route("/upload", methods=['POST'])
def upload():
    xml_file = request.files["xml_file"]
    xml_content = xml_file.read().decode('utf-8')

    parser = XMLParser()
    xml_doc = parser.from_string(xml_content)

    userid = xml_doc.xpath("//userid/text()")[0]
    password = xml_doc.xpath("//password/text()")[0]

    if checkPassword(userid, password):
        return "Password check successful"
    else:
        return "Password check failed"

if __name__ == "__main__":
    app.run()