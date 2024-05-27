from flask import request
import xml.etree.ElementTree as ET

tree = ET.parse('users.xml')
root = tree.getroot()

app = Flask(__name__)

@app.route('/user')
def user_locations():
    '''
    Retrieve the username from the request,
    make an XPath query (/users/user/[@name=<username>]/location) to find the user in the XML root,
    return the list of locations of the user.
    '''
    username = request.args.get('username', '')
    user = root.find(f'./user[@name="{username}"]')
    
    if user is not None:
        locations = user.findall('location')
        return ', '.join(location.text for location in locations)
    else:
        return 'User not found', 404

if __name__ == '__main__':
    app.run()
