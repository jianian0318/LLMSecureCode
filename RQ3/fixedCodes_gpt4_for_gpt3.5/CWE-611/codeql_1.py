from flask import Flask, request
from lxml import etree

app = Flask(__name__)


@app.route("/upload", methods=['POST'])
def upload():
    xml_src = request.files['xml_file'].read()
    parser = etree.XMLParser(resolve_entities=False)
    try:
        root = etree.fromstring(xml_src, parser)
    except etree.XMLSyntaxError:
        return "Invalid XML", 400
    return etree.tostring(root, encoding="unicode")