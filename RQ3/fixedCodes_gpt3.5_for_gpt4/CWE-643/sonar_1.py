from flask import Flask, request
import xml.etree.ElementTree as ET

app = Flask(__name__)

tree = ET.parse('users.xml')
root = tree.getroot()

@app.route('/user', methods=['GET'])
def user_locations():
    # Retrieve the username from the request
    username = request.args.get('username')
    
    # make an XPath query to find the user in the XML root
    query = f".//user[@name='{username}']/location"
    
    # return the list of locations of the user if username exists and is not manipulated
    if username is not None and root.find(query) is not None:
        locations = [element.text for element in root.findall(query)]
        return {'locations': locations}
    else:
        return {'error': 'User not found or invalid username provided'}

if __name__ == "__main__":
    app.run(debug=True)