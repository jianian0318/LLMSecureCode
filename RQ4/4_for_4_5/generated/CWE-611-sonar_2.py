from defusedxml.lxml import parse

def get_root():
    '''
    Create an XML parser, parse the 'resources/config.xsd' file, and return the root of XML.
    '''
    xml_file_path = 'resources/config.xsd'
    try:
        xml_tree = parse(xml_file_path)
        xml_root = xml_tree.getroot()
    except Exception as e:
        print(f"Exception occurred while parsing the XML file: {str(e)}")
        return None

    return xml_root