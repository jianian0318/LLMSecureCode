from flask import Flask, request
from defusedxml.ElementTree import fromstring, tostring

app = Flask(__name__)

@app.route("/upload", methods=['POST'])
def upload():
    '''
    Reads the XML from the incoming request.
    Parse it and return.
    '''
    if request.data:
        try:
            xml_data = request.data
            root = fromstring(xml_data)  # Use defusedxml's fromstring

            # Convert the Element Tree back into XML and return
            xmlstr = tostring(root, encoding='utf8').decode('utf8')
            return xmlstr
        except Exception as e:
            return "Error: " + str(e)
    else:
        return "No data posted"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000)  # Bind to localhost instead of all interfaces