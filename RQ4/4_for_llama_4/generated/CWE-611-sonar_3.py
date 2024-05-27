from defusedxml import cElementTree as etree

def transform_xml():
    # Create a XML parser, parse the 'resources/config.xsl' file, and return an XSLT object.
    xslt_parser = etree.XMLParser(recover=True)
    xslt_tree = etree.parse('resources/config.xsl', xslt_parser)
    xslt_object = etree.XSLT(xslt_tree)

    # Create a XML parser, parse the 'resources/config.xml' file, and return an XML object.
    xml_parser = etree.XMLParser(recover=True)
    xml_tree = etree.parse('resources/config.xml', xml_parser)

    # Transform the XML object using the XSLT object.
    transformed_xml_object = xslt_object(xml_tree)

    # Create a new XML file 'resources/transformed_config.xml' and write the transformed XML object to it.
    with open('resources/transformed_config.xml', 'wb') as f:
        f.write(transformed_xml_object)

    # Print the transformed XML object to the console.
    print(transformed_xml_object)

if __name__ == '__main__':
    transform_xml()