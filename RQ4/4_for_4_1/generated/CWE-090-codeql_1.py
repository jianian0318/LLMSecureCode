from flask import request, Flask
import ldap

app = Flask(__name__)

@app.route("/normal")
def normal():
    # get Domain Component (dc) and username from the request
    dc = request.args.get('dc')
    username = request.args.get('username')

    # create an LDAP query with them
    dn = "uid=" + username + ",dc=" + dc + ",dc=com"

    # establish an LDAP connection on localhost
    con = ldap.initialize('ldap://localhost')
    
    #default settings for LDAP
    con.set_option(ldap.OPT_REFERRALS, 0)
    base_dn = "dc={},dc=com".format(dc)
    search_filter = "uid=" + username
    
    try:
        # then search for the user in the LDAP and return it
        result = con.search_s(base_dn, ldap.SCOPE_SUBTREE, search_filter)

        # returns the result if found
        if result:
            return str(result)
        else:
            return "User not found."

    except ldap.LDAPError as e:
        return 'Unable to perform the LDAP search: ' + str(e)

if __name__ == "__main__":
    app.run(debug=False)