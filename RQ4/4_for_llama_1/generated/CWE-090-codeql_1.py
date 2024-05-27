from flask import request, Flask
import ldap
from ldap.filter import escape_filter_chars

app = Flask(__name__)

@app.route("/normal")
def normal():
    # Get the Domain Component (dc) and username from the request
    dc = escape_filter_chars(request.args.get('dc'))
    username = escape_filter_chars(request.args.get('username'))

    # Safely create an LDAP query with the escaped dc and username
    query = f"(cn={username})"

    try:
        # Establish an LDAP connection on your_ldap_server_address
        ldap_connection = ldap.initialize("ldap://your_ldap_server_address")
        
        # Set LDAP protocol version, if needed, for example:
        ldap_connection.set_option(ldap.OPT_PROTOCOL_VERSION, ldap.VERSION3)
        
        # If your LDAP server needs authentication, do it here, for example:
        # ldap_connection.simple_bind_s('your_bind_dn', 'your_password')

        # Search for the user in the LDAP, using the escaped query
        result = ldap_connection.search_s(dc, ldap.SCOPE_SUBTREE, query)

        # Properly close the connection to free resources
        ldap_connection.unbind_s()
    except ldap.LDAPError:
        # Instead of revealing error details to the user, return a general error message
        return "An error occurred while reaching the server. Please try again later.", 500

    # Return the user information
    return str(result)

if __name__ == "__main__":
    app.run()