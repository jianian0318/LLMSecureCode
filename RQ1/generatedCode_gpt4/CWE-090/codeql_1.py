from flask import request, Flask
import ldap

app = Flask(__name__)

@app.route("/normal")
def normal():
    # Get the Domain Component (dc) and username from the request
    dc = request.args.get('dc')
    username = request.args.get('username')
    
    if not dc or not username:
        return {'error': 'dc and username must be provided'}, 400

    # Create an LDAP query with them
    ldap_query = f"cn={username},dc={dc}"

    # Establish an LDAP connection on localhost
    con = ldap.initialize('ldap://localhost')

    # Search for the user in the LDAP and return it.
    try:
        result = con.search_s(ldap_query, ldap.SCOPE_SUBTREE)
        return {'user': result}
    except ldap.LDAPError as e:
        return {'error': str(e)}, 500

if __name__ == "__main__":
    app.run()