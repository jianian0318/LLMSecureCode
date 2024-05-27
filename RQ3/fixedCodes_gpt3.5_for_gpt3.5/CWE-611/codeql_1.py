from flask import Flask, request
import lxml.etree

app = Flask(__name__)

@app.post("/upload")
def upload():
    xml_src = request.form.get('xml_src')
    parser = lxml.etree.XMLParser(resolve_entities=False)
    root = lxml.etree.fromstring(xml_src, parser)
    return lxml.etree.tostring(root)