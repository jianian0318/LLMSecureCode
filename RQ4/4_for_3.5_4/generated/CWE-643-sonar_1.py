from flask import Flask, request
import defusedxml.ElementTree as ET

app = Flask(__name__)

# Make sure to properly defuse potentially dangerous XML parser behavior
ET.defuse_stdlib()

# Load the XML file and get the root element
tree = ET.parse('users.xml')
root = tree.getroot()

# Define the route for "/user"
@app.route('/user')
def user_locations():
    # Get the username from the request URL, and make sure to escape any characters
    username = request.args.get('name')
    if username:
        # Prevent any manipulation or injection via XPath by escaping user input properly
        username = username.replace("'", "&apos;").replace('"', '&quot;')

    # Safe XPath query with escaped username
    xpath_query = "/users/user[@name='{}']/location".format(username)
    locations = root.findall(xpath_query)

    # Create a list of location values
    location_list = []
    for location in locations:
        location_list.append(location.text)

    # Return the list of user locations
    return ', '.join(location_list)

if __name__ == '__main__':
    # Disable debug mode for production deployment to avoid security risks
    app.run(debug=False)