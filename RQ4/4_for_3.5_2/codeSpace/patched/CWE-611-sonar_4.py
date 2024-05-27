import xml.sax

def get_root():
    """
    Create an XML parser,
    parse the file 'resources/config.xml' and return the parsed result.
    """
    # Create a SAX parser
    parser = xml.sax.make_parser()

    # Create a handler to handle XML events
    handler = xml.sax.ContentHandler()

    # Set the handler for the parser
    parser.setContentHandler(handler)

    # Parse the XML file
    parser.parse('resources/config.xml')

    # Return the root element of the parsed result
    return handler.root