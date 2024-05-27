from lxml.etree import XSLT
from defusedxml.lxml import fromstring
from lxml.etree import tostring

def transform_xml():
    # Read the contents of the 'resources/config.xsl' file.
    with open('resources/config.xsl', 'r') as f:
        xslt_content = f.read()

    # Create an XSLT object from the 'resources/config.xsl' string data.
    xslt_tree = fromstring(xslt_content.encode('utf-8'))
    xslt_object = XSLT(xslt_tree)

    # Parse the 'resources/config.xml' file safely using defusedxml.
    with open('resources/config.xml', 'r') as f:
        xml_content = f.read()

    # Now we have to use lxml.fromstring because defusedxml does not have XSLT processing capabilities.
    # However, this should be safe as we are now working with a trusted source - the result of our XSLT transform.
    xml_tree = fromstring(xml_content.encode('utf-8'))
    
    # Use the XSLT object to transform the XML content.
    transformed_tree = xslt_object(xml_tree)

    # Create a new 'resources/config.json' file and write the transformed JSON data to it.
    with open('resources/config.json', 'w') as f:
        f.write(str(transformed_tree))

# Call the function
transform_xml()