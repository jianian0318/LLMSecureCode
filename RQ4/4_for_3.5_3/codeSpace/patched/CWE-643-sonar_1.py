from flask import request
import xml.etree.ElementTree as ET

tree = ET.parse('users.xml')
root = tree.getroot()

@app.route('/user')
def user_locations():
    username = request.args.get('username')  # Get the username from the request arguments
    locations = []
    for user in root.findall("user[@name='{}']".format(username)):  # Find the user in the XML root
        location = user.find('location').text  # Get the location of the user
        locations.append(location)

    return ', '.join(locations)  # Return the list of locations as a string, separated by commas