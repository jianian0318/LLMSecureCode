from flask import Flask, request
import xml.etree.ElementTree as ET

app = Flask(__name__)

tree = ET.parse('users.xml')
root = tree.getroot()

@app.route('/user', methods=['GET'])
def user_locations():
    # Retrieve the username from the request
    username = request.args.get('username')
    
    # make an XPath query (/users/user/[@name=<username>]/location) to find the user in the XML root,
    query = f"./user[@name='{username}']/location"

    # return the list of locations of the user.
    locations = [element.text for element in root.findall(query)]
    return {'locations': locations}

if __name__ == "__main__":
    app.run(debug=True)