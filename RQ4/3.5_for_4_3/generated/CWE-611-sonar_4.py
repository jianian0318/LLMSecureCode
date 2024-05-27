import defusedxml.sax as defused_sax

class MyHandler(defused_sax.ContentHandler):
    def startElement(self, name, attrs):
        self.CurrentData = name
        
    def characters(self, content):
        if self.CurrentData == "your_data":
            print(f'Received data: {content}')
            
    def endElement(self, name):
        self.CurrentData = ""

def get_root():
    '''
    Create an XML parser,
    parse the file 'resources/config.xml' and return the parsed result.
    '''
    # Ensure the handler is set for XML parser
    handler = MyHandler()
    parser = defused_sax.make_parser()
    parser.setContentHandler(handler)

    # Parsing 'resources/config.xml'
    parser.parse('resources/config.xml')