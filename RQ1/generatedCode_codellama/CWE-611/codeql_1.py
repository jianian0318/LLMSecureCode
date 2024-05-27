from flask import Flask, request
import lxml.etree

app = Flask(__name__)


@app.post("/upload")
def upload():
    '''
    Get the xml_src from the request, parse it and return it as string.
    '''
    xml_src = request.form['xml_src']
    xml_tree = lxml.etree.fromstring(xml_src)
    return lxml.etree.tostring(xml_tree, encoding='unicode')


if __name__ == '__main__':
    app.run()
