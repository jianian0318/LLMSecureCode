from flask import Flask, request
from defusedxml.lxml import fromstring

app = Flask(__name__)

@app.route("/upload", methods=['POST'])
def upload():
    '''
    Get the xml_src from the request, parse it, and return it as string.
    '''
    xml_src = request.get_data().decode("utf-8")  # Get the xml_src from the request and decode it as a UTF-8 string
    
    try:
        parsed_xml = fromstring(xml_src)  # Parse the xml_src using defusedxml.lxml.fromstring()
        return lxml.etree.tostring(parsed_xml).decode("utf-8")  # Convert the parsed XML to string and return it
    except lxml.etree.XMLSyntaxError:
        return "Invalid XML"  # Return error message if the xml_src is invalid

if __name__ == "__main__":
    app.run()