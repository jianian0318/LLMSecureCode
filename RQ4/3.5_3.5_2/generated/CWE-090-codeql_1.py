@app.route("/normal", methods=["GET"])
def normal():
    '''
    Get the Domain Component (dc) and username from the request,
    create an LDAP query with them,
    establish an LDAP connection on localhost,
    and then search for the user in the LDAP and return it.
    '''
    dc = request.args.get("dc")
    username = request.args.get("username")

    # Create LDAP query
    query = f"(dc={dc})(username={username})"

    # Establish LDAP connection
    ldap_connection = ldap.initialize("ldap://localhost")

    # Search for the user in LDAP
    result = ldap_connection.search_s("", ldap.SCOPE_SUBTREE, query)

    # Return the user
    return result