from lxml import etree


def getXmlRoot():
    parser = etree.XMLParser(remove_blank_text=True)
    tree = etree.parse('resources/c.xml', parser)
    root = tree.getroot()
    return root