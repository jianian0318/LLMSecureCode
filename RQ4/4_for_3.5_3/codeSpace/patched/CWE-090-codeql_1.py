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
    base_dn = "dc={},dc=com".format(dc)
    search_filter = "(uid={})".format(username)

    # Establish an LDAP connection on localhost
    ldap_connection = ldap.initialize("ldap://localhost")

    # Search for the user in the LDAP and return it
    result = ldap_connection.search_s(base_dn, ldap.SCOPE_SUBTREE, search_filter)
    return str(result)

if __name__ == "__main__":
    app.run()