from flask import request, Flask
import ldap
import re

app = Flask(__name__)

@app.route("/normal")
def normal():
    # Get the Domain Component (dc) and username from the request
    dc = request.args.get('dc')
    username = request.args.get('username')
    
    # Check if dc and username is None mean it does not found in request
    if dc is None or username is None:
        return 'Missing parameters!'

    # Sanitize or escape the inputs
    dc = re.escape(dc)
    username = re.escape(username)

    # Create an LDAP query with them
    query = f"(cn={username})"

    # Establish an LDAP connection on localhost
    ldap_connection = ldap.initialize("ldap://localhost")

    # Search for the user in the LDAP and return it
    result = ldap_connection.search_s(dc, ldap.SCOPE_SUBTREE, query)
    return str(result)

if __name__ == "__main__":
    app.run()