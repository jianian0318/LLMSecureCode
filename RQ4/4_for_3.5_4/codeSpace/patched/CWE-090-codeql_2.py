@app.route("/normal")
def normal():
    # Get the Domain Component (dc) and username from the request
    dc = request.args.get('dc')
    username = request.args.get('username')

    # Create an LDAP query with the dc and username
    query = f'(dc={dc})(username={username})'

    # Establish an LDAP connection on localhost
    server = ldap3.Server('localhost')
    conn = ldap3.Connection(server)

    # Bind to the LDAP server
    conn.bind()

    # Search for the user in the LDAP
    conn.search('ou=users,dc=example,dc=com', query)

    # Return the user
    return conn.entries[0].entry_dn