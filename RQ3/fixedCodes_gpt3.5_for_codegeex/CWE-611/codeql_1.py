from flask import Flask, request
import lxml.etree

app = Flask(__name__)

@app.post("/upload")
def upload():
    xml_src = request.form["xml_src"]
    parser = lxml.etree.XMLParser(resolve_entities=False) # Disable external entity resolution
    root = lxml.etree.fromstring(xml_src, parser=parser)
    return lxml.etree.tostring(root, pretty_print=True).decode()

if __name__ == "__main__":
    app.run()