from flask import request, Flask
import ldap3

app = Flask(__name__)

@app.route("/normal")
def normal():
    # Get the Domain Component (dc) and username from the request
    dc = request.args.get('dc')
    username = request.args.get('username')

    # Create an LDAP query with them
    ldap_query = "(uid={})".format(username)
    user_dn = "uid={},dc={},dc=com".format(username, dc)
    
    # Establish an LDAP connection on localhost
    server = ldap3.Server('localhost')
    conn = ldap3.Connection(server)

    # Connect to the server
    if not conn.bind():
        return 'Error in server connection'

    # Search for the user in the LDAP and return it
    conn.search(search_base=user_dn,
                search_filter=ldap_query,
                search_scope=ldap3.SUBTREE,
                attributes=ldap3.ALL_ATTRIBUTES)

    # Get the search results
    results = conn.entries

    # Close the connection
    conn.unbind()
    
    return str(results)
    
if __name__ == "__main__":
    app.run()