import defusedxml.ElementTree as ET

def get_root():
    # Parse the 'resources/config.xml' file using defusedxml
    tree = ET.parse('resources/config.xml')

    # Get the root element
    root = tree.getroot()

    # Return the root element
    return root