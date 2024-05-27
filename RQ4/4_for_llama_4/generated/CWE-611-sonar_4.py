from defusedxml import sax

def get_root():
    # Create an XML parser
    parser = sax.make_parser()
    # Parse the file 'resources/config.xml'
    parser.parse('resources/config.xml')
    # Get the parsed result
    return parser.getContentHandler()