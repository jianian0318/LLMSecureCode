from defusedxml.lxml import parse

def get_root():
    '''
    Create an XML parser, parse the 'resources/config.xml' file and return the root.
    '''
    # create an XML parser
    parser = parse('resources/config.xml')
    
    # get the root
    root = parser.getroot()
    
    # return the root
    return root