import defusedxml.sax

class MyHandler(defusedxml.sax.handler.ContentHandler):
    def startElement(self, name, attrs):
        # define behavior for start of element here
        pass

    def endElement(self, name):
        # define behavior for end of element here
        pass

    def characters(self, content):
        # define behavior for processing text inside element here
        pass

def get_root():
    '''
    Create an XML parser, parse the file 'resources/config.xml' and return the parsed result.
    '''
    handler = MyHandler()
    parser = defusedxml.sax.parse('resources/config.xml', handler=handler)
    return handler.root  # assumes MyHandler has 'root' attribute

if __name__ == '__main__':
    root = get_root()
    print(root)