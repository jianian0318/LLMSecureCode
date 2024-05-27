from flask import Flask, request
import xml.etree.ElementTree as ET

app = Flask(__name__)

tree = ET.parse('users.xml')
root = tree.getroot()


@app.route('/user')
def user_locations():
    username = request.args.get('username')

    xpath_query = f'./user[@name="{username}"]/location'
    
    locations = root.findall(xpath_query)
    
    return ', '.join([location.text for location in locations])


if __name__ == "__main__":
    app.run()