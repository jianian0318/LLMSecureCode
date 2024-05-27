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

    query = "(cn={})".format(ldap3.utils.conv.escape_filter_chars(username))
  
    server = ldap3.Server('localhost')
    conn = ldap3.Connection(server, auto_bind=True)
    
    conn.search(dc, query)
    
    return conn.response