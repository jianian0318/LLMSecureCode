from flask import Flask, request
from defusedxml.lxml import fromstring

app = Flask(__name__)

@app.route("/upload", methods=['POST'])
def upload():
    '''
    Get the xml_src from the request, parse it and return it as string.
    '''
    xml_src = request.form.get('xml_src')
    root = fromstring(xml_src)
    return lxml.etree.tostring(root)

if __name__ == "__main__":
    app.run(debug=True)