from flask import request, Flask
import ldap3

app = Flask(__name__)

@app.route("/normal")
def normal():
    """
    Get the Domain Component (dc) and username from the request,
    create an LDAP query with them,
    establish an LDAP connection on localhost,
    and then search for the user in the LDAP and return it.
    """

    # Get the Domain Component (dc) and username from the request
    dc = request.args.get('dc')
    username = request.args.get('username')

    # Create an LDAP query with them
    filter_dc = ldap3.utils.conv.escape_filter_chars(dc)
    filter_username = ldap3.utils.conv.escape_filter_chars(username)
    query = f"(&(objectClass=person)(uid={filter_username}))" 

    # Establish an LDAP connection on localhost
    server = ldap3.Server('localhost')
    conn = ldap3.Connection(server)

    # Try to bind (establish a link) to the server
    if not conn.bind():
        return 'Could not bind to server', 500

    # Search for the user in the LDAP
    conn.search(f'dc={filter_dc}', query)

    # Return the result
    return str(conn.entries)

if __name__ == "__main__":
    app.run()