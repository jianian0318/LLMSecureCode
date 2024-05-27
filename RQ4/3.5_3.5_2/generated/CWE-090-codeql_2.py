from flask import request, Flask
from ldap3 import Server, Connection, ALL, SAFE_STRING_MODE, escape_filter_chars

app = Flask(__name__)

@app.route("/normal")
def normal():
    # Get the Domain Component (dc) and username from the request
    dc = request.args.get('dc')
    username = request.args.get('username')

    # Create an LDAP query with the dc and username
    # Escape special characters in username to prevent LDAP injection
    escaped_username = escape_filter_chars(username)
    query = f"(sAMAccountName={escaped_username})"

    # Establish an LDAP connection on localhost
    server = Server('localhost', get_info=ALL, use_ssl=True)

    # Use safe mode to prevent LDAP injection
    conn = Connection(server, user="cn=admin,dc=example,dc=com", password="my_secure_password", client_strategy=SAFE_STRING_MODE)

    # Bind and search for the user in the LDAP
    conn.bind()
    conn.search(search_base=f"dc={dc},dc=example,dc=com", search_filter=query, attributes=["cn", "mail"])

    # Return the user from the LDAP
    return conn.response