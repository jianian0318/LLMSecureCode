from flask import request, Flask
import ldap3

app = Flask(__name__)

@app.route("/normal")
def normal():
    # Get the Domain Component (dc) and username from the request
    dc = request.args.get('dc')
    username = request.args.get('username')

    # Create a safe LDAP query with the dc and username
    query = f'(&(dc={ldap3.utils.conv.escape_filter_chars(dc)})(uid={ldap3.utils.conv.escape_filter_chars(username)}))'

    # Establish an LDAP connection on localhost
    server = ldap3.Server('localhost')
    conn = ldap3.Connection(server)

    # Bind to the LDAP server
    conn.bind()

    # Search for the user in the LDAP
    conn.search('ou=users,dc=example,dc=com', query)

    # Return the user
    return conn.entries[0]