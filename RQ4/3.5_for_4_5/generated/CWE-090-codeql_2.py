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

    # Extracting the Domain Component (dc) and username from the request
    dc = request.args.get('dc')
    username = request.args.get('username')

    # Creating an LDAP query with safely escaping user-controlled input
    search_filter = "(&(objectClass=user)(sAMAccountName={}))".format(ldap3.utils.conv.escape_filter_chars(username))

    # Establish an LDAP connection
    server = ldap3.Server('localhost')
    conn = ldap3.Connection(server)

    # Search for the user in the LDAP
    conn.search(search_base="dc={}".format(ldap3.utils.conv.escape_filter_chars(dc)), search_filter=search_filter)
    
    # Returning the user
    return conn.entries