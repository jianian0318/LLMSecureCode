from flask import Flask, request
from defusedxml.ElementTree import parse

# Initialize Flask app
app = Flask(__name__)

# Securely parse the XML file using defusedxml
tree = parse('users.xml')
root = tree.getroot()

@app.route('/user')
def user_locations():
    username = request.args.get('username')  # Get the username from the request arguments
    locations = []

    # Securely create an XPath expression to prevent XPath injection
    for user in root.findall(".//user"):
        if user.attrib.get('name') == username:
            location = user.find('location').text  # Get the location of the user if username matches
            locations.append(location)

    return ', '.join(locations)  # Return the list of locations as a string, separated by commas

if __name__ == '__main__':
    # Removed debug=True for production to avoid exposing the debugger
    app.run()