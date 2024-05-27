from flask import request, Flask
from ldap3 import Server, Connection, SAFE_SYNC, ALL_ATTRIBUTES, ALL, escape_filter_chars

app = Flask(__name__)

@app.route("/normal")
def normal():
    # Get the Domain Component (dc) and username from the request
    dc = escape_filter_chars(request.args.get('dc'))
    username = escape_filter_chars(request.args.get('username'))

    # Create a safe LDAP query using escaped inputs
    query = f"(&(dc={dc})(cn={username}))"

    # Establish an LDAP connection on localhost
    server = Server('localhost')
    conn = Connection(server, client_strategy=SAFE_SYNC)

    # Bind to the LDAP server with anonymous credentials
    conn.bind()

    # Search for the user in the LDAP directory
    conn.search('dc=mydomain,dc=com', query, attributes=ALL_ATTRIBUTES)

    # Return the user entry if found
    if conn.entries:
        user_entry = str(conn.entries[0])  # Convert the entry to string for a simple representation
        return user_entry
    else:
        return 'No user found'

if __name__ == '__main__':
    app.run(debug=True)