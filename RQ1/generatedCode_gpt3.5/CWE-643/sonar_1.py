from flask import request
import xml.etree.ElementTree as ET

tree = ET.parse('users.xml')
root = tree.getroot()


@app.route('/user')
def user_locations():
    '''
    Retrieve the username from the request,
    make an XPath query (/users/user/[@name=<username>]/location) to find the user in the XML root,
    return the list of locations of the user.
    '''
    username = request.args.get('username')

    locations = []
    for user in root.findall(f"user[@name='{username}']"):
        for location_elem in user.findall('location'):
            locations.append(location_elem.text)
    
    return locations