import xml.sax

def get_root():
    '''
    Create an XML parser,
    parse the file 'resources/config.xml' and return the parsed result.
    '''
    # Create a new XML parser object
    parser = xml.sax.make_parser()

    # Disable namespace handling
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    # Create a new ContentHandler object
    handler = ContentHandler()

    # Set the ContentHandler for the parser
    parser.setContentHandler(handler)

    # Parse the XML file
    parser.parse("resources/config.xml")

    # Get the root element from the ContentHandler
    root = handler.root

    # Return the root element
    return root