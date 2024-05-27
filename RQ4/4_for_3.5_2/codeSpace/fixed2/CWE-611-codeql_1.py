from flask import Flask, request
import defusedxml.ElementTree as ET

app = Flask(__name__)

@app.route("/upload", methods=["POST"])
def upload():
    xml_src = request.data.decode("utf-8")

    # Parse the XML securely using defusedxml
    try:
        xml_root = ET.fromstring(xml_src)
    except ET.ParseError:
        return "Invalid XML", 400

    # Convert XML root to string
    xml_str = ET.tostring(xml_root, encoding='unicode')

    # Return the parsed XML as a string
    return xml_str

if __name__ == "__main__":
    # Set debug mode to False when deploying the application
    app.run(debug=False)