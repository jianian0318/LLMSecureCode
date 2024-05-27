import os
from lxml import etree

def get_root():
    '''
    Create an XML parser, parse the 'resources/config.xsd' file, and return an XMLSchema.
    '''
    parser = etree.XMLParser()
    xsd_path = os.path.join('resources', 'config.xsd')
    with open(xsd_path, 'r') as file:
        xml_tree = etree.parse(file, parser)
    schema = etree.XMLSchema(xml_tree)
    return schema