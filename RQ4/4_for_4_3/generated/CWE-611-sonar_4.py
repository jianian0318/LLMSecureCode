from defusedxml.sax import make_parser
import defusedxml.sax as sax

class MyHandler(sax.ContentHandler):
    # Override the methods of this class according to your needs

    def startElement(self, name, attrs):
        print('startElement', name)

    def endElement(self, name):
        print('endElement', name)

    def characters(self, content):
        print('characters', content)

def get_root():
    """
    Create an XML parser, parse the file 'resources/config.xml' and return the parsed result.
    """
    parser = make_parser()
    parser.setContentHandler(MyHandler())
    parser.parse('resources/config.xml')

# Assuming 'resources/config.xml' exists
get_root()