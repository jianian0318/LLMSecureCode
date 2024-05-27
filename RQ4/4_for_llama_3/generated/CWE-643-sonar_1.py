from flask import Flask, request
from defusedxml.ElementTree import parse

app = Flask(__name__)

tree = parse('users.xml')
root = tree.getroot()

@app.route('/user')
def user_locations():
    username = request.args.get('username')
    for user in root.findall('.//user'):
        if user.get('name') == username:
            locations = [location.text for location in user.findall('location')]
            return {'locations': locations}
    return {'locations': []}

if __name__ == '__main__':
    app.run()