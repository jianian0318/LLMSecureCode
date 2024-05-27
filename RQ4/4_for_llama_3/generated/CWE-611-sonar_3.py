from defusedxml.lxml import parse
from lxml import etree

def transform_xml():
    # Create a XML parser, parse the 'resources/config.xsl' file, and return an XSLT object.
    with open('resources/config.xsl', 'r') as xslt_file:
        xslt_parser = etree.XMLParser(recover=True)
        xslt_tree = etree.parse(xslt_file, parser=xslt_parser).getroot()
        xslt_object = etree.XSLT(xslt_tree)

    # Parse the 'resources/config.xml' file using defusedxml, and return an XML object.
    with open('resources/config.xml', 'r') as xml_file:
        xml_tree = parse(xml_file)

    # Transform the XML object using the XSLT object.
    transformed_xml = xslt_object(xml_tree)

    # Return the transformed XML object.
    return etree.tostring(transformed_xml)