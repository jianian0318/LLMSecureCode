from flask import Flask, request
import xml.etree.ElementTree as ET

app = Flask(__name__)

tree = ET.parse('users.xml')
root = tree.getroot()

@app.route('/user', methods=["GET"])
def user_locations():
    username = request.args.get('username')
    user = root.findall(f"./user[@name='{username}']/location")
    return  ', '.join([location.text for location in user])

if __name__ == '__main__':
    app.run(port=5000)