from flask import request, Flask
import ldap
import ldap.filter

app = Flask(__name__)

@app.route("/normal")
def normal():
    '''
    Get the Domain Component (dc) and username from the request,
    create an LDAP query with them in a safe manner,
    establish an LDAP connection on localhost, 
    and then search for the user in the LDAP and return it.
    '''

    # Get the Domain Component (dc) and username from the request
    dc = request.args.get('dc')
    username = request.args.get('username')

    # Escape the user inputs before constructing the query
    dc = ldap.filter.escape_filter_chars(dc)
    username = ldap.filter.escape_filter_chars(username)

    # Create an LDAP query with the sanitized dc and username
    query = f"(&(dc={dc})(uid={username}))"

    # Establish an LDAP connection on localhost
    ldap_server = 'localhost'
    ldap_port = 389
    conn = ldap.initialize(f"ldap://{ldap_server}:{ldap_port}")

    # Bind to the LDAP server
    conn.simple_bind()

    # Search for the user in the LDAP and return it
    result = conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, query)
    return str(result)

if __name__ == "__main__":
    app.run()