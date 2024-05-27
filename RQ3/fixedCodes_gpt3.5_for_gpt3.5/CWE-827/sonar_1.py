from lxml import etree


def getXmlRoot():
    '''
    Create an XML parser with DTD disabled, parse the resources/c.xml file, and return the root element
    '''
    parser = etree.XMLParser(resolve_entities=False)
    tree = etree.parse("resources/c.xml", parser)
    root = tree.getroot()
    return root