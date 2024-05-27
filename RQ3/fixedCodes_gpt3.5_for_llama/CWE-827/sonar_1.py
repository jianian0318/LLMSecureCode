from lxml import etree

def getXmlRoot():
    '''
    Create an XML parser with no DTD loading and parse the resources/c.xml file and return the root element
    '''
    parser = etree.XMLParser(remove_blank_text=True, dtd_validation=False, load_dtd=False)
    tree = etree.parse('resources/c.xml', parser)
    return tree.getroot()