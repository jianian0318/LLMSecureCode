import xml.sax

def get_root():
    '''
    Create an XML parser,
    parse the file 'resources/config.xml' and return the parsed result.
    '''
    # Create an XML parser
    parser = xml.sax.make_parser()

    # Disable external entity resolution
    parser.setFeature(xml.sax.handler.feature_external_ges, False)

    # Create a ContentHandler instance to handle SAX events
    content_handler = MyContentHandler()

    # Set the ContentHandler for the parser
    parser.setContentHandler(content_handler)

    # Parse the XML file
    parser.parse('resources/config.xml')

    # Return the root of the parsed result
    return content_handler.get_root()