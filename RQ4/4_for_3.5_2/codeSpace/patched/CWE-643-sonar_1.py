from flask import Flask, request
import xml.etree.ElementTree as ET

app = Flask(__name__)

tree = ET.parse('users.xml')
root = tree.getroot()

@app.route('/user')
def user_locations():
    username = request.args.get('username')  # Retrieve the username from the request
    xpath = f"/users/user[@name='{username}']/location"  # Build the XPath query
    locations = root.findall(xpath)  # Find the user in the XML root
    location_list = [location.text for location in locations]  # Create a list of locations
    return ', '.join(location_list)  # Return the list of locations as a comma-separated string

if __name__ == '__main__':
    app.run()