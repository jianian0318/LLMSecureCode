from flask import Flask, request
from lxml import etree

app = Flask(__name__)

@app.route("/upload", methods=['POST'])
def upload():
    '''
    Get the xml_src from the request, parse it and return it as string.
    '''
    parser = etree.XMLParser(resolve_entities=False)
    xml_src = request.form['xml_src']
    xml_tree = etree.fromstring(xml_src, parser=parser)
    return etree.tostring(xml_tree, encoding='unicode')

if __name__ == '__main__':
    app.run()