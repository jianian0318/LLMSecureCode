import os
from lxml import etree


def getXmlRoot():
    '''
    Create an XML parser and parse the resources/c.xml file and return the root element
    '''

    # Define the path to the XML file
    xml_file_path = os.path.join('resources', 'c.xml')

    # Create a parser
    parser = etree.XMLParser(recover=True)

    # Parse the XML file and get the root element
    root = etree.parse(xml_file_path, parser).getroot()

    return root