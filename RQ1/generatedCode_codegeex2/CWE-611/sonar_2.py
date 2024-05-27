from lxml import etree


def get_root():
    '''
    Create an XML parser, parse the 'resources/config.xsd' file, and return an XMLSchema.
    '''
    # Parse the 'resources/config.xsd' file
    schema_root = etree.parse('resources/config.xsd')

    # Create an XMLSchema object
    schema = etree.XMLSchema(schema_root)

    return schema


# Test the function
if __name__ == '__main__':
    root = get_root()
    print(root)
