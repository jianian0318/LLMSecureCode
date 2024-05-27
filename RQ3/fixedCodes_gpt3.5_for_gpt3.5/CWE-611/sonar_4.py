import xml.sax

class MyHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.root = None
    
    def startElement(self, name, attrs):
        if name == 'root':
            self.root = name
    
def get_root():
    parser = xml.sax.make_parser()
    handler = MyHandler()
    parser.setContentHandler(handler)
    parser.parse('resources/config.xml')
    return handler.root