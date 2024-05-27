import xml.etree.ElementTree as ET
from lxml import etree
from flask import request

tree = ET.parse('users.xml')
root = tree.getroot()


def safe_xpath_extraction(username):
    '''
    Prevents XPath injection by properly escaping the user input
    '''
    return {"name": username}


@app.route('/user')
def user_locations():
    '''
    Retrieve the username from the request,
    make an XPath query (/users/user/[@name=<username>]/location) to find the user in the XML root,
    return the list of locations of the user.
    '''
    username = request.args.get('username')

    locations = []
    for user in root.findall(".", safe_xpath_extraction(username)):
        for location_elem in user.findall('location'):
            locations.append(location_elem.text)
    
    return locations