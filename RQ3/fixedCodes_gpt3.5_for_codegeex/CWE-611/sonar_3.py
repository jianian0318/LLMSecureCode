from lxml import etree


def transform_xml():
    '''
    Create an XML parser with entity and DTD loading disabled,
    parse the 'resources/config.xsl' file,
    and return an XSLT object.
    '''
    # Disable entity and DTD loading
    parser = etree.XMLParser(no_network=True, resolve_entities=False)

    # Parse the 'resources/config.xsl' file
    transform_root = etree.parse('resources/config.xsl', parser)

    # Create an XSLT object
    transform = etree.XSLT(transform_root)

    return transform


# Test the function
if __name__ == '__main__':
    transform = transform_xml()
    print(transform)