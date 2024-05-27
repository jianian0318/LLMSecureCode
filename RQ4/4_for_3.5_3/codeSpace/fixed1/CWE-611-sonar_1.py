from defusedxml.lxml import parse

def get_root():
    # Parse the 'resources/config.xml' file using defusedxml which is safe against XML attacks
    tree = parse('resources/config.xml')

    # Return the root
    root = tree.getroot()
    return root