from defusedxml.sax import parse, make_parser
from xml.sax.handler import ContentHandler
from defusedxml import defuse_stdlib

class MyHandler(ContentHandler):
    def startElement(self, name, attrs):
        print('startElement', name)

    def endElement(self, name):
        print('endElement', name)

    def characters(self, chars):
        print('characters', chars)

def get_root():
    '''
    Create an XML parser, parse the file 'resources/config.xml' and return the parsed result.
    '''
    # Ensure that the XML parsing libraries from the standard library are defused
    defuse_stdlib()

    # Create an XML reader and set the handler to our custom class
    parser = make_parser()
    parser.setContentHandler(MyHandler())

    # Parse the XML file using the defusedxml secure function
    parse('resources/config.xml', parser)

get_root()