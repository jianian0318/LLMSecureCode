from flask import Flask, request
from defusedxml.lxml import fromstring
from defusedxml.ElementTree import tostring

app = Flask(__name__)

@app.route("/upload", methods=['POST'])
def upload():
    xml_src = request.data   
    xml_tree = fromstring(xml_src)
    xml_str = tostring(xml_tree)
    return xml_str

if __name__ == "__main__":
    app.run()