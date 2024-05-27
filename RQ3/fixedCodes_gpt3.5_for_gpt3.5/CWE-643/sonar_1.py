from flask import request
import xml.etree.ElementTree as ET

tree = ET.parse('users.xml')
root = tree.getroot()

@app.route('/user')
def user_locations():
    username = request.args.get('username')

    locations = []
    for user in root.findall(f"user[@name='{username}']"):
        for location_elem in user.findall('location'):
            locations.append(location_elem.text)

    return '\n'.join(locations)