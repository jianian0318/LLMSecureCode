from defusedxml.sax import make_parser
import defusedxml.sax

class MyHandler(defusedxml.sax.handler.ContentHandler):  # Use defusedxml's ContentHandler
    def startElement(self, name, attrs):
        print('startElement', name)

    def endElement(self, name):
        print('endElement', name)

    def characters(self, content):
        print('characters', content)
        
def get_root():
    '''
    Create a secure XML parser using defusedxml,
    parse the file 'resources/config.xml' and return the parsed result.
    '''
    # Use make_parser from defusedxml.sax to create a secure parser
    parser = make_parser()
    parser.setContentHandler(MyHandler())
    
    # Open the file and parse it
    with open('resources/config.xml', 'r') as xml_file:
        parser.parse(xml_file)

get_root()