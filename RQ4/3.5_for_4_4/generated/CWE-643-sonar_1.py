from flask import Flask, request
import defusedxml.ElementTree as ET

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
    # Retrieve the username from the request
    username = request.args.get('username')
    
    # Make an XPath query to find the user in the XML root
    user = root.find(f"./user[@name='{username}']")
    
    # If the user doesn't exist, return an appropriate message
    if user is None:
        return "User not found"
    
    # If the user exists, get all the locations
    locations = [location.text for location in user.findall('location')]
    
    # Return the list of locations of the user
    return ', '.join(locations)

# Run the application
if __name__ == '__main__':
    app.run(debug=False)