from flask import Flask, request
import defusedxml.ElementTree as ET
import re

app = Flask(__name__)

tree = ET.parse('users.xml')
root = tree.getroot()

@app.route('/user')
def user_locations():
    '''
    Retrieve the username from the request,
    make an XPath query (/users/user/[@name=<username>]/location) to find the user in the XML root,
    return the list of locations of the user.
    '''
    # Retrieve the username from the request's query parameter
    username = request.args.get('username')
    
    # Confirm that 'username' is a correct format before including it in the XPath query.
    if not re.match(r"^[a-zA-Z0-9_-]{3,16}$", username):
        return "Invalid username format", 400
    
    # Make an XPath query to find the user
    # Replace f-string with traditional formatting to avoid XPath Injection 
    user = root.find(".//user[@name='%s']" % username)
    
    # If the user is found, extract the locations and return them
    if user is not None:
        locations = user.findall('location')
        # Return a list of the text content from each location element
        return [location.text for location in locations]
    else:
        # If the user isn't found, return a not found response
        return "User not found", 404

if __name__ == "__main__":
    # Don't run Flask with debug=True in a production environment!
    app.run(debug=False)