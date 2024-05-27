from flask import request, Flask
import ldap3
from ldap3.utils.conv import escape_filter_chars

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
    
    # Escape any special characters to prevent LDAP injection
    dc = escape_filter_chars(dc)
    username = escape_filter_chars(username)
    
    # Create an LDAP query with the escaped dc and username
    query = f'&(dc={dc})(username={username})'
    
    # Establish an LDAP connection on localhost
    server = ldap3.Server('localhost')
    conn = ldap3.Connection(server)
    
    # Search for the user in the LDAP and return it
    conn.search('dc=my_domain', query)
    results = conn.entries
    return str(results)

# In this code, the python LDAP3 library's `escape_filter_chars` function is used to escape any special characters in the 'dc' and 'username', thereby preventing any potential LDAP injection. The '&' symbol is also added to ensure that all conditions must be met in the search filter.