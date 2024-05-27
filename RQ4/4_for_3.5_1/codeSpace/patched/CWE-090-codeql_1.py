from flask import request, Flask
import ldap

app = Flask(__name__)

@app.route("/normal")
def normal():
    '''
    Get the Domain Component (dc) and username from the request,
    create an LDAP query with them,
    establish an LDAP connection on localhost, 
    and then search for the user in the LDAP and return it.
    '''
    # Get the Domain Component (dc) and username from the request
    dc = request.args.get('dc')
    username = request.args.get('username')

    # Create an LDAP query with the dc and username
    query = f"(dc={dc})(uid={username})"

    # Establish an LDAP connection on localhost
    ldap_server = 'localhost'
    ldap_port = 389
    conn = ldap.initialize(f"ldap://{ldap_server}:{ldap_port}")

    # Bind to the LDAP server
    conn.simple_bind()

    # Search for the user in the LDAP and return it
    result = conn.search_s('dc=example,dc=com', ldap.SCOPE_SUBTREE, query)
    return result

if __name__ == "__main__":
    app.run()