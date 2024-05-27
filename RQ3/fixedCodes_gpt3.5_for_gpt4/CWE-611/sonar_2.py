import os
from lxml import etree

def get_root():
    parser = etree.XMLParser(no_network=True)
    xsd_path = os.path.join('resources', 'config.xsd')
    with open(xsd_path, 'r') as file:
        xml_tree = etree.parse(file, parser)
    schema = etree.XMLSchema(xml_tree)
    return schema