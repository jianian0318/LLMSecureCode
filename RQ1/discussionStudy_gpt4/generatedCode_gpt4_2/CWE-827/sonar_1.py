import os
from lxml import etree

def getXmlRoot():
    '''
    Create an XML parser and parse the resources/c.xml file and return the root element
    '''
    parser = etree.XMLParser(remove_blank_text=True)
    root = etree.parse(os.path.join('resources', 'c.xml'), parser).getroot()
    
    return root