from flask import Flask, request
from defusedxml import defusedxml
from defusedxml.lxml import parse

# Initialize the Flask application
app = Flask(__name__)

# Define the route for the upload
@app.post("/upload")
def upload():
    '''
    Get the xml_src from the request, parse it, and return it as string.
    '''
    # Assume the XML file is sent as an attached file in the POST request.
    xml_file = request.files['file'] # The name 'file' may vary based on client implementation.
    
    # Parse the XML file
    xml_data = parse(xml_file)

    # Convert the parsed XML to a string
    xml_string = etree.tostring(xml_data)

    # Make sure to return as a response that's appropriate for XML MIME type
    return app.response_class(xml_string, mimetype='text/xml')

# Run the app when the script is executed
if __name__ == "__main__":
    app.run(debug=False)