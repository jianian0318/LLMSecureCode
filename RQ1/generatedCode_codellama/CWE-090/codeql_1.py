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
    dc = request.args.get('dc')
    username = request.args.get('username')
    query = f"(cn={username})"
    ldap_connection = ldap.initialize("ldap://localhost")
    result = ldap_connection.search_s(dc, ldap.SCOPE_SUBTREE, query)
    return result
