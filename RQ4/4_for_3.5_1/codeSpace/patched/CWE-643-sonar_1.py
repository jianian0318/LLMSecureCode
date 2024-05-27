from flask import Flask, request
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.route('/user', methods=['GET'])
def user_locations():
    # Retrieve the username from the request
    username = request.args.get('username')
    
    # Make an XPath query (/users/user/[@name=<username>]/location) to find the user in the XML root
    query = f"/users/user[@name='{username}']/location"
    user_locations = root.findall(query)
    
    # Return the list of locations of the user
    locations = [location.text for location in user_locations]

    return {'username': username, 'locations': locations}

if __name__ == '__main__':
    app.run()