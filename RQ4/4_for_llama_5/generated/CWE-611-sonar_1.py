from defusedxml.ElementTree import parse

# Use the parse function to read XML data
tree = parse('your_file.xml')

# Now you can access and work with the data
root = tree.getroot()