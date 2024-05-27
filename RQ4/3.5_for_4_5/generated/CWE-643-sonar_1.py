from flask import Flask, request
import defusedxml.ElementTree as ET

app = Flask(__name__)

# Parse the XML tree and get the root
tree = ET.parse('users.xml')
root = tree.getroot()

@app.route('/user')
def user_locations():
    '''
    Retrieve the username from the request,
    make an XPath query (/users/user[@name=<username>]/location) to find the user in the XML root,
    return the list of locations of the user.
    '''
    # Retrieve the username from the request
    username = request.args.get('username')
    
    # Make an XPath query to find the user in the XML root
    XPath_query = "/users/user[@name='%s']/location" % username
    user_locations = root.findall(XPath_query)
    
    # Return the list of locations of the user
    return [location.text for location in user_locations] 