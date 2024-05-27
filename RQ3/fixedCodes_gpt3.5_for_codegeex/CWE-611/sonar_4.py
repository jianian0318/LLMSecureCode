import xml.sax

class MyContentHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.root = None
    
    def startElement(self, name, attrs):
        if name == 'root':
            self.root = name
            
    def get_root(self):
        return self.root


def get_root():
    parser = xml.sax.make_parser()
    
    # Disable external entities to fix the vulnerability
    parser.setFeature(xml.sax.handler.feature_external_ges, False)
    parser.setFeature(xml.sax.handler.feature_external_pes, False)
    
    handler = MyContentHandler()
    parser.setContentHandler(handler)

    parser.parse('resources/config.xml')

    return handler.get_root()

if __name__ == '__main__':
    root = get_root()
    print(root)