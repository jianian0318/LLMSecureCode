import defusedxml.sax as defused_sax

class MyHandler(defused_sax.ContentHandler):
    '''
    Define a custom handler class to handle different tasks during parsing.
    This is an empty handler that you will have to customize according to your needs.
    '''
    def startElement(self, tag, attributes):
        pass

    def endElement(self, tag):
        pass

    def characters(self, content):
        pass

def get_root():
    '''
    Create an XML parser, parse the file 'resources/config.xml' 
    and return the parsed result.
    '''
    handler = MyHandler()
    parser = defused_sax.make_parser()
    parser.setContentHandler(handler)

    try:
        parser.parse('resources/config.xml')
    except FileNotFoundError:
        print("File 'resources/config.xml' not found.")

    return handler