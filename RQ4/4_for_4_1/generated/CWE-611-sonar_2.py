from defusedxml import lxml as dlxml

def get_root():
    '''
    Create an XML parser, parse the 'resources/config.xsd' file, and return an XMLSchema.
    '''
    parser = dlxml.defuse_stdlib()
    tree = dlxml.parse('resources/config.xsd', parser)
    schema = dlxml.etree.XMLSchema(tree)
    return schema