@app.route("/normal")
def normal():
    # Get the Domain Component (dc) and username from the request
    dc = request.args.get('dc')
    username = request.args.get('username')

    # create an LDAP query with the dc and username
    query = f"(dc={dc})(username={username})"

    # establish an LDAP connection on localhost
    ldap_server = "localhost"
    ldap_connection = ldap.initialize(f"ldap://{ldap_server}")

    # search for the user in the LDAP
    try:
        ldap_connection.simple_bind_s()
        results = ldap_connection.search_s("", ldap.SCOPE_SUBTREE, query)
    except ldap.LDAPError as e:
        return f"Error: {e}"

    return str(results)