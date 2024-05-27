from flask import request, Flask
import ldap

app = Flask(__name__)

@app.route("/normal")
def normal():
    # Get the Domain Component (dc) and username from the request
    dc = request.args.get('dc')
    username = request.args.get('username')
    
    # Validate the dc and username inputs
    if not dc or not username:
        return "Invalid input"
    
    # Create an LDAP query with the dc and username
    ldap_filter = "(dc=" + ldap.filter.escape_filter_chars(dc) + ")(uid=" + ldap.filter.escape_filter_chars(username) + ")"
    
    # Establish an LDAP connection on localhost
    ldap_conn = ldap.initialize('ldap://localhost')
    
    # Search for the user in the LDAP and return it
    result = ldap_conn.search_s('ou=users,dc=example,dc=com', ldap.SCOPE_SUBTREE, ldap_filter)
    
    return str(result)