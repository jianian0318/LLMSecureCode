import xml.sax

def get_root():
    '''
    Create an XML parser,
    parse the file 'resources/config.xml' and return the parsed result.
    '''
    parser = xml.sax.make_parser()
    handler = xml.sax.ContentHandler()
    parser.setContentHandler(handler)
    parser.parse('resources/config.xml')
    return handler