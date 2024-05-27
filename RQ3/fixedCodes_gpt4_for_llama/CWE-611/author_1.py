from flask import Flask, request
from lxml import etree

app = Flask(__name__)


def checkPassword(userid, password):
    # TODO: Implement your password checking logic here
    pass


@app.route("/upload", methods=['POST'])
def upload():
    xml_file = request.files['xml']
    xml_content = xml_file.read()

    parser = etree.XMLParser(resolve_entities=False)
    xml_tree = etree.fromstring(xml_content, parser) 

    userid = xml_tree.find('userid').text
    password = xml_tree.find('password').text

    if checkPassword(userid, password):
        # TODO: Handle the upload logic here
        pass
    else:
        # TODO: Handle the error case here
        pass

if __name__ == '__main__':
    app.run()