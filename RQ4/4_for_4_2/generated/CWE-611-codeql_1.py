from flask import Flask, request
from defusedxml.lxml import fromstring  # Importing defusedxml's fromstring function

app = Flask(__name__)

@app.route("/upload", methods=['POST'])
def upload():
    # Get the xml_src from the request
    xml_src = request.get_data().decode('utf-8')

    # Parse the XML content and convert it into a string
    try:
        # Using defusedxml to safely parse the XML data
        tree = fromstring(xml_src)
        xml_as_string = etree.tostring(tree, pretty_print=True).decode()
    except etree.XMLSyntaxError:
        # Return a generic error message without leaking information
        return "Invalid XML format detected."

    return xml_as_string

# Add if clause to only run the app when the script is run directly.
# And remember to turn off debugging when deploying
if __name__ == "__main__":
    app.run(debug=False)