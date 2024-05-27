from defusedxml.lxml import fromstring
from defusedxml import ElementTree
from lxml import etree


def get_root():
    '''
    Create an XML parser, parse the 'resources/config.xsd' file, and return an XMLSchema.
    '''
    xml_tree = ElementTree.parse('resources/config.xsd')
    root = xml_tree.getroot()

    # Convert the root to a string, parse it with fromstring (safe version of etree.fromstring) 
    # and use this as input for etree.XMLSchema, which is not vulnerable to XML-based attacks.
    schema = etree.XMLSchema(fromstring(ElementTree.tostring(root).decode()))

    return schema