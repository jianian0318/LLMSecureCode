from flask import request, Flask
import ldap
import ldap.filter

app = Flask(__name__)

@app.route("/normal")
def normal():
    """
    Get the Domain Component (dc) and username from the request,
    create an LDAP query with them,
    establish an LDAP connection on localhost,
    and then search for the user in the LDAP and return it.
    """
    # Get the Domain Component (dc) and username from the request
    dc = request.args.get('dc')
    username = request.args.get('username')

    # Create an LDAP query with them
    ldap_filter = ldap.filter.escape_filter_chars(username)
    ldif = "uid={},dc={}".format(ldap_filter, ldap_filter)

    # Establish an LDAP connection on localhost
    conn = ldap.initialize('ldap://localhost')

    # Search for the user in the LDAP and return it.
    result = conn.search_s(ldif, ldap.SCOPE_SUBTREE)
    return str(result)

if __name__ == "__main__":
    app.run()