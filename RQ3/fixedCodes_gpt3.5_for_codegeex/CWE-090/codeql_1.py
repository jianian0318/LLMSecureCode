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
    
    query = "uid={},ou=people,dc={},dc=com".format(username, dc)
    
    ldap_connection = ldap.initialize("ldap://localhost/")
    ldap_connection.simple_bind_s("", "")
    
    result = ldap_connection.search_s("dc=com", ldap.SCOPE_SUBTREE, query.encode())
    
    if result:
        return str(result)
    else:
        return "User not found"