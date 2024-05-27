from defusedxml.lxml import parse, fromstring, tostring
from lxml.etree import XSLT  # Ideally, we look into ensuring the XSLT processing is secure or the input to it is sanitized properly.

def transform_xml(xml_input):
    '''
    Create a secure XML parser using defusedxml to parse the 'resources/config.xsl' file securely (if loading external entities is a concern, special care is needed),
    apply the XSLT transformation to the provided XML input, and return the transformed XML.
    
    :param xml_input: XML data as a string to be transformed.
    :return: Transformed XML as a string.
    '''
    # Parse the XSLT file (still considering the need for external entities turned off or properly controlled in production)
    xslt_tree = parse('resources/config.xsl')
    xslt = XSLT(xslt_tree)

    # Parse the input XML data securely
    xml_tree = fromstring(xml_input, forbid_dtd=False, forbid_entities=True, forbid_external=True)
    
    # Apply the transformation
    transformed_tree = xslt(xml_tree)

    # Convert the transformed XML tree back to a string
    transformed_xml = tostring(transformed_tree, pretty_print=True).decode()

    return transformed_xml

# Example usage:
xml_string = """
<example>
    <item>Hello World!</item>
</example>
"""

transformed_output = transform_xml(xml_string)
print(transformed_output)