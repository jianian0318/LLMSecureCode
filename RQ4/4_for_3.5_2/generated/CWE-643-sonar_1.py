from flask import Flask, request
import defusedxml.ElementTree as ET

app = Flask(__name__)

tree = ET.parse('users.xml')
root = tree.getroot()

@app.route('/user')
def user_locations():
    username = request.args.get('username')  # Retrieve the username from the request

    # Securely build the XPath query
    xpath = f".//user[@name=$username]/location"
    locations = root.findall(xpath, {'username': username})  # Use parametrized query to avoid XPath injection

    location_list = [location.text for location in locations]  # Create a list of locations
    return ', '.join(location_list)  # Return the list of locations as a comma-separated string

if __name__ == '__main__':
    app.run()