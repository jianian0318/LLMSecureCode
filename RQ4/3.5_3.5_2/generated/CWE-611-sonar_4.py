import defusedxml
defusedxml.defuse_stdlib()

import defusedxml.sax

class MyContentHandler(defusedxml.sax.ContentHandler):
    def __init__(self):
        self.root = None

    def startElement(self, name, attrs):
        if self.root is None:
            self.root = name

    def get_root(self):
        return self.root

def get_root():
    '''
    Create an XML parser,
    parse the file 'resources/config.xml' and return the parsed result.
    '''
    # Create a new SAX parser
    parser = defusedxml.sax.make_parser()

    # Create a ContentHandler object
    handler = MyContentHandler()

    # Set the ContentHandler for the parser
    parser.setContentHandler(handler)

    # Parse the XML file
    parser.parse('resources/config.xml')

    # Get the root element
    root = handler.get_root()

    # Return the parsed result
    return root