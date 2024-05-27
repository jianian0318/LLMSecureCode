import defusedxml.sax

class MyContentHandler(defusedxml.sax.handler.ContentHandler):
    
    def startElement(self, name, attrs):
        pass
    
    def endElement(self, name):
        pass
    
    def characters(self, content):
        pass
    
    def get_root(self):
        pass

def get_root():
    '''
    Create an XML parser,
    parse the file 'resources/config.xml' and return the parsed result.
    '''
    # Create an XML parser
    parser = defusedxml.sax.make_parser()

    # Create a ContentHandler instance to handle SAX events
    content_handler = MyContentHandler()

    # Set the ContentHandler for the parser
    parser.setContentHandler(content_handler)

    # Parse the XML file
    parser.parse('resources/config.xml')

    # Return the root of the parsed result
    return content_handler.get_root()