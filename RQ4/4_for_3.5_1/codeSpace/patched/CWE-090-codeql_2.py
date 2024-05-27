from flask import request, Flask
from ldap3 import Server, Connection

app = Flask(__name__)

@app.route("/normal")
def normal():
    dc = request.args.get('dc')  # Get the Domain Component (dc) from the request
    username = request.args.get('username')  # Get the username from the request
    
    query = f"(dc={dc})(username={username})"  # Create an LDAP query with the dc and username
    
    server = Server('localhost')  # Establish an LDAP server connection
    
    with Connection(server) as conn:
        conn.bind()  # Bind to the LDAP server
        
        conn.search(search_base='ou=users,dc=mydomain,dc=com', search_filter=query)  # Search for the user in the LDAP
        response = conn.entries[0] if len(conn.entries) > 0 else None  # Get the first entry if it exists
        
        return str(response)  # Return the user as a string