from flask import request, Flask
import ldap
from ldap.filter import escape_filter_chars

app = Flask(__name__)

@app.route("/normal")
def normal():
    '''
    Get the Domain Component (dc) and username from the request,
    safely create an LDAP query with them,
    establish an LDAP connection on localhost,
    and then search for the user in the LDAP and return it.
    '''

    # Get the Domain Component (dc) and username from the request, escaping any special characters
    dc = escape_filter_chars(request.args.get('dc', ''))
    username = escape_filter_chars(request.args.get('username', ''))

    # Create an LDAP query with the safely escaped dc and username
    base_dn = "dc={},dc=com".format(dc)
    search_filter = "(uid={})".format(username)

    # Establish an LDAP connection on localhost
    ldap_connection = ldap.initialize("ldap://localhost")
    ldap_connection.set_option(ldap.OPT_REFERRALS, 0)

    # Search for the user in the LDAP and return the results
    result = ldap_connection.search_s(base_dn, ldap.SCOPE_SUBTREE, search_filter)
    ldap_connection.unbind_s()
    return str(result)

if __name__ == "__main__":
    app.run()