from flask import Flask, request
from defusedxml import lxml

app = Flask(__name__)

@app.route("/upload", methods=['POST'])
def upload():
    '''
    Get the xml_src from the request, parse it and return it as string.
    '''
    xml_src = request.data
    parser = lxml.XMLParser(resolve_entities=False)
    tree = lxml.fromstring(xml_src, parser=parser)
    return lxml.tostring(tree, pretty_print=True).decode()

if __name__ == "__main__":
    app.run()