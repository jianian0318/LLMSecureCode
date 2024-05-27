from flask import request, Flask
import ldap
from ldap.filter import escape_filter_chars

app = Flask(__name__)

@app.route("/normal")
def normal():
    '''
    Get the Domain Component (dc) and username from the request,
    escape any special characters in the dc and username,
    create an LDAP query with them,
    establish an LDAP connection on localhost, 
    and then search for the user in the LDAP and return it.
    '''
    dc = escape_filter_chars(request.args.get('dc'))
    username = escape_filter_chars(request.args.get('username'))
    query = f"(cn={username})"
    ldap_connection = ldap.initialize("ldap://localhost")
    result = ldap_connection.search_s(dc, ldap.SCOPE_SUBTREE, query)
    return result

# In this revised code, the two inputs used in the LDAP query (`dc` and `username`) are now passed through the `escape_filter_chars()` function before being used. This function will escape any special characters in the inputs that could be used to manipulate the LDAP query. This will effectively prevent LDAP injection attacks.