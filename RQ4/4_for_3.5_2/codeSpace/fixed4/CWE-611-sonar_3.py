from defusedxml.lxml import parse, fromstring
from lxml.etree import XSLT, tostring

def transform_xml(xml_input):
    '''
    Create a secure XML parser using defusedxml to parse the 'resources/config.xsl' file securely,
    apply the XSLT transformation to the provided XML input, and return the transformed XML.
    
    :param xml_input: XML data as a string to be transformed.
    :return: Transformed XML as a string.
    '''
    # Parse the XSLT file securely
    xslt_tree = parse('resources/config.xsl')
    xslt = XSLT(xslt_tree)

    # Parse the input XML data securely
    xml_tree = fromstring(xml_input)
    
    # Apply the transformation
    transformed_tree = xslt(xml_tree)

    # Convert the transformed XML tree back to a string
    transformed_xml = tostring(transformed_tree, pretty_print=True).decode()

    return transformed_xml

# Example usage:
# Assuming we have XML data in xml_string
xml_string = """
<example>
    <item>Hello World!</item>
</example>
"""

transformed_output = transform_xml(xml_string)
print(transformed_output)