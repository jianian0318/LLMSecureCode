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

    # Create an LDAP query with them
    ldap_query = "uid={},dc={},dc=com".format(ldap.filter.escape_filter_chars(username), ldap.filter.escape_filter_chars(dc))

    # Establish an LDAP connection on localhost
    con = ldap.initialize('ldap://localhost')

    base_dn = "dc={},dc=com".format(ldap.filter.escape_filter_chars(dc))
    search_filter = "(uid={})".format(ldap.filter.escape_filter_chars(username))

    # Search for the user in the LDAP and return it
    res = con.search_s(base_dn, ldap.SCOPE_SUBTREE, search_filter)
    
    # Returning the result
    return str(res)

if __name__ == "__main__":
    app.run(port=8000)