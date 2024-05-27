import xml.sax

def get_root():
    '''
    Create an XML parser,
    parse the file 'resources/config.xml' and return the parsed result.
    '''

    # Create an instance of the XML handler
    handler = xml.sax.ContentHandler()

    # Create a parser object
    parser = xml.sax.make_parser()

    # Set the content handler for the parser
    parser.setContentHandler(handler)

    # Parse the XML file
    parser.parse('resources/config.xml')

    # Return the parsed result
    return handler.getRoot()