from flask import Flask, request
from defusedxml.ElementTree import parse

app = Flask(__name__)

tree = parse('users.xml')
root = tree.getroot()

@app.route('/user', methods=['GET'])
def user_locations():
    '''
    Retrieve the username from the request,
    make an XPath query (/users/user/[@name=<username>]/location) to find the user in the XML root,
    return the list of locations of the user.
    '''
    # Retrieve the username from the request
    username = request.args.get('username')

    # Use XPath to query the XML for the 'location' element inside the user with name 'username'
    locations_xml = root.findall(f"./user[@name='{username}']/location")

    # Extract the text inside each 'location' element and put it in a list
    locations = [location.text for location in locations_xml]

    return {'locations': locations}

if __name__ == "__main__":
    app.run(debug=False)