from flask import request
import xml.etree.ElementTree as ET

tree = ET.parse('users.xml')
root = tree.getroot()

app = Flask(__name__)

@app.route('/user')
def user_locations():
    username = request.args.get('username', '')
    # Sanitize the input by using the escape functions from xml.sax.saxutils
    from xml.sax.saxutils import escape, quoteattr
    sanitized_username = escape(username)
    
    # Use quoteattr() to properly quote the sanitized_username in the XPath query
    user = root.find(f'./user[@name={quoteattr(sanitized_username)}]')
    
    if user is not None:
        locations = user.findall('location')
        return ', '.join(location.text for location in locations)
    else:
        return 'User not found', 404

if __name__ == '__main__':
    app.run()