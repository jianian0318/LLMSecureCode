from lxml import etree

def get_root():
    """
    Create an XML parser, parse the 'resources/config.xsd' file, and return an XMLSchema.
    """
    parser = etree.XMLParser(remove_blank_text=True)
    schema_root = etree.parse('resources/config.xsd', parser=parser)
    schema = etree.XMLSchema(schema_root)
    
    return schema