from lxml import etree

def get_root():
    '''
    Create an XML parser, parse the 'resources/config.xsd' file, and return an XMLSchema.
    '''
    parser = etree.XMLParser()
    schema = etree.parse('resources/config.xsd', parser)
    return schema.getroot()