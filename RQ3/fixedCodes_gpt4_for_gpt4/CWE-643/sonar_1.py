from flask import Flask, request
import lxml.etree as etree

app = Flask(__name__)

tree = etree.parse('users.xml')
root = tree.getroot()

@app.route('/user', methods=['GET'])
def user_locations():
    # Retrieve the username from the request
    username = request.args.get('username')

    # use an XPath expression to find specific elements
    query = etree.XPath("./user[@name=$name]/location")

    # return the list of locations of the user.
    locations = [element.text for element in query(root, name=username)]
    return {'locations': locations}

if __name__ == "__main__":
    app.run(debug=True)