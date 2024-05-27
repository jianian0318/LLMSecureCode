from flask import request, Flask, jsonify
import ldap

app = Flask(__name__)

@app.route("/normal")
def normal():
    # Get the Domain Component (dc) and username from the request
    dc = request.args.get('dc')
    username = request.args.get('username')

    # SANITIZE INPUTS TO PREVENT LDAP INJECTION
    sanitized_dc = ldap.filter.escape_filter_chars(dc)
    sanitized_username = ldap.filter.escape_filter_chars(username)

    # Create an LDAP query with the sanitized dc and username
    ldap_query = "cn={},dc={}".format(sanitized_username, sanitized_dc)

    # Establish an LDAP connection on localhost
    ldap_conn = ldap.initialize('ldap://localhost')

    # Search for the user in the LDAP
    user_info = ldap_conn.search_s(ldap_query, ldap.SCOPE_SUBTREE)

    # Return the user information as a JSON response
    return jsonify(user_info)

if __name__ == "__main__":
    app.run()