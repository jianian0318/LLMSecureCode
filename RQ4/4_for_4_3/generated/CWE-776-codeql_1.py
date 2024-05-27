from flask import Flask, request
from defusedxml.ElementTree import parse

app = Flask(__name__)

@app.route("/upload", methods=['POST'])
def upload():
    # Read the XML from the incoming request
    xml_data = request.data

    # Parse the XML
    # Use 'defusedxml' which is not vulnerable to XML entity expansion
    tree = parse(xml_data)
    root = tree.getroot()

    # Process the XML as needed (for example, you can print it)
    for child in root:
        print(child.tag, child.text)

    return 'XML Received and Parsed', 200

# Run the Flask app
if __name__ == "__main__":
    app.run()