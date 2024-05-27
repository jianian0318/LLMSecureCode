@app.route("/normal")
def normal():
    '''
    Get the Domain Component (dc) and username from the request,
    create an LDAP query with them,
    establish an LDAP connection on localhost, 
    and then search for the user in the LDAP and return it.
    '''
    # Get the Domain Component (dc) and username from the request
    dc = request.args.get('dc')
    username = request.args.get('username')

    # Create an LDAP query
    query = '(&(objectclass=user)(cn={})(dc={}))'.format(username, dc)

    # Establish an LDAP connection on localhost
    conn = ldap.initialize('ldap://localhost')

    try:
        # Bind the connection with LDAP credentials
        conn.simple_bind_s("username", "password")

        # Search for the user in the LDAP
        result = conn.search_s(dc, ldap.SCOPE_SUBTREE, query)

        # Return the user
        return str(result)
    except ldap.LDAPError as e:
        # Handle any LDAP errors
        return str(e)
    finally:
        # Close the LDAP connection
        conn.unbind()