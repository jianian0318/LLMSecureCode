from flask import request, Flask
from ldap3.utils.conv import escape_filter_chars
import ldap

app = Flask(__name__)

@app.route("/normal")
def normal():
    # Get the Domain Component (dc) and username from the request
    dc = escape_filter_chars(request.args.get('dc'))
    username = escape_filter_chars(request.args.get('username'))

    # Create a safe LDAP query
    query = f"(uid={username})"

    # Establish an LDAP connection on localhost
    ldap_connection = ldap.initialize("ldap://localhost")

    # Search for the user safely in the LDAP and return it
    result = ldap_connection.search_s(dc, ldap.SCOPE_SUBTREE, query)
    
    return result

if __name__ == "__main__":
    app.run()