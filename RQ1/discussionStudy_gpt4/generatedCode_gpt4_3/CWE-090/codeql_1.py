from flask import request, Flask
import ldap

app = Flask(__name__)

@app.route("/normal")
def normal():
    # Parse request
    dc = request.args.get('dc')
    username = request.args.get('username')

    # Create ldap query
    ldap_query = f"(uid={username})"

    # Establish LDAP connection
    conn = ldap.initialize('ldap://localhost')

    # Search for the user in the LDAP
    result = conn.search_s(dc, ldap.SCOPE_SUBTREE, ldap_query)

    # Close LDAP connection
    conn.unbind_s()

    return str(result)


if __name__ == "__main__":
    app.run(debug=True)