from flask import request, Flask
import ldap3
import re

# Regular expression for LDAP injection prevention.
# Only allow alphanumeric characters, dot, dash and underscore.
LDAP_SAFE_REGEX = re.compile(r'^[\w\.-]+$')

app = Flask(__name__)

@app.route("/normal")
def normal():
    # Get the Domain Component (dc) and username from the request
    dc = request.args.get('dc')
    username = request.args.get('username')

    # Return with error if inputs are not safe
    if not (dc and LDAP_SAFE_REGEX.match(dc) and username and LDAP_SAFE_REGEX.match(username)):
        return "Invalid inputs! Only alphanumeric characters, dashes, and underscores are allowed."

    # Create an LDAP query with the dc and username
    search_filter = f"(uid={username})"
    search_base = f"dc={dc},dc=com"

    # Establish an LDAP connection on localhost
    server = ldap3.Server('localhost')
    with ldap3.Connection(server) as conn:
        # Search for the user in the LDAP
        conn.search(search_base, search_filter, ldap3.SEARCH_SCOPE_SUBTREE)
        
        # If search was successful and got at least one response, return the response
        if conn.response:
            return str(conn.response)
        else:
            return "User not found"

if __name__ == "__main__":
    app.run(debug=True)