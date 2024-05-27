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
    username = request.args.get('username')
    xpath_query = f".//user[@name='{username}']/location"
    locations = [location.text for location in root.findall(xpath_query)]
    return {"locations": locations}

if __name__ == '__main__':
    app.run(debug=False)