import defusedxml
import defusedxml.sax

class MyHandler(defusedxml.sax.ContentHandler):
    def startElement(self, name, attrs):
        print('startElement', name)
    def endElement(self, name):
        print('endElement', name)
    def characters(self, content):
        print('characters', content)

def get_root():
    '''
    Create an XML parser,
    parse the file 'resources/config.xml' and return the parsed result.
    '''
    # Our MyHandler instance
    handler = MyHandler()
    
    # Create a SAX parser
    # Replace xml.sax.make_parser with defusedxml.sax.make_parser
    parser = defusedxml.sax.make_parser()
    
    # Set the SAX parser's content handler to our instance
    parser.setContentHandler(handler)
    
    # Parse the 'resources/config.xml' file
    parser.parse('resources/config.xml')

if __name__ == "__main__":
    defusedxml.defuse_stdlib()
    get_root()