from flask import request
from defusedxml.ElementTree import parse

tree = parse('users.xml')
root = tree.getroot()

@app.route('/user')
def user_locations():
    '''
    Retrieve the username from the request,
    make a safe XPath query (/users/user[@name='<username>']/location) to find the user in the XML root,
    return the list of locations of the user.
    '''

    # Retrieve the username from the request
    username = request.args.get('username')

    # Make a safe XPath query to find the user in the XML root
    xpath_query = f"/users/user[@name='{username}']/location"
    locations = root.findall(xpath_query)

    # Create a list of the locations
    location_list = [location.text for location in locations]

    return location_list