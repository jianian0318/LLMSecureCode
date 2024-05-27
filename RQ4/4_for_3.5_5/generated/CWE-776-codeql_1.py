    @app.route("/upload", methods=["POST"])
    def upload():
        '''
        Reads the XML from the incoming request.
        Parse it and return.
        '''
        # Get the XML data from the request
        xml_data = request.data

        # Parse the XML data
        root = ET.fromstring(xml_data)

        # Return the parsed XML data
        return ET.tostring(root)