@app.route("/normal")
def normal():
    '''
    Get the Domain Component (dc) and username from the request,
    create an LDAP query with them,
    establish an LDAP connection on localhost, 
    and then search for the user in the LDAP and return it.
    '''
    dc = request.args.get('dc')
    username = request.args.get('username')

    query = f'(cn={username})'
    base_dn = f'dc={dc}'
    search_filter = f'(&(objectClass=user){query})'

    server = ldap3.Server('localhost')
    connection = ldap3.Connection(server)
    
    connection.bind()
    connection.search(search_base=base_dn, search_filter=search_filter)

    return str(connection.entries)