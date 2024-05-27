from flask import request, Flask
import ldap3
from ldap3.utils.conv import escape_filter_chars

app = Flask(__name__)

@app.route("/normal")
def normal():
    # Get the Domain Component (dc) and username from the request
    domain_component = escape_filter_chars(request.args.get('dc'))     # prevent LDAP injection
    username = escape_filter_chars(request.args.get('username'))       # prevent LDAP injection
    
    # Assuming we are using 'dc=example,dc=com' as the base DN for the LDAP search
    base_dn = f"dc={domain_component},dc=com"
    
    # Creating an LDAP query
    search_filter = f"(uid={username})"
    
    # Establish an LDAP connection on localhost
    server = ldap3.Server('localhost')
    conn = ldap3.Connection(server)
    
    try:
        # Attempt to bind to the server.
        if conn.bind():
            # Perform the search for the user in the LDAP
            conn.search(search_base=base_dn, search_filter=search_filter, attributes=ldap3.ALL_ATTRIBUTES)
            
            # Fetch the search results
            results = conn.entries
            
            # Unbind the connection
            conn.unbind()
            
            # Return the result as a string
            return str(results)
        else:
            conn.unbind()
            return 'Error: Unable to bind to LDAP server', 500
    except ldap3.core.exceptions.LDAPException:
        return 'An internal server error occurred. Please try again later.', 500      # updated

if __name__ == "__main__":
    app.run(debug=False)      # updated