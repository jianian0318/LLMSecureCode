from flask import Flask, request
from defusedxml import ElementTree

app = Flask(__name__)

tree = ElementTree.parse('users.xml')
root = tree.getroot()

@app.route('/user', methods=['GET'])
def user_locations():
    '''
    Retrieve the username from the request,
    make an XPath query (/users/user/[@name=<username>]/location) to find the user in the XML root,
    return the list of locations of the user.
    '''
    # Retrieve the username from query parameters in the request
    username = request.args.get('username')
    if not username:
        return "Please provide a username query parameter", 400  # Bad Request

    # Make an XPath query to find the user in the XML root
    xpath_query = f".//user[@name='{username}']/location"
    locations_elements = root.findall(xpath_query)

    # Extracting the text of the location tag and return the list of locations
    locations = [loc.text for loc in locations_elements]

    return {'locations': locations}


if __name__ == "__main__":
    app.run(debug=False)