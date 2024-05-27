from flask import Flask, request
from flask import secure_filename
from defusedxml.lxml import parse as defused_parse

app = Flask(__name__)

@app.route("/upload", methods=['POST'])
def upload():
    file = request.files['file']
    filename = secure_filename(file.filename)  # Securing the filename
    xml_src = file.stream
    # Using defusedxml for parsing xml file
    xml_tree = defused_parse(xml_src)
    xml_str = etree.tostring(xml_tree, pretty_print=True)
    return xml_str

if __name__ == "__main__":
    app.run()