from flask import request, Flask
import ldap3
import re 

app = Flask(__name__)

@app.route("/normal")
def normal():
    # Get the Domain Component (dc) and username from the request
    dc = request.args.get('dc')
    username = request.args.get('username')

    # Check if the username is alphanumeric (to prevent LDAP injection)
    if not re.match('^[a-zA-Z0-9]+$', username):
        return "Invalid username"

    # Check if the dc is alphanumeric (to prevent LDAP injection)
    if not re.match('^[a-zA-Z0-9.,]+$', dc):
        return "Invalid domain component"

    # Now we escape special characters in the username using the escape_filter_chars method from ldap3.utils.conv
    # Create an LDAP query with the extracted information
    query = f"(cn={ldap3.utils.conv.escape_filter_chars(username)})"

    # Establish an LDAP connection on localhost
    server = ldap3.Server('localhost')
    connection = ldap3.Connection(server, auto_bind=True)

    # Search for the user in the LDAP and return it
    connection.search(dc, query)
    return connection.response

if __name__ == "__main__":
    app.run()