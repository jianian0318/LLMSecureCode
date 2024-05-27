from flask import Flask, request
from defusedxml.lxml import fromstring

app = Flask(__name__)

@app.route("/upload", methods=['POST'])
def upload():
    xml_src = request.form.get('xml_src') 

    try:
        xml_doc = fromstring(xml_src)
        return etree.tostring(xml_doc)
    except etree.XMLSyntaxError:
        return 'Malformed XML'

if __name__ == "__main__":
    app.run()