from defusedxml import ElementTree

def parse_xml(xml_file):
    return ElementTree.parse(xml_file)

# Sample usage:
parsed_xml = parse_xml('example.xml')