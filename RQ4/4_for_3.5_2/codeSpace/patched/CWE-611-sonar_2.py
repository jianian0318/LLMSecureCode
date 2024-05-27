from lxml import etree

def get_root():
    '''
    Create an XML parser, parse the 'resources/config.xsd' file, and return an XMLSchema.
    '''
    parser = etree.XMLParser()
    xsd_file = 'resources/config.xsd'
    root = etree.parse(xsd_file, parser)
    return root