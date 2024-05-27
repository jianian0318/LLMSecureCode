from flask import request
import xml.etree.ElementTree as ET

# Load the XML file and get the root element
tree = ET.parse('users.xml')
root = tree.getroot()

# Define the route for "/user"
@app.route('/user')
def user_locations():
    # Get the username from the request URL
    username = request.args.get('name')

    # Make an XPath query to find the user's location
    xpath_query = "/users/user[@name='{}']/location".format(username)
    locations = root.findall(xpath_query)

    # Create a list of location values
    location_list = []
    for location in locations:
        location_list.append(location.text)

    # Return the list of user locations
    return location_list