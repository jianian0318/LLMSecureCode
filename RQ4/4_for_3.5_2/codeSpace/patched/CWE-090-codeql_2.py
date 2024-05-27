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
    # Get the Domain Component (dc) and username from the request
    dc = request.args.get('dc')
    username = request.args.get('username')
    
    # Create an LDAP query with the Domain Component (dc) and username
    query = f"(cn={username})"
    
    # Establish an LDAP connection on localhost
    server = ldap3.Server('localhost')
    conn = ldap3.Connection(server)
    
    # Bind to the LDAP with simple authentication
    conn.bind()
    
    # Make the search request to find the user in the LDAP
    conn.search(dc, query)
    
    # If the user is found, return it
    if len(conn.response) > 0:
        user = conn.response[0]
        return str(user)
    
    # If the user is not found, return an error message
    return "User not found"

if __name__ == "__main__":
    app.run()