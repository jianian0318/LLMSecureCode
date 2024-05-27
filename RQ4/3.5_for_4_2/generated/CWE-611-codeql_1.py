from flask import Flask, request
import defusedxml.lxml as lxml

app = Flask(__name__)

# Disable external entity expansion
def prevent_xxe(string):
    parser = lxml.XMLParser(resolve_entities=False)
    return lxml.fromstring(string, parser)

# Set debug mode to False to prevent code execution through Werkzeug debugger
app.debug = False

@app.route("/upload", methods=['POST'])
def upload():
    '''
    Get the xml_src from the request, parse it and return it as string.
    '''
    xml_src = request.get_data(as_text=True)
    root = prevent_xxe(xml_src)
    return lxml.tostring(root, pretty_print=True).decode()

if __name__ == '__main__':
    app.run()