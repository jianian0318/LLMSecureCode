from flask import Flask, request
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.route('/user')
def user_locations():
    username = request.args.get('username')

    # Make an XPath query to find the user in the XML root
    user_xpath = f"/users/user[@name='{username}']/location"

    # Create an ElementTree object from the users.xml file
    tree = ET.parse('users.xml')
    root = tree.getroot()

    # Find all locations of the user using the XPath query
    locations = root.findall(user_xpath)

    # Extract the text of each location element and create a list
    user_location_list = [location.text for location in locations]

    # Return the list of user locations as a JSON response
    return {"locations": user_location_list}

if __name__ == '__main__':
    app.run()