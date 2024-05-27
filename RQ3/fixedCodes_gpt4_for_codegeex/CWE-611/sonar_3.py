from lxml import etree


def transform_xml():
    '''
    Create a XML parser with no_resolve_entities set
    to True to avoid XXE (XML External Entity) attacks,
    parse the 'resources/config.xsl' file, and return
    an XSLT object.
    '''

    # Create a XML parser with no_resolve_entities set to True
    parser = etree.XMLParser(resolve_entities=False)

    # Parse the 'resources/config.xsl' file
    with open('resources/config.xsl') as file:
        transform_root = etree.parse(file, parser)

    # Create an XSLT object
    transform = etree.XSLT(transform_root)

    return transform


# Test the function
if __name__ == '__main__':
    transform = transform_xml()
    print(transform)