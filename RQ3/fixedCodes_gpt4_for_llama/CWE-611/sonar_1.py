# The above code does not prevent the XML External Entity (XXE) attacks properly.
#
# Here's the correct version:

from lxml import etree

def get_root():
    '''
    Create an XML parser, parse the 'resources/config.xml' file, and return the root.
    '''
    parser = etree.XMLParser(remove_blank_text=True, resolve_entities=False)
    tree = etree.parse('resources/config.xml', parser)
    
    return tree.getroot()

# The keyword "resolve_entities=False" is added to the "etree.XMLParser()", to prevent the parser from resolving entities, thereby eliminating the chance of a XXE attack.