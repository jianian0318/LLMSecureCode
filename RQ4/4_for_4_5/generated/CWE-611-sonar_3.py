from defusedxml import DefusedXMLParser
from lxml import etree

def transform_xml(filename):
    """
    Create an XML parser, parse the 'resources/config.xsl' file,
    and return an XSLT object
    """
    # Create a defused XML parser
    parser = DefusedXMLParser()

    # Parse the xml file using defusedxml
    with open(filename, 'r') as xml_content:
        tree = parser.parse(xml_content)

    # Ensure the input is sanitized and trusted before this step
    # WARNING: The next line still uses lxml and could be a security risk if the input XML is not safe
    xslt_root = etree.XML(etree.tostring(tree.getroot()))
    transform = etree.XSLT(xslt_root)

    return transform