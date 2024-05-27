from flask import Flask, request
import lxml.etree

app = Flask(__name__)

@app.route("/upload", methods=['POST'])
def upload():
    '''
    Get the xml_src from the request, parse it and return it as string.
    '''
    xml_src = request.data  # Get the xml from the request 
    root = lxml.etree.fromstring(xml_src)  # Parse the xml_src
    return lxml.etree.tostring(root, pretty_print=True).decode()  # Return it as string

if __name__ == "__main__":
    app.run()