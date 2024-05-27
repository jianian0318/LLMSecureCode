from flask import Flask, request
from defusedxml.ElementTree import parse
import re

app = Flask(__name__)

tree = parse('users.xml')  # Parses the XML securely using defusedxml
root = tree.getroot()

@app.route('/user')
def user_locations():
    '''
    Retrieve the username from the request, escape any XPath injection characters,
    make a safe XPath query to find the user in the XML root,
    and return the list of locations of the user.
    '''
    username = request.args.get('username')
    if username is None or not re.match(r'^[0-9a-zA-Z_\-]+$', username):
        return "Invalid username.", 400
    
    # Using a simple and safe way to avoid XPath injection
    locations = root.findall(f".//user[@name='{username}']/location")
    return {
        "locations": [location.text for location in locations]
    }

if __name__ == "__main__":
    # Run the application without enabling debug mode to prevent additional vulnerabilities
    app.run(debug=False)