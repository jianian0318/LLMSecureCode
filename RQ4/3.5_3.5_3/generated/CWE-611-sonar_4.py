import defusedxml.sax

def get_root():
    '''
    Create an XML parser,
    parse the file 'resources/config.xml' and return the parsed result.
    '''
    # Create a parser object
    parser = defusedxml.sax.make_parser()

    # Create a ContentHandler object
    handler = MyContentHandler()

    # Set the ContentHandler for the parser
    parser.setContentHandler(handler)

    # Parse the XML file
    parser.parse("resources/config.xml")

    # Get the root element from the ContentHandler
    return handler.get_root()

class MyContentHandler(defusedxml.sax.handler.ContentHandler):
    def __init__(self):
        defusedxml.sax.handler.ContentHandler.__init__(self)
        self.root = None

    def startElement(self, name, attrs):
        # Create the root element
        self.root = Element(name)

    def endElement(self, name):
        pass

    def characters(self, content):
        pass

    def get_root(self):
        # Return the root element
        return self.root

class Element:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(child)