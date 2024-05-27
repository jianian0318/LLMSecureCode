from flask import request, Flask
import ldap

app = Flask(__name__)

@app.route("/normal")
def normal():
    '''
    Get the Domain Component (dc) and username from the request,
    create an LDAP query with them,
    establish an LDAP connection using proper escaping on localhost, 
    and then search for the user in the LDAP and return it.
    '''
    dc = ldap.filter.escape_filter_chars(request.args.get('dc'), escape_mode=ldap.filter.ESCAPE_FILTER_CHARS)
    username = ldap.filter.escape_filter_chars(request.args.get('username'), escape_mode=ldap.filter.ESCAPE_FILTER_CHARS)
    query = f"(cn={username})"
    ldap_uri = "ldap://localhost"
    ldap.set_option(ldap.OPT_X_TLS_REQUIRE_CERT, ldap.OPT_X_TLS_NEVER)
    ldap_connection = ldap.initialize(ldap_uri)
    result = ldap_connection.search_s(dc, ldap.SCOPE_SUBTREE, query)
    return result