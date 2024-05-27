from flask import request, Flask
import ldap

app = Flask(__name__)

@app.route("/normal")
def normal():
    # Get the Domain Component (dc) and username from the request
    dc = request.args.get('dc')
    username = request.args.get('username')

    # Create an LDAP query with dc and username
    ldap_search_query = f"uid={username},dc={dc}"

    # Establish an LDAP connection on localhost
    con = ldap.initialize('ldap://localhost')

    # Search for the user in the LDAP and return it
    try:
        result = con.search_s(ldap_search_query, ldap.SCOPE_SUBTREE)
        return "User found: " + str(result[0][1])
    except ldap.LDAPError:
        return 'User not found.'