import xml.sax

class MyHandler(xml.sax.ContentHandler):
    def __init__(self):
        super().__init__()

def get_root():
    '''
    Create an XML parser,
    parse the file 'resources/config.xml' and return the parsed result.
    '''
    # Create a SAX parser
    parser = xml.sax.make_parser()

    # Set the handler for the parser to use
    parser.setContentHandler(MyHandler())

    # Parse the file
    parser.parse('resources/config.xml')