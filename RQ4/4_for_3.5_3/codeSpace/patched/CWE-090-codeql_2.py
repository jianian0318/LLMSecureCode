from flask import request, Flask
from ldap3 import Server, Connection, ObjectDef, AttrDef

app = Flask(__name__)

@app.route("/normal")
def normal():
    # Get the Domain Component (dc) and username from the request
    dc = request.args.get('dc')
    username = request.args.get('username')

    # Create an LDAP query with the dc and username
    query = f"(dc={dc})(cn={username})"

    # Establish an LDAP connection on localhost
    server = Server('localhost')
    conn = Connection(server)

    # Bind to the LDAP server with anonymous credentials
    conn.bind()

    # Search for the user in the LDAP directory
    conn.search('dc=mydomain,dc=com', query)

    # Return the user entry if found
    user_entry = conn.response[0]['attributes']
    return user_entry