from flask import Flask, request
import xml.etree.ElementTree as ET

app = Flask(__name__)


@app.route("/upload", methods=['POST'])
def upload():
    xml_data = request.data
    parser = ET.XMLParser(resolve_entities=False) # Disable entity expansion
    root = ET.fromstring(xml_data, parser=parser)
    return f"Parsed XML: {ET.tostring(root).decode()}"


if __name__ == "__main__":
    app.run(debug=True)