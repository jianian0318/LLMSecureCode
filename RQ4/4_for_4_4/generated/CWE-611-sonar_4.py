from defusedxml.sax import make_parser
from defusedxml.sax import ContentHandler

class MyXMLHandler(ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.root = ""
        # set other elements to empty string 

    # Call when an element starts
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == 'root':
            print('*****Root*****')

    # Call when an elements ends
    def endElement(self, tag):
        if self.CurrentData == 'root':
            print('Root:', self.root)

    # Call when a character is read
    def characters(self, content):
        if self.CurrentData == 'root':
            self.root = content

def get_root():
    # create an XMLReader
    parser = make_parser()
    # turn off namepsaces
    parser.setFeature(ContentHandler.feature_namespaces, 0)

    # override the default ContextHandler
    Handler = MyXMLHandler()
    parser.setContentHandler( Handler )
    
    file_path = 'resources/config.xml'
    parser.parse(file_path)