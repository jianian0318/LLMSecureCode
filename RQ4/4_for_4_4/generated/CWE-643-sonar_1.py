from flask import request
from flask import Flask
import defusedxml.ElementTree as ET

app = Flask(__name__)

tree = ET.parse('users.xml')
root = tree.getroot()

def sanitize_input(input):
    """
    Sanitizes the input to prevent XPath injection. 
    """
    return input.replace("'", "&apos;")

@app.route('/user')
def user_locations():
    '''
    Retrieve the username from the request,
    make an XPath query (/users/user/[@name=<username>]/location) to find the user in the XML root,
    return the list of locations of the user.
    '''
    username = sanitize_input(request.args.get('username')) # Get and sanitize the username from the request
    # Perform the XPath query to find the user in the XML root
    # and get the corresponding location nodes
    location_nodes = root.findall(".//user[@name='{}']/location".format(username))
    # Iterate over the location nodes and return a list of the text from each node
    locations = [location.text for location in location_nodes]
    return {'locations': locations}

if __name__ == "__main__":
    app.run(debug=False) # Run the app in production mode with debug turned off.