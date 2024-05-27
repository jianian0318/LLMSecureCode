from flask import request, Flask
import ldap3

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

    query = f"uid={username},ou=people,dc={dc},dc=com"

    ldap_connection = ldap3.initialize("ldap://localhost/")
    ldap_connection.simple_bind_s("", "")

    result = ldap_connection.search_s("dc=com", ldap3.SCOPE_SUBTREE, query)

    if result:
        return result
    else:
        return "User not found"
