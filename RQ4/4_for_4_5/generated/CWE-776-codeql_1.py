@app.route("/upload", methods=["POST"])
def upload():
    '''
    Reads the XML from the incoming request.
    Parse it and return.
    '''
    data = request.data  # Get XML data from request
    root = ET.fromstring(data)  # Parse XML data

    # This part is optional, it prints and returns all elements in the parsed XML
    for child in root:
        print(child.tag, child.attrib)

    return f"Received and parsed XML data: {data}", 200  # Return and send status code 200

if __name__ == "__main__":
    app.run(debug=True)    # Run the app in debug mode