from lxml import etree


def transform_xml():
    '''
    Create a XML parser, parse the 'resources/config.xsl' file,
    and return an XSLT object.
    '''
    # Parse the 'resources/config.xsl' file
    transform_root = etree.parse('resources/config.xsl')

    # Create an XSLT object
    transform = etree.XSLT(transform_root)

    return transform


# Test the function
if __name__ == '__main__':
    transform = transform_xml()
    print(transform)
