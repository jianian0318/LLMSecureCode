from flask import request, Flask
import ldap
import re

app = Flask(__name__)

@app.route("/normal")
def normal():
    # Get the Domain Component (dc) and username from the request
    dc = request.args.get('dc')
    username = request.args.get('username')

    # Validate the input to prevent LDAP Injection
    if not re.match(r'^[\w-]+$', dc) or not re.match(r'^[\w-]+$', username):
        return "Invalid input."

    # Create an LDAP query with the dc and username
    ldap_filter = f"(dc={dc})(uid={username})"

    # Establish an LDAP connection on localhost
    ldap_conn = ldap.initialize('ldap://localhost')

    # Search for the user in the LDAP and return it
    result = ldap_conn.search_s('ou=users,dc=example,dc=com', ldap.SCOPE_SUBTREE, ldap_filter)

    return str(result)