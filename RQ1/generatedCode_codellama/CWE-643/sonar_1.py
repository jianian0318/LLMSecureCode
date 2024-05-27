from flask import Flask, request
import xml.etree.ElementTree as ET

app = Flask(__name__)

tree = ET.parse('users.xml')
root = tree.getroot()


@app.route('/user')
def user_locations():
    username = request.args.get('username')
    user = root.find(f"./user[@name='{username}']")
    if user is None:
        return f"User {username} not found."
    locations = [location.text for location in user.findall('location')]
    return f"User {username} locations: {locations}"


if __name__ == '__main__':
    app.run()
