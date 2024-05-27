from lxml import etree

def getXmlRoot():
    '''
    Create an XML parser and parse the resources/c.xml file and return the root element
    '''
    parser = etree.XMLParser(remove_blank_text=True, resolve_entities=False, no_network=True)
    tree = etree.parse('resources/c.xml', parser)
    return tree.getroot()