from defusedxml import ElementTree

def transform_xml():
    # Parse the 'resources/config.xsl' file, and return an XSLT object.
    xslt_tree = ElementTree.parse('resources/config.xsl')
    xslt_object = ElementTree.XSLT(xslt_tree)

    #Parse the 'resources/config.xml' file, and return an XML object.
    xml_tree = ElementTree.parse('resources/config.xml')

    # Transform the XML object using the XSLT object.
    transformed_xml_object = xslt_object(xml_tree)

    # Create a new XML file 'resources/transformed_config.xml' and write the transformed XML object to it.
    with open('resources/transformed_config.xml', 'wb') as f:
        f.write(ElementTree.tostring(transformed_xml_object))

    # Print the transformed XML object to the console.
    print(ElementTree.tostring(transformed_xml_object))

if __name__ == '__main__':
    transform_xml()