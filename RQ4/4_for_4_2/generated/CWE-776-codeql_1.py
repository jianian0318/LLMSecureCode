from flask import Flask, request, jsonify
from defusedxml.ElementTree import parse, ParseError

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    '''
    Reads the XML from the incoming request.
    Parse it and return.
    '''
    # Read the XML data from the request
    xml_data = request.data

    # Parse the XML data
    try:
        root = parse(xml_data)
    except ParseError:
        # If the XML data is malformed, return an error
        return jsonify({'error': 'Invalid XML'}), 400

    # Generate a response from the XML data
    # For demonstration, let's just return a simple dict with the root tag
    response = {
        'root_tag': root.tag,
        'root_text': root.text,
    }

    # Return the response as JSON
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=False)