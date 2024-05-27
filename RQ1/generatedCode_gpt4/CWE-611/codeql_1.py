from flask import Flask, request
import lxml.etree

app = Flask(__name__)


@app.route("/upload", methods=['POST'])
def upload():
    xml_string = request.data.decode("utf-8")
    parsed_xml = lxml.etree.fromstring(xml_string)
    xml_string = lxml.etree.tostring(parsed_xml, pretty_print=True).decode("utf-8")
    return xml_string

if __name__ == "__main__":
    app.run()