from defusedxml import sax

def get_root():
    '''
    Create a safe XML parser, parse the file 'resources/config.xml' and return the parsed result.
    '''
    parser = sax.make_parser()
    handler = sax.handler.ContentHandler()
    parser.setContentHandler(handler)
    parser.parse('resources/config.xml')
    return handler  