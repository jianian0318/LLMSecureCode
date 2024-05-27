from defusedxml import DefusedExpatParser
from lxml import etree

def get_root():
    """
    Create an XML parser, parse the 'resources/config.xsd' file, and return an XMLSchema.
    This now uses defusedxml to safely parse the XML file.
    """
    parser = DefusedExpatParser()
    schema = etree.XMLSchema(etree.fromstring(open('resources/config.xsd').read(), parser=parser))
    return schema.getroot()