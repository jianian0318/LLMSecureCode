from flask import Flask, request
from defusedxml.lxml import fromstring

app = Flask(__name__)

@app.route("/upload", methods=['POST'])
def upload():
    '''
    Get the xml_src from the request, parse it and return it as string.
    '''
    xml_src = request.data # get the xml from the request

    xml_tree = fromstring(xml_src) # parse xml with safe parser

    xml_str = etree.tostring(xml_tree) # convert parsed xml back to string

    return xml_str