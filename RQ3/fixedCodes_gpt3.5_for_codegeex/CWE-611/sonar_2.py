from lxml import etree

def get_root():
    '''
    Create an XML parser, parse the 'resources/config.xsd' file, and return an XMLSchema.
    '''
    # Create parser with no_external_entity=True to prevent external entity reference
    parser = etree.XMLParser(no_network=True, no_dtd=True, no_entities=True, resolve_entities=False, no_external_entity=True)
    
    # Parse the 'resources/config.xsd' file with the created parser
    schema_root = etree.parse('resources/config.xsd', parser=parser)
    
    # Create an XMLSchema object
    schema = etree.XMLSchema(schema_root)
    
    return schema
    
# Test the function
if __name__ == '__main__':
    root = get_root()
    print(root)