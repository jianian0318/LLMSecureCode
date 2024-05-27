@app.route("/normal")
def normal():
    # Get the Domain Component (dc) and username from the request
    dc = request.args.get("dc")
    username = request.args.get("username")

    # Create an LDAP query with the dc and username
    query = f"(dc={dc})(username={username})"

    # Establish an LDAP connection on localhost
    conn = ldap.initialize("ldap://localhost")

    try:
        # Bind with LDAP server using default credentials
        conn.simple_bind_s()
     
        # Search for the user in the LDAP using the query
        result = conn.search_s("dc=mydomain,dc=com", ldap.SCOPE_SUBTREE, query)

        # Return the user if found
        if result:
            return result[0]

        return "User not found"
    finally:
        # Close the LDAP connection
        conn.unbind()