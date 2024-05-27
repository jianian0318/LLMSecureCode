import lxml.etree as etree


def getXmlRoot():
    parser = etree.XMLParser(resolve_entities=False)
    tree = etree.parse('resources/c.xml', parser)
    root = tree.getroot()
    return root