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
    # Get the Domain Component and username from the request
    dc = request.args.get('dc')
    username = request.args.get('username')

    # Create an LDAP query with them
    search_filter = "(uid=" + ldap.filter.escape_filter_chars(username) + ")"
    base_dn = "dc=" + ldap.filter.escape_filter_chars(dc)

    # Establish an LDAP connection on localhost
    con = ldap.initialize('ldap://localhost')

    # Search for the user in the LDAP and return it
    results = con.search_s(base_dn, ldap.SCOPE_SUBTREE, search_filter)
    return str(results)