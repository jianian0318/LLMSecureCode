from flask import request, Flask
import ldap
from ldap.filter import escape_filter_chars

app = Flask(__name__)

@app.route("/normal")
def normal():
    # Get the Domain Component (dc) and username from the request
    dc = escape_filter_chars(request.args.get('dc'))
    username = escape_filter_chars(request.args.get('username'))

    # Create an LDAP query with them
    ldap_query = "uid={},dc={}".format(username, dc)

    # Establish an LDAP connection on localhost
    con = ldap.initialize('ldap://localhost')

    # Search for the user in the LDAP
    result = con.search_s(ldap_query, ldap.SCOPE_SUBTREE)

    # Return it
    return {
        'user': result
    }

if __name__ == "__main__":
    app.run()