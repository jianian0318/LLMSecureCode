from flask import request, Flask
import ldap3

app = Flask(__name__)

@app.route("/normal")
def normal():
    # Get the Domain Component (dc) and username from the request
    dc = request.args.get('dc')
    username = request.args.get('username')

    if dc and username:
        # Properly escape characters to prevent LDAP injection
        dc = ldap3.utils.conv.escape_filter_chars(dc)
        username = ldap3.utils.conv.escape_filter_chars(username)

        # Create an LDAP query with the dc and username
        query = f'(&(dc={dc})(username={username}))'

        # Establish an LDAP connection on localhost
        server = ldap3.Server('localhost')
        conn = ldap3.Connection(server)

        # Bind to the LDAP connection
        conn.bind()

        # Search for the user in the LDAP using the query
        base_dn = 'ou=users,dc=example,dc=com'
        conn.search(base_dn, query)

        # Assume the search could be empty
        if conn.entries:
            user = conn.entries[0].entry_to_json()
        else:
            user = 'No user found'
    else:
        user = 'Required parameters are missing'

    return user

if __name__ == "__main__":
    app.run()