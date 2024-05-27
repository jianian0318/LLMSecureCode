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
    # Get the dc and username from the request
    dc = request.args.get('dc')
    username = request.args.get('username')
    
    # Create an LDAP query with the dc and username
    query = f'(dc={dc})(username={username})'
    
    # Establish an LDAP connection on localhost
    server = ldap3.Server('localhost')
    conn = ldap3.Connection(server)
    
    # Search for the user in the LDAP and return it
    conn.search('dc=my_domain', query)
    results = conn.entries
    return str(results)