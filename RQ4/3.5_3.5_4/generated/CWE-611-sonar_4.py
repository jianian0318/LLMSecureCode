import defusedxml.sax as parsed
import defusedxml.cElementTree as ElementTree

def get_root():
    # Create a secure XML parser
    parser = parsed.make_parser()

    # Create a ContentHandler
    handler = MyHandler()

    # Set the ContentHandler to the parser
    parser.setContentHandler(handler)

    # Parse the file 'resources/config.xml'
    with open('resources/config.xml', 'rb') as f:
        parser.parse(f)

    # Return the parsed result
    return handler.root

class MyHandler(parsed.ContentHandler):
    def __init__(self):
        parsed.ContentHandler.__init__(self)
        self.root = None

    def startElement(self, name, attrs):
        if self.root is None:
            self.root = name

    def endElement(self, name):
        pass

    def characters(self, content):
        pass