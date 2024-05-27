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
    
    # creating LDAP query
    query = '(&(objectClass=person)(sAMAccountName={}))'.format(username)
    
    # establish LDAP connection
    server = ldap3.Server('localhost')
    conn = ldap3.Connection(server)
    conn.bind()   # assuming anonymous access is allowed
    
    # search user in LDAP
    conn.search('dc={}'.format(dc), query)
    result = conn.entries
    
    # unbind and close the connection
    conn.unbind()
    
    return str(result)
    
if __name__ == "__main__":
    app.run()