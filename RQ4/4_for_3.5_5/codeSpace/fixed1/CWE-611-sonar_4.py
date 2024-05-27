from defusedxml.sax import make_parser
import xml.sax

class CustomContentHandler(xml.sax.ContentHandler):
    def __init__(self):
        super().__init__()
        self.root = None  # Variable to store the root element

    def startElement(self, name, attrs):
        if self.root is None:
            self.root = name  # Capture the root element

    def getRoot(self):
        return self.root

def get_root():
    '''
    Create an XML parser,
    parse the file 'resources/config.xml' and return the root element of the XML.
    '''

    # Create an instance of the custom XML handler
    handler = CustomContentHandler()

    # Create a parser object
    parser = make_parser()

    # Set the content handler for the parser
    parser.setContentHandler(handler)

    # Try to parse the XML file with error handling
    try:
        parser.parse('resources/config.xml')
    except xml.sax.SAXException as e:
        print(f"Error during XML parsing: {e}")
        return None

    # Return the root element name
    return handler.getRoot()

# Example: Print the root element of the XML file
if __name__ == "__main__":
    root = get_root()
    print(f"Root element: {root}")