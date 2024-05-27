import xml.sax

def get_root():
    '''
    Create an XML parser,
    parse the file 'resources/config.xml' and return the parsed result.
    '''
    # Create a XMLReader
    parser = xml.sax.make_parser()

    # Set the ContentHandler
    handler = MyContentHandler()
    parser.setContentHandler(handler)

    # Parse the 'resources/config.xml' file
    parser.parse('resources/config.xml')

    return handler.get_root()

# Test the function
if __name__ == '__main__':
    root = get_root()
    print(root)
