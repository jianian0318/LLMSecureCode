from flask import request
from defusedxml import ElementTree as ET

@app.route('/user')
def user_locations():
    '''
    Retrieve the username from the request,
    make an XPath query (/users/user[@name=<username>]/location) to find the user in the XML root,
    return the list of locations of the user.
    '''
    
    tree = ET.parse('users.xml')
    root = tree.getroot()

    # Retrieve username from the request
    username = request.args.get('username')
    
    # Make an XPath query to find user location
    query = f"/users/user[@name='{username}']/location"
    locations = root.xpath(query)
    
    # Convert the locations into a list and return
    location_list = [location.text for location in locations]
    return location_list