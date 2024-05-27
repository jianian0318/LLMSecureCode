from flask import Flask, request
from lxml import etree

app = Flask(__name__)

@app.route("/upload", methods = ['POST'])
def upload():
    '''
    Get the xml_src from the request, parse it and return it as string after preventing XXE attack.
    '''
    # Acquiring xml_src from the request body
    xml_src = request.data
    # Parsing with denying access to external entities
    parser = etree.XMLParser(resolve_entities=False)
    # Create XML tree
    xml_tree = etree.fromstring(xml_src, parser)
    # Return parsed xml_src without external entity
    return etree.tostring(xml_tree, pretty_print=True).decode()

if __name__ == "__main__":
    app.run()