from lxml import etree

def get_root():
    parser = etree.XMLParser(remove_blank_text=True)
    tree = etree.parse('resources/config.xsd', parser)
    return etree.XMLSchema(tree)
