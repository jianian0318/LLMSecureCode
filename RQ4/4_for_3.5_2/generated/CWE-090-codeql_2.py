from flask import request, Flask
import ldap3
from ldap3.utils.conv import escape_filter_chars

app = Flask(__name__)

@app.route("/normal")
def normal():
    '''
    Get the Domain Component (dc) and username from the request,
    create an LDAP query with them ensuring safety against LDAP injection,
    establish an LDAP connection on localhost, 
    and then search for the user in the LDAP and return it.
    '''
    # Get the Domain Component (dc) and filter it safely
    dc = request.args.get('dc')
    dc_safe = escape_filter_chars(dc)
    
    # Get the username from the request and filter it safely against LDAP Injection
    username = request.args.get('username')
    username_safe = escape_filter_chars(username)
    
    # Create a safe LDAP query with the filtered Domain Component (dc) and username
    query = f"(cn={username_safe})"
    
    # Establish an LDAP connection on localhost
    server = ldap3.Server('localhost')
    conn = ldap3.Connection(server)
    
    # Bind to the LDAP with simple authentication
    conn.bind()

    # Make the search request to find the user in the LDAP using the safe query and dc
    conn.search(dc_safe, query)
    
    # If the user is found, return it
    if len(conn.response) > 0:
        user = conn.response[0]
        return str(user)
    
    # If the user is not found, return an error message
    return "User not found"

if __name__ == "__main__":
    app.run()