from flask import request, Flask
import ldap3

app = Flask(__name__)

@app.route("/normal")
def normal():
    # Get the Domain Component (dc) and username from the request
    dc = request.args.get('dc')
    username = request.args.get('username')

    # Properly escape characters to prevent LDAP injection
    if dc:
        dc = ldap3.utils.conv.escape_filter_chars(dc)
    if username:
        username = ldap3.utils.conv.escape_filter_chars(username)

    # Create an LDAP query with the dc and username
    query = f'(&(dc={dc})(username={username}))'

    # Establish an LDAP connection on localhost
    server = ldap3.Server('localhost')
    conn = ldap3.Connection(server)

    # Bind to the LDAP connection
    conn.bind()

    # Search for the user in the LDAP using the query
    conn.search('ou=users,dc=example,dc=com', query)

    # Assume the search could be empty
    if conn.entries:
        user = conn.entries[0].entry_to_json()
    else:
        user = 'No user found'

    return user

if __name__ == "__main__":
    app.run()