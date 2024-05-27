import os
from lxml import etree

def transform_xml():
    '''
    Create a XML parser, parse the 'resources/config.xsl' file,
    and return an XSLT object.
    '''
    # Check if the .xsl file exists
    if not os.path.exists('resources/config.xsl'):
        raise FileNotFoundError("File 'resources/config.xsl' not found.")

    # Parse the .xsl file
    xsl_doc = etree.parse("resources/config.xsl")

    # Create an XSLT object
    xslt_transformer = etree.XSLT(xsl_doc)

    return xslt_transformer