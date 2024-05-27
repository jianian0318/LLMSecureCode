import xml.sax

def get_root():
    class MyHandler(xml.sax.ContentHandler):
        def startElement(self, name, attrs):
            print('startElement', name)
        def endElement(self, name):
            print('endElement', name)
        def characters(self, content):
            print('characters', content)

    parser = xml.sax.make_parser()
    parser.setContentHandler(MyHandler())
    parser.parse('resources/config.xml')

get_root()