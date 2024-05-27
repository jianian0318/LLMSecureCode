import os
from lxml import etree

def get_root():
    '''
    Create an XML parser, parse the 'resources/config.xsd' file, and return an XMLSchema.
    '''
    path = os.path.join(os.path.dirname(__file__), 'resources/config.xsd')

    with open(path, 'r') as file:
        schema_root = etree.XMLSchema(etree.parse(file))
    
    return schema_root