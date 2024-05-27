import defusedxml.sax as safe_sax

class MyHandler(safe_sax.ContentHandler):
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
    handler = MyHandler()
    parser = safe_sax.make_parser()
    parser.setContentHandler(handler)
    parser.parse('resources/config.xml')