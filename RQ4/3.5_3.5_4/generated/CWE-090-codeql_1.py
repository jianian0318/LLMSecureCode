@app.route("/normal", methods=['GET'])
def normal():
    dc = request.args.get('dc')
    username = request.args.get('username')

    query = "(&(objectClass=user)(sAMAccountName={}))".format(username)
    ldap_connection = ldap.initialize("ldap://localhost")
    ldap_connection.simple_bind_s("", "")
    result = ldap_connection.search_s(dc, ldap.SCOPE_SUBTREE, query)

    return result