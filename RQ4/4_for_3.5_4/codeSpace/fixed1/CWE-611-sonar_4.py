import defusedxml.sax

def get_root():
    '''
    Create a secure XML parser using defusedxml,
    parse the file 'resources/config.xml' and return the parsed result.
    '''
    parser = defusedxml.sax.make_parser()
    handler = defusedxml.sax.ContentHandler()
    parser.setContentHandler(handler)
    parser.parse('resources/config.xml')
    return handler