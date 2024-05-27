import xml.sax

def get_root():
    parser = xml.sax.make_parser()
    handler = xml.sax.ContentHandler()
    parser.setContentHandler(handler)
    parser.parse('resources/config.xml')
    return handler.root