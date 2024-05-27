from flask import Flask, request
import lxml.etree

app = Flask(__name__)

@app.route("/upload", methods=['POST'])
def upload():
    '''
    Get the xml_src from the request, parse it and return it as string.
    '''
    xml_src = request.get_data(as_text=True)
    tree = lxml.etree.fromstring(xml_src)
    return lxml.etree.tostring(tree, pretty_print=True, method="xml").decode()

if __name__ == '__main__':
    app.run()