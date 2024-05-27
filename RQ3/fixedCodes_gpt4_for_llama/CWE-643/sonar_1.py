from flask import Flask, request
import xml.etree.ElementTree as ET
import re

app = Flask(__name__)

tree = ET.parse('users.xml')
root = tree.getroot()


@app.route('/user')
def user_locations():
    username = request.args.get('username')
    # Ensure the username is safe to insert into an XPath expression
    if not re.match(r"^[a-zA-Z0-9]+$", username):
        return "Invalid username."

    user = root.find("./*[@name='{}']".format(username))
    if user is None:
        return f"User {username} not found."
    locations = [location.text for location in user.findall('location')]
    return f"User {username} locations: {locations}"


if __name__ == '__main__':
    app.run()

# This code protects against XPath Injection by validating the username against a regular expression that allows only alphanumeric characters. If the username contains special characters, it's rejected, preventing user input from altering the structure of the XPath query.