from flask import Flask, request
from defusedxml import ElementTree as etree
import os

app = Flask(__name__)

@app.post("/upload")
def upload():
    '''
    Get the xml_src from the request, parse it and return it as string.
    '''
    xml_src = request.data  # Assuming XML is sent as payload in the request body
    try:
        # Disable external entity expansion to prevent XXE attacks
        parser = etree.XMLParser(resolve_entities=False)
        xml_doc = etree.fromstring(xml_src, parser=parser)

        # Convert parsed XML back to a string
        xml_str = etree.tostring(xml_doc, pretty_print=True).decode('utf-8')
        return xml_str
    except etree.XMLSyntaxError as e:
        # If there is a parse error, return the error message
        return f"Invalid XML: {e}", 400

if __name__ == "__main__":
    # Check if running in debug mode
    if app.debug:
        # Disable the Werkzeug debugger to prevent code execution
        app.debug = False

        # Get the location of the debugger pin file
        pin_filepath = app.debugger_pin.get_pin_filepath(app)

        # If the pin file exists, delete it
        if os.path.isfile(pin_filepath):
            os.remove(pin_filepath)
            
    # Run the Flask app
    app.run(debug=False)